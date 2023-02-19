# smolBASIC

A very simple text-based programming language for the BBC micro:bit, written in MicroPython.

![smolBASIC in use](https://raw.githubusercontent.com/blogmywiki/smolBASIC/main/images/alpha-editor-screenshot-small.png)

## Tell me more, tell me more
smolBASIC can run in the simulator in the micro:bit Python Editor https://python.microbit.org/ - or on a real micro:bit connected to any serial console via USB. The serial console can be the micro:bit Python Editor in a Chrome or Edge web browser. Scroll down the page to find out about a [version with colour and simple graphics](https://github.com/blogmywiki/smolBASIC#pigfx-graphical-version).

smolBASIC could be a child's first text-based programming language, but it's also simple enough students can modify it themselves, for example adding instructions to show more images or access more sensors on the micro:bit or play more sounds. It could be used in KS3 in England to satisfy the requirement to teach a text-based language, and it could be accessible to more students than other, more complex languages.

Students could also translate the smolBASIC commands into other languages, to give younger students the opportunity to do some text-based coding in their mother tongue.

Its sheer simplicty also allows students to access some of the clarity of thought that comes with learning assembly language or machine code, but without having to learn hexadecimal, binary or memorise op codes.

As a first text-based language, it aims to be as simple as possible, so it avoids punctuation like quotation marks around strings or brackets that students find hard to type.

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
Variables can be numerical or strings of characters.

You can put user input into a variable using
```
input b
```

Assign a random number between 0 and 99 to a variable with 
```
random a 99
```

### Maths operations
Maths operations can only be performed on variables and must be in the format `a=b*c`

Only +, -, / and * operators are supported.

### Branching and flow control

smolBASIC can branch conditionally with `if` and `goto` instructions:
```
if a>b goto 6
```

It supports <, > and = as operators.

Stop a program executing with
```
stop
```

### Loops

smolBASIC has count-controlled loops. Looped sections of code start with `repeat` and end with `again` - so this example prints 'micro:bit is cool' 5 times then beeps:

```
0 repeat 5
1 print micro:bit is cool
2 again
3 beep A
```

### Sensor readings

You can assign sound, temperature and light level sensor readings to variables:

```
a=sound
b=temp
c=light
```


### Button inputs

You can read button A and button B presses using variables.

`a=button a` puts 1 in variable a if button A was pressed since the last test, otherwise 0.

`b=button b` puts 1 in variable a if button V was pressed since the last test, otherwise 0.

You can use any variable a-z, but a and b seem sensible.


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

## Why 'smolBASIC'?
It's smoller than TinyBASIC.

## Try it out in your browser

The simplest way to try out smolBASIC for yourself is to save and load `smolBASIC.py` or `smolBASIC.hex` in the micro:bit Python editor https://python.microbit.org/ and use it in the simulator. You may need to rearrange your screen slightly so you the serial console in the simulator is bigger. Press the 'play' button on the simualtor and interact with it using your computer's keyboard.

## What you need to run it on a real micro:bit

- A BBC micro:bit V2 with built-in speaker (alas, it's now not smol enough to run on a V1)
- A micro USB cable
- A computer with either USB serial terminal software or access via Chrome or Edge web browsers to either the online micro:bit Python editor https://python.microbit.org/ or an online serial console like https://googlechromelabs.github.io/serial-terminal/

### How to start it up
- Flash the `smolBASIC.py` from an editor or copy the `smolBASIC.hex` file direct to a BBC micro:bit V2 over USB.
- Open a serial console: either the REPL/serial console in one of the micro:bit Python editors or any other serial console
- Type 'help' and press enter to see a list of instructions
- Type commands and run them!

## Simulator
There's a very unstable and experimental simulator here: http://suppertime.co.uk/microbit/smolBASIC/demo.html 

It pre-loads the smolBASIC.py program into a text editor. Press play to start and type command into the black serial console. The simulator supports some very basic physical inputs: buttons, temperature, light and sound.

You can inspect and modify the source code in the text editor below the serial console, but to save your code you'd need to copy and paste it somewhere else.

## To-do list
There's lots I could add, but I don't want to add too much - it needs to be super-simple. For example, I know my Python is shonky and inconsistent, but if it's improved it still needs to be readable by a student new to Python.

- [x] add access to sensors - perhaps assign them to variables, eg `a=light` or `b=temperature`
- [x] read button state
- [x] Add loops - a `repeat... again` construct
- [ ] add speech
- [ ] add a function to verify variable names and convert them to an index number
- [ ] Ability to parse expressions like a=b/17 - it may be a step too far, but I think the language needs to allow tasks like unit conversion. I have added the ability to do maths operations on variables.
- [ ] Consider changing paradigm so stored program lines have to be entered with a line number
- [ ] Consider direct execution of instructions
- [ ] Allow non-consecutive line numbers?
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

### Loop without a loop instruction
This will count to 10.
```
0 a=1
1 b=1
2 c=11
3 print a
4 a=a+b
5 if a<c goto 3
```

### Test if button A was pressed

```
0 a=button a
1 clear
2 c=1
3 if a=c goto 6
4 print you did not press button A
5 goto 8
6 print you pressed button A
7 happy
8 beep A
```


### Emotion badge

```
0 a=button a
1 b=button b
2 z=0
3 if a=z goto 6
4 happy
5 goto 0
6 if b=z goto 0
7 sad
8 goto 0
```

## Original preview video

[![preview video](https://img.youtube.com/vi/xwxMju_L0hQ/0.jpg)](http://www.youtube.com/watch?v=xwxMju_L0hQ)]

# smolBASIC-GFX, the graphical version

![Hardware for graphical version](gfx-hardware-small.JPG)

Note that `smolBASIC-GFX-main.py` is an experimental and very buggy version that instead of using serial over USB, uses serial over pins on the micro:bit's edge connector so you can use a normal dumb terminal, such as a Raspberry Pi running PiGFX https://github.com/fbergama/pigfx 
This has added graphics and colour capabilities.


![PiGFX version](images/gfx-version-test.JPG)

### Making it

You could use an old PiZero or, as I did, an old Raspberry Pi Model B as your terminal. PiGFX boots very quickly because it's not using Linux, it runs on 'bare metal'. Note that you should use a 1GB SD card for PiGFX - I could not get it to work with larger cards with 1GB FAT partitions, possibly because I was formatting them on a Mac.

Follow the installation instructions at https://github.com/fbergama/pigfx. Configure PiGFX to run at 9600 baud. Connect a USB keyboard to the Pi and the Pi to a monitor via HDMI or composite video out (NTSC).

Connect micro:bit RX pin 1 to the Pi UART TX pin on the Pi (Pin 8 - GPIO 14).

Connect micro:bit TX pin 2 to the Pi UART RX pin on the Pi (Pin 10 - GPIO 15).

Connect micro:bit GND to any Pi GND pin and micro:bit 3v to the Pi 3v pin.

If you use any other terminal hardware with this, note that the micro:bit (and Raspberry Pi) data pins run at 3v, not 5v, so you may need a level shifter to avoid blowing up your micro:bit.

<img src="https://github.com/blogmywiki/smolBASIC/raw/main/images/smolBASIC_bb.png" width="300" />

## Ink and paper

`ink` and `paper` commands to set colours by name: red, green, blue, yellow, cyan, magenta, black and white. Ink also accepts numbers in the range 0-255 or variable names so you can create random colours.

See https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg for a colour chart.

## Clear screen

`clear screen` clears the screen and sets colours back to black and white.

## Shapes

`circle 20 30 40` draws a circle at x=20, y=30 with a radius of 40

`rectangle 100 200 30 40` draws a rectangle at x=100, y=200 of width 30 and height 40

### Sample program to draw random colour and size circles

Sorry there's no break key, so save this before running. Enter fast mode, run it - then press the reset button on the micro:bit to break out of it.

```
0 random x 600
1 random y 400
2 random r 75
3 random c 255
4 ink c
5 circle x y r
6 goto 0
```


### Sound level meter demo

This draws a bar that gets longer and changes colour the louder the sound the micro:bit picks up:

```
0 repeat 1000
1 a=sound
2 ink a
3 b=2
4 c=a*b
5 rectangle 0 100 c 50
6 again
```


### Change colour depending on light and sound

This draws a circle that changes colour depending on light levels and a rectangle that changes colour depending on sound levels.

```
0 repeat 200
1 a=light
2 ink a
3 circle 200 200 50
4 b=sound
5 ink b
6 rectangle 100 100 50 50
7 again
```

### Fix / to-do list

- [ ] Make paper take numbers and variables like ink
- [ ] Backspace needs to delete character if errors are corrected 
- [ ] Add more graphics: lines
- [x] add rectangles
- [ ] Add a break key - this may not be possible as `except KeyboardInterrupt:` doesn't work
- [ ] Replace PiGFX font with custom cool font like Chicago
- [ ] Rewrite whole parsing system to be more efficient
- [ ] Consider a version with serial over USB instead of pins - requires more hardware but could greatly simplify code (input etc); I've tried this with a USB-serial adaptor used in reverse and it didn't work.
- [x] Allow circle to take variables as parameters
- [x] strip out stray spaces at ends of commands which cause errors
- [x] Input doesn't work
- [x] Add paper and ink colours
- [x] Add graphics (circle)
