---
title: "Why Does Software Contain Bugs?"
url: "https://boyter.org/2015/07/software-bugs/"
fetched_at: 2026-05-05T07:02:01.912974+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Why Does Software Contain Bugs?

Source: https://boyter.org/2015/07/software-bugs/

“Why does all software contain bugs?” this was a question recently asked of me. My response at the time was because all software is not perfect, but is this true?
Lets take a very simple example.
public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
The above example is arguably the simplest program that can be written using Java. It also happens to be the first program usually written by any Java programmer. It simply print outs the text “Hello World!” when it is run. Surely this program is so simple that it is perfect and therefore bug free?
Ignoring the obvious that this program does nothing useful, lets assume for the moment that we have been tasked to write a “Hello World!” program in Java. Surely the above is 100% bug free.
Yes. The application is 100% bug free. But thats not the whole story. What happens when this application run?
The first thing to happen is it needs to be compiled. This takes the application from its text form converting it into something that the computer can understand. In the case of Java it turns it into something the Java Virtual Machine can understand. This allows you to take the same compiled program and in theory run it on your computer, phone, playstation, blu ray, ipad or any other device that runs Java.
The Java Virtual Machine or JVM is itself a compiled program running on a device. The catch is that it is compiled using a different compiler for every platform (computer, phone etc…). When it runs it takes your compiled application and converts the instructions into something that the computer understands.
However underneath the JVM is usually the Operating System. This hands out resources to the programs that are running. So the JVM runs inside the operating system and the operating system talks to the physical hardware.
Actually while the operating system does talk to the hardware directly there is usually software inside the hardware itself which controls the actual hardware these days. Not only does the hardware contain software the hardware itself such as a CPU is literally software turned into hardware. This means CPU’s and the like can also contain bugs.
This means in order for your perfect application to run perfectly the following pieces of software also need to run perfectly,
Your Program -> Java Compiler -> JVM -> JVM Compiler -> Operating System -> Operating System Compiler -> Hardware Software -> Hardware Software Compiler -> Hardware Itself
As you can see it really is an iceberg with your perfect program at the top and lot of things going on underneath. Any bug in any level can result in “perfect” software not working as expected making it flawed.
This is why perfect software does not currently exist. The only way to do so would to be by writing perfect software at every level which is a monumental undertaking. There are estimates around that suggest that the cost to rewrite the Linux kernel as being around 500 billion dollars, and thats not really accounting for making it “perfect”, and as shown is literally one small piece of the puzzle.
So should we just give in? Well no. At every level there are thousands of testers and processes designed to make the software as bug free as possible. Just because we cannot reach perfection does not mean it is not at least worth trying.
