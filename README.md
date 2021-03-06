# smolBASIC

(formerly known as mi:little coder)

A very simple text-based programming language for the BBC micro:bit, written in Python.

![smolBASIC in use](https://raw.githubusercontent.com/blogmywiki/smolBASIC/main/images/alpha-editor-screenshot-small.png)

## Tell me more, tell me more
smolBASIC runs on a micro:bit connected to any serial console via USB. The serial console can be the official micro:bit Python editor in a Chrome or Edge web browser.

smolBASIC could be a child's first text-based programming language, but it's also simple enough students can modify it themselves, for example adding instructions to show more images or access more sensors on the micro:bit or play more sounds. It could be used in KS3 in England to satisfy the requirement to teach a text-based language, and it could be accessible to more students than other, more complex languages.

Students could also translate the smolBASIC commands into other languages, to give younger students the opportunity to do some text-based coding in their mother tongue.

Its sheer simplicty also allows students to access some of the clarity of thought that comes with learning assembly language or machine code, but without having to learn hexadecimal, binary or memorise op codes.

As a first text-based langauge, it aims to be as simple as possible, so it avoids punctuation like quotation marks around strings or brackets that students find hard to type.

Programs have no line numbers when entered, but lines do have numbers when listed (mainly to allow 'goto' statements to work).

Every instruction takes half a second to execute. The slow pace allows students to think about how their programs work and what they do.

A student can simply type 
```
heart
pacman
ghost
run
```
and they have written and executed a text-based program and sequence without worrying about line numbers, capital letters or punctuation.

Despite being so simple, it lets you save smolBASIC programs to the micro:bit's non-volatile memory, so you don't lose your work (if you remember to save it!)

Read my initial blog post and watch the video here: http://www.suppertime.co.uk/blogmywiki/2021/07/simple-text-language/

## What's the instruction set?

Enter instructions and they don't run immediately as they would at a BASIC prompt or Python REPL. Instead they get stored in a program, which you then run by typing `run`

### LED display
Show images / icons just by typing their name, eg
```
heart
happy
sad
confused
meh
angry 
asleep
confused
yes
no
duck
small heart
pacman
ghost
skull
rabbit
diamond
small diamond
star
```

It's easy for students to add their own image instructions to the language.

Scroll text on the LED display with 
```
scroll hello world
```

You can clear the screen with `clear`

### Variables

You can have 26 variables. They have single letter names a - z.

Assign a variable with
```
a=23
```

You can get user input using
```
input b
```

Assign a random number between 1 and 99 to a variable with 
```
random a 99
```

### Maths operations
Maths operations can only be performed on variables and must be in the format `a=b*c`

Only +, -, / and * are supported.

### Branching and flow control

smolBASIC has a goto instruction:
```
if a>b goto 6
```

It supports <, > and = as operators.

Stop a program executing with
```
stop
```

There's no 'for' loop but you can create a loop by incrementing a variable and testing it, see the 'Loop' example below.

### Editing and running programs

Delete the current program with `new`

You can delete line 3 with `del 3`

Edit line 3 by typing the line number and what you now want it to read, eg
```
3 happy
```

Run a program with `run`

Break out of a program with ctrl-C on the host computer.

### Sound
Play note A with
```
beep A
```
At the moment no note duration can be set.

### Fast and slow modes

By default every instruction takes half a second to excecute.

You can speed things up by typing `fast` at the prompt. This removes any delay. 

You can slow them back down again with `slow`


### Saving and loading programs

Save the current program to non-volatile memory with `save`

Restore the saved program with `load`

I think smolBASIC has just enough instructions to be 'Turing complete', but I'm happy to be corrected.

## Why 'smolBASIC'?
It's smoller than TinyBASIC.

## What you need to run it
- A BBC micro:bit V2 with built-in speaker (alas, it's now not smol enough to run on a V1)
- A micro USB cable
- A computer with either USB serial terminal software or access via Chrome or Edge web browsers to either the online micro:bit Python editor https://python.microbit.org/v/2 or the new alpha editor https://python.microbit.org/v/alpha or an online serial console like https://googlechromelabs.github.io/serial-terminal/

## How to start it up
- Flash the .py or .hex file to a BBC micro:bit V2
- Open a serial console, either the REPL in one of the micro:bit Python editors or any other serial console
- Type 'help' and press enter to see a list of instructions
- Type commands and run them!

## To-do list
There's lots I could add, but I don't want to add too much - it needs to be super-simple. For example, I know my Python is shonky and inconsistent, but if it's improved it still needs to be readable by a student new to Python.

- [ ] add access to sensors
- [ ] add speech
- [ ] add a function to verify variable names and convert them to an index number
- [ ] Ability to parse expressions like a=b/17 - it may be a step too far, but I think the language needs to allow tasks like unit conversion. I have added the ability to do maths operations on variables.
- [x] More general and better exception handling - at the moment if you trigger an exception, you lose your code (unless it's saved).

## Sample programs

### Voting age
```
0 print enter your age
1 input a
2 b=17
3 if a>b goto 6
4 print you are too young to vote
5 stop
6 print you can vote
```

### Guess the number 
```
0 random a 10
1 print guess my number 1-10
2 input b
3 if a=b goto 6
4 if a>b goto 8
5 if a<b goto 10
6 print correct!
7 stop
8 print too low!
9 goto 1
10 print too high!
11 goto 1
```

### Loop
This will count to 10.
```
0 a=1
1 b=1
2 c=11
3 print a
4 a=a+b
5 if a<c goto 3
```

## Original preview video

[![preview video](https://img.youtube.com/vi/xwxMju_L0hQ/0.jpg)](http://www.youtube.com/watch?v=xwxMju_L0hQ)]
