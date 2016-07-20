overview
python
computing

#   `lec01`

##  Administration

Next Monday and Wednesday are i<clicker test sessions.  Then grades count for real.


##  Motivation

##  Encouragement

Everyone can learn how to program.  It is a way of thinking about the world.

##  Class Structure

20% HW
25% Labs
10% Lecture (~5% attendace, ~5% quizzes)
20% Midterms
25% Final exam

Compass has official gradebook.

go.illinois.edu/cs101

-   homework assignments, course calendar, policies


Required supplies:
-   no textbook
-   i>clicker
-   codelab account (instructions in hw01)


lab01 begins TODAY
you MUST attend YOUR lab section

Policies
-   No late homework submissions
-   All machine generated grades are final
-   Late registrants should keep up with work
    -   Corollary:  no extensions or exceptions for late registration
-   Never copy code 


Get help at the Piazza forum
-   be civil to peers and staff
-   all posts containing solutions should be marked private

Office hours (TBA)
-   have specific questions for the TA if you want assistance

• ≈ 6-7 weeks: programming (Python)
• ≈ 5-6 weeks: engineering programming
• 2 weeks: Matlab


##  Programming

A set of instructions a computer executes
to achieve a goal
• Can be very long (millions of instructions)
• Also called “code” or “source code”
• Our programs will be called “scripts” 

Information stored in a computer is called
data.
• All data is represented in binary.
– A series of 0’s and 1’s
• Each 0 or 1 is called a bit.
• Bits are stored in groups of 8 called bytes.
00011001 11011110 00001110 11111101

• Programs are data.
• Instructions are encoded in binary.
• Each instruction is typically 4 or 8 bytes.

Programming Language
• An artificial language used to
communicate instructions to a computer
• Rigorous and unambiguous
• Grammar is mathematically formal
• Has syntax and semantics like a natural
language 

Programming Languages
• Low-level: add $t0, $t1, $t2
– Define individual, machine readable
instructions
• High-level: x=y+z
– Human readable instructions translated into
machine readable instructions 

High-level languages
• Compiled languages
– Compiler translates entire program into
machine language
• Interpreted (scripting)
– Interpreter translates program into machine
language line by line
– Translation happens “on the fly” 

Python
• High-level language
• Interpreted language
• Strongly, dynamically typed language
• WARNING: Split between versions 2 and 3. We will use version 3! 

Why Python?
• Freely available
• Cross platform
• Widely adopted
• Well documented
• Designed for teaching
• Beautiful (I don’t know if I can tell you what makes a language beautiful but I can sure tell you what makes one ugly.)

Let’s get started!




Everyone can learn how to program.

You think that you are here to learn how to program, how to write code.  You are here to learn how to think.  You are here to learn problem solving strategies and to develop a better grasp of logic.  Much of that is embodied in "code", in programming.


I'll go out on a limb here and make a prediction:  in the long run, programming will make your life easier.  Not a single one of you actually believes me.  Every engineering company is a software company today.  Every job you will ever have is a software job.  I don't care if you're a nuclear engineer, a civil engineer, a physicist, a novelist, whatever.  Even if you do not code, you will have to manage software workflows and process data.  That's a big part of what CS 101 is about.

http://www.ybrikman.com/writing/2014/05/19/dont-learn-to-code-learn-to-think/
http://www.wsj.com/news/articles/SB10001424053111903480904576512250915629460
http://search.proquest.com/docview/885059180/fulltext/CBD8033B7CC34EACPQ/14?accountid=14553
http://breakingsmart.com/season-1/
https://techcrunch.com/2016/06/07/software-is-eating-the-world-5-years-later/



Shall we get the boring bits out of the way?  Let's do that really quick.  (Some of you are thinking "yeah, right, so we can get to the *really* boring bits.")



