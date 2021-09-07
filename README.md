# smolBASIC

(formerly known as mi:little coder)

A very simple text-based programming language for the BBC micro:bit, written in Python.

## Tell me more, tell me more
smolBASIC could be a child's first text-based programming language, but it's also simple enough students can modify it themselves, for example adding instructions to show more images or access more sensors on the micro:bit or play more sounds. It could be used in KS3 in England to satisfy the requirement to teach a text-based language, and it could be accessible to more students than other, more complex languages.

As a first text-based langauge, it aims to be as simple as possible, so it avoids punctuation like quotation marks around strings or brackets that students find hard to type.

Programs have no line numbers when entered, but lines do have numbers when listed (mainly to allow 'goto' statements to work).

Every instruction takes 1 second to execute. The slow pace allows students to think about how their programs work and what they do.

A student can simply type 
```
heart
pacman
ghost
run
```
and they have written and executed a text-based program and sequence without worrying about line numbers, capital letters or punctuation.

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

Scroll text on the LED display with 
`scroll hello world`

I think it has just enough to be 'Turing complete', but happy to be corrected.

## Why 'smolBASIC'?
It's smoller than TinyBASIC.

## What you need to run it
- A BBC micro:bit V2 with built-in speaker (alas, it's now not smol enough to run on a V1)
- A micro USB cable
- A computer with either serial terminal software or access via Chrome or Edge web browsers to either the online micro:bit Python editor https://python.microbit.org/v/2 or the new alpha editor https://python.microbit.org/v/alpha or any serial console like https://googlechromelabs.github.io/serial-terminal/

## How to start it up
- Flash the .py or .hex file to a BBC micro:bit V2
- Open a serial console, either the REPL in one of the micro:bit Python editors or any other serial console
- Type 'help' and press enter to see a list of instructions
- Type commands and run them!

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


