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

## Why 'smolBASIC'?
It's smoller than TinyBASIC.

## What you need to run it
- A BBC micro:bit (it's currently still small enough to run on a V1)
- A micro USB cable
- A computer with either serial terminal software or access via Chrome or Edge web browsers to either the online micro:bit Python editor https://python.microbit.org/v/2 or the new alpha editor https://python.microbit.org/v/alpha or any serial console like https://googlechromelabs.github.io/serial-terminal/

## How to start it up
- Flash the .py or .hex file to a BBC micro:bit (V2 only now, it's too big for a V1)
- Open a serial console, either the REPL in one of the micro:bit Python editors or any other serial console
- Type 'help' and press enter to see a list of instructions
- Type commands and run them!