In the beginning, mankind discovered writing.
geometry
graphical reasoning
symbolic reasoning (algebra)
This suggested to some great minds the possibility of a *calculus ratiocinator*, a universal rational calculator that could answer all questions definitively.
Later, Charles Babbage took up the idea of calculating mathematical tables mechanically.  This was a straightforward procedure in principle, although the technology of the time couldn't machine the required components properly.  Later Babbage hit on the notion of using punch cards to direct control.  Now punch cards were used with the Jacquard loom to guide weaving and embroidery.  The notion of sequential control, program branching, iteration, and computer memory were all possible with Babbage's plans, although unfortunately the Analytical Engine was never built.  (If you ever get a chance to go to the Science Museum in London, stop by and take a look at the surviving components.)
 • get Analytical Engine book

The ideas of a universal calculus were taken up by early twentieth-century mathematicians, who began to ask probing questions about what precisely we mean when we say "computation".  Alan Turing and Alonzo Church worked out the basic theoretical principles to understand how to program a general-purpose computer.  At the same time, others had taken up the idea of large-scale calculating machines—such as IBM—and large machines were built.  The first general-purpose machine (programmable to solve any computable problem) was the Z2.  Many early developments occurred due to the WW2 cryptography—the need to break enemy codes, whichever side one happened to be on.  After the war, the need for nuclear calculations at Los Alamos drove John von Neumann to work out the necessary computer science to design the MANIAC I and other early general-purpose digital computers.

Here's where the story circles back a little more closely to our challenge in this class.  Let's consider a couple of general-purpose problems and think about how we would make them into a process, or *algorithm*.  (An algorithm is just a precise set of instructions to accomplish something.  It has to be an effective method though, basically mechanical, nothing hand-waving.)

1)  How would you go about sorting all of the people in this room from tallest to shortest?  Does it make a difference if no one is thinking about it except for the guide?

2) Consider being lost in a hedge maze.  How could you find your way out?  Write a process explaining your approach.  Your response should include at least 3 steps, and you may assume any necessary supplies are available (that don’t destroy the maze or subvert the whole problem—find your way out of the maze!).

Well, with early computers the challenge was to translate processes like these into a formal language that could instruct the machine what to do.  The digital computer knows only ones and zeros.  This could be magnetic polarization on a tape, change in reflectivity on a CD, an electronic circuit on a hard disk, or anything else that has two distinct states and can be built into a machine.

This series of ones and zeros is called *machine language*.  It was difficult to do much with it, so shortly afterwards *assembly language* was invented.  This meant assigning mnemonics to the machine language, rendering it "readable" and more importantly debuggable.  These are called *low-level* languages, which fortunately for us implies the existence of *high-level* languages.

Computer designers in the 1950s introduced high-level languages, which allowed programmers to write codes that were then automatically transformed into machine language.  If the language does this ahead of time (and stored the instructions in memory), it is called a *compiled* language.  If it does it at the time it's needed (at *runtime*), it is called an *interpreted* language.
http://www.catb.org/retro/plankalkuel/

Python is an interpreted language.  At first, it will feel a bit like a graphing calculator, although it is much more powerful.

A program is a collection of instructions to the machine.  To write a program, one needs a language and an algorithm.  The language choice is easy for you:  in this class it will be Python or MATLAB.  The algorithm is generally more challenging:  it often involves decomposing the problem into smaller pieces and finding ways of solving each of those.

A trivial example:  suppose I need to calculate the number of raindrops that fell on Urbana last week.  If I break the problem into solvable units, I can come up with a process that lets me answer the question.  So I can look up the number of inches of rain (and what that means) and the number of acres of land in Urbana to get the volume of rain that fell.  Now I estimate the volume of a raindrop and do the math to get the number of raindrops that fell.
depth * area = volume
volume rain / volume drop = n drop

That was an algorithm, albeit a simple one.

So a program is an algorithm written down in a specific language.  In Python we will often call these *scripts*.

Some tasks are easy for machines but relatively hard for humans, like solving a random Rubik’s Cube.  Others are trivial for humans but nearly impossible for current computers, such as driving a car.

Reminders:
-   hw01 has been posted.
-   Next Monday and Wednesday are i>clicker test sessions.
