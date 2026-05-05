---
title: "Taming Deep Recursion"
url: "https://databasearchitects.blogspot.com/2020/11/taming-deep-recursion.html"
fetched_at: 2026-05-05T07:01:28.643571+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Taming Deep Recursion

Source: https://databasearchitects.blogspot.com/2020/11/taming-deep-recursion.html

When operating on hierarchical data structures, it is often convenient to formulate that using pairwise recursive functions. For example, our semantic analysis walks that parse tree recursively and transforms it into an expression tree. This corresponding code looks roughly like this:
unique_ptr<Expression> analyzeExpression(AST* astNode) {  
   switch (astNode->getType()) {  
    case AST::BinaryExpression: return analyzeBinaryExpression(astNode->as<BinaryExpAST>());  
    case AST::CaseExpression: return analyzeCaseExpression(astNode->as<CaseExpAST>());  
    ...  
   }  
 }  
 unique_ptr<Expression> analyzeBinaryExpression(BinaryExpAST* astNode) {  
   auto left = analyzeExpression(astNode->left);  
   auto right = analyzeExpression(astNode->right);  
   auto type = inferBinaryType(astNode->getOp(), left, right);  
   return make_unique<BinaryExpression>(astNode->getOp(), move(left), move(right), type);  
 }
It recursively walks the tree, collects input expressions, infers types, and constructs new expressions. This works beautifully until you encounter a (generated) query with 300,000 expressions, which we did. At that point our program crashed due to stack overflow. Oops.
Our first mitigation was using
__builtin_frame_address(0)
at the beginning of
analyzeExpression
to detect excessive stack usage, and to throw an exception if that happens. This prevented the crash, but is not very satisfying. First, it means we refuse a perfectly valid SQL query "just" because it uses 300,000 terms in one expression. And second, we cannot be sure that this is enough. There are several places in the code that recursively walk the algebra tree, and it is hard to predict their stack usage. Even worse, the depth of the tree can change due to optimizations. For example, when a query has 100,000 entries in the from clause, the initial tree is extremely wide but flat. Later, after we have stopped checking for stack overflows, the optimizer might transform that into a tree with 100,000 levels, again leading to stack overflow. Basically, all recursive operations on the algebra tree are dangerous.
Now common wisdom is to avoid recursion if we cannot bound the maximum depth, and use iteration with an explicit stack instead. We spend quite some time thinking about that approach, but the main problem with that is that it makes the code extremely ugly. The code snippet above is greatly simplified, but even there an explicit stack would be unwieldy and ugly if we have to cover both
binaryExpression
and
caseExpression
using one stack. And the code gets cut into tiny pieces due to the control flow inversion required for manual stacks. And all that to defend against something that nearly never happens. We were unhappy with that solution, we wanted something that is minimal invasive and created overhead only in the unlikely case that a user gives us an extremely deep input.
One mechanism that promises to solve this problem is
-fsplit-stack
. There, the compiler checks for stack overflows in the function prolog and creates a new stack segment if needed. Great, exactly what we wanted! We can handle deep trees, no code change, and we only create a new stack if we indeed encounter deep recursion. Except that it is not really usable in practice. First, -fsplit-stack is quite slow. We measured 20% overhead in our optimizer when enabling split stacks, and that in cases where we did not create any new stacks at all. When -fsplit-stack does create new stacks it is even worse. This is most likely a deficit of the implementation, one could implement -fsplit-stack much more efficiently, but the current implementation is not encouraging. Even worse, clang produces an
internal compiler error
when compiling some functions with -fsplit-stack. Nobody seems to use this mechanism in production, and after disappointing results we stopped considering -fsplit-stack.
But the idea of split stacks is clearly good. When encountering deep recursion we will have to switch stacks at some point. After contemplating this problem for some time we realized that
boost.context
offers the perfect mechanism for switching stacks: It can start a fiber with a given stack, and switching between fibers costs just 19 cycles. By caching additional stacks and their fibers in thread-local data structures we can provide our own implementation of split stacks that is fast and supports arbitrary code. Without compiler support the split stack mechanism is visible, of course, but that is fine in our code. We have only a few entry points like
analyzeExpression
that will be called over and over again during recursion, and checking there is enough. Code wise the mechanism is not too ugly, it needs two lines of code per recursion head and looks like
unique_ptr<Expression> analyzeExpression(AST* astNode) {  
   if (StackGuard::needsNewStack())  
    return StackGuard::newStack([=]() { return analyzeExpression(astNode); });  
   ... // unchanged  
 }
Note that the lambda argument for
newStack
will be called from within the new stack, avoiding the stack overflow. When the lambda returns the mechanism will use boost.context to switch back to the previous stack. The performance impact of that mechanism is negligible, as 1) we do not check for overflows all the time but only in the few places that we know are central to the recursive invocations, like
analyzeExpression
here, 2) stack overflows are extremely rare in practice, and we only pay with one
if
per invocation is no overflow happens, and 3) even if they do happen, the mechanism is reasonably cheap. We cache the child stacks, and switching to a cached stack costs something like 30 cycles. And we never recurse in a hot loop.
It took us a while to get there, but now we can handle really large queries without crashing. Just for fun we tried running a query with 100,000 relations in the from clause. Fortunately our optimizer
could already handle that
, and now the rest of the system can handle it, too. And that with nice, intuitive, recursive code, at the small price of two lines of code per recursion head.
