---
title: "Writing Prolog with ChatGPT"
url: "https://www.johndcook.com/blog/2026/06/15/writing-prolog-with-chatgpt/"
fetched_at: 2026-06-16T07:00:49.079248+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Writing Prolog with ChatGPT

Source: https://www.johndcook.com/blog/2026/06/15/writing-prolog-with-chatgpt/

A few days ago
I wrote about using Claude to solve a chess puzzle by writing Prolog code. This morning I tried a
similar chess puzzle
with ChatGPT. The task is to place a queen, king, rook, bishop, and knight on a 4 by 4 chessboard so no piece attacks another.
Of course there’s not a lot of market demand for solving chess puzzles, but there is demand for solving real-world problems that amount to logic puzzles. Experiments with chess puzzles suggest writing Prolog with LLM help might be pleasant. The syntax of Prolog can be a little odd, but the LLM handles that. And because Prolog has been around so long without changing much, you’d expect LLMs to be good at generating code in it. [1]
I gave ChatGPT this prompt:
Write a SWI Prolog program to solve the following chess puzzle. Place a queen, king, rook, bishop, and knight on a 4 by 4 chessboard so no piece attacks another. Print all solutions.
It produced a file
chess4.pl
(below) that I ran with
swipl -q -s chess4.pl -g solve -t halt
It found all 16 solutions:
Solution 1:
  queen=1-2  king=2-4  rook=3-1  bishop=4-3  knight=4-4
. K . N
. . . B
Q . . .
. . R .

Solution 2:
  queen=1-2  king=4-3  rook=2-4  bishop=3-1  knight=4-1
. R . .
. . . K
Q . . .
. . B N

...
Here’s the code.
% chess4.pl
% Place queen, king, rook, bishop, and knight on a 4x4 board
% so that no piece attacks another.

:- use_module(library(lists)).

square(X-Y) :-
    between(1, 4, X),
    between(1, 4, Y).

solve :-
    findall(Board, solution(Board), Boards),
    print_solutions(Boards, 1),
    length(Boards, Count),
    format('Total solutions: ~d~n', [Count]).

solution(Board) :-
    Pieces = [queen, king, rook, bishop, knight],
    findall(S, square(S), Squares),
    place_pieces(Pieces, Squares, Board),
    safe(Board).

place_pieces([], _, []).
place_pieces([Piece | Pieces], Squares, [Piece-Square | Board]) :-
    select(Square, Squares, RemainingSquares),
    place_pieces(Pieces, RemainingSquares, Board).

safe(Board) :-
    safe(Board, Board).

safe([], _).
safe([Piece-Square | Rest], Board) :-
    forall(
        member(OtherPiece-OtherSquare, Rest),
        non_attacking(Piece-Square, OtherPiece-OtherSquare, Board)
    ),
    safe(Rest, Board).

non_attacking(P1-S1, P2-S2, Board) :-
    \+ attacks(P1, S1, S2, Board),
    \+ attacks(P2, S2, S1, Board).

% Attack rules

attacks(king, X1-Y1, X2-Y2, _) :-
    X1-Y1 \= X2-Y2,
    DX is abs(X1 - X2),
    DY is abs(Y1 - Y2),
    DX =< 1,
    DY =< 1. attacks(knight, X1-Y1, X2-Y2, _) :- DX is abs(X1 - X2), DY is abs(Y1 - Y2), ( DX =:= 1, DY =:= 2 ; DX =:= 2, DY =:= 1 ). attacks(rook, S1, S2, Board) :- same_rank_or_file(S1, S2), clear_line(S1, S2, Board). attacks(bishop, S1, S2, Board) :- same_diagonal(S1, S2), clear_line(S1, S2, Board). attacks(queen, S1, S2, Board) :- ( same_rank_or_file(S1, S2) ; same_diagonal(S1, S2) ), clear_line(S1, S2, Board). same_rank_or_file(X1-Y1, X2-Y2) :- ( X1 =:= X2 ; Y1 =:= Y2 ). same_diagonal(X1-Y1, X2-Y2) :- DX is abs(X1 - X2), DY is abs(Y1 - Y2), DX =:= DY. % For sliding pieces, make sure no piece blocks the path. clear_line(X1-Y1, X2-Y2, Board) :- step(X1, X2, SX), step(Y1, Y2, SY), NX is X1 + SX, NY is Y1 + SY, clear_path(NX-NY, X2-Y2, SX-SY, Board). clear_path(Target, Target, _, _) :- !. clear_path(X-Y, Target, SX-SY, Board) :- \+ occupied(X-Y, Board), NX is X + SX, NY is Y + SY, clear_path(NX-NY, Target, SX-SY, Board). step(A, B, 0) :- A =:= B. step(A, B, 1) :- B > A.
step(A, B, -1) :-
    B < A.

occupied(Square, Board) :-
    member(_-Square, Board).

% Printing

print_solutions([], _).
print_solutions([Board | Rest], N) :-
    format('Solution ~d:~n', [N]),
    print_coordinates(Board),
    print_board(Board),
    nl,
    N1 is N + 1,
    print_solutions(Rest, N1).

print_coordinates(Board) :-
    member(queen-Q, Board),
    member(king-K, Board),
    member(rook-R, Board),
    member(bishop-B, Board),
    member(knight-N, Board),
    format('  queen=~w  king=~w  rook=~w  bishop=~w  knight=~w~n',
           [Q, K, R, B, N]).

print_board(Board) :-
    forall(
        between(1, 4, Row0),
        (
            Y is 5 - Row0,
            forall(
                between(1, 4, X),
                (
                    piece_at(X-Y, Board, Symbol),
                    format('~w ', [Symbol])
                )
            ),
            nl
        )
    ).

piece_at(Square, Board, Symbol) :-
    member(Piece-Square, Board),
    !,
    piece_symbol(Piece, Symbol).
piece_at(_, _, '.').

piece_symbol(queen,  'Q').
piece_symbol(king,   'K').
piece_symbol(rook,   'R').
piece_symbol(bishop, 'B').
piece_symbol(knight, 'N').
[1] I’ve played around with generating Prolog and Lean this weekend, and I’ve had better results with Prolog. The problems with Lean haven’t been Lean per se but the Mathlib library. The library is frequently refactored, which makes sense for a young language, but this makes it harder to generate and debug code.
