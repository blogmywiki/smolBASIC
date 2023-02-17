# experimental version using serial on pins 1 & 2 rather than USB

from microbit import *
import micropython
import music
from random import *
program_list = []
global program_counter
program_counter = -1
variables = [None]*26
operators = '+-/*'
delay = 500
global repeat_count
repeat_count = 0
global return_address 
return_address = 0
colours = {'white':'15', 'black':'0', 'red':'9', 'yellow':'11', 'green':'10', 'blue':'12', 'magenta':'13', 'cyan':'14'}

uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin2, rx=pin1)
micropython.kbd_intr(-1) # disable accidental keyboard interrupt

def help():
    print('Type image names and then \'run\' to display them')
    print('\'scroll hello\' scrolls hello on LED display')
    print('\'beep A\' plays the note A')
    print('\'stop\' stops the program')
    print('\'input a\' prompts user input of a variable')
    print('\'a=23\' assigns 23 to variable a')
    print('\'random a 99\' assigns a random number between 1 and 99 to a')
    print('\'if a>b goto 3\' jumps to line 3 if a>b')
    print('You can also use < and = as comparisons')
    print('\'list\' to list your program')
    print('\'new\' to create a new program')
    print('\'save\' stores your program in non-volatile memory')
    print('\'load\' to load your program from non-volatile memory')
    print('\'del 3\' deletes line 3')    
    print('Edit line 3 by typing \'3 happy\'')
    print('\'goto 0\' will go back to line 0 in a program')
    print('\'help\' to view this help')

def parse(instruction):
    global program_counter
    global repeat_count
    global return_address
    try:
        if instruction.startswith('goto '):
            split = instruction.find(' ') + 1
            line_number = int(instruction[split:])
            if line_number > -1 and line_number < len(program_list) + 1:
                program_counter = line_number - 1
            else:
                print('Error: goto line doesn\'t exist.')
        elif instruction.startswith('wait '):
            split = instruction.find(' ') + 1
            wait_time = int(instruction[split:])
            sleep(wait_time)
            print('sleep')
        elif instruction.startswith('repeat '):
            split = instruction.find(' ') + 1
            repeat_count = int(instruction[split:])
            return_address = program_counter
        elif instruction == 'again':
            repeat_count -= 1
            if repeat_count != 0:
                program_counter = return_address
        elif instruction == 'clear':
            display.clear()
        elif instruction == 'clear screen':
            uart.write('\x1B[2J')
        elif instruction == 'stop':
            program_counter = len(program_list)
        elif instruction.startswith('beep '):
            music.play(instruction[5])
        elif instruction.startswith('random '):
            # random a 99 puts a random number between 0 and 99 in variable a
            var_rnd = instruction[7]
            var_index = ord(var_rnd) - 97
            rnd_range = int(instruction[9:])
            variables[var_index] = randint(0,rnd_range)
        elif instruction.startswith('if '):
            var1 = ord(instruction[3]) - 97
            operator = instruction[4]
            var2 = ord(instruction[5]) - 97
            goto = int(instruction[12:])
            if goto  < 0 or goto > len(program_list):
                print('Error: goto line doesn\'t exist.')
            else:
                if operator == '=':
                    if variables[var1] == variables[var2]:
                        program_counter = goto - 1
                elif operator == '>':
                    if variables[var1] > variables[var2]:
                        program_counter = goto - 1
                elif operator == '<':
                    if variables[var1] < variables[var2]:
                        program_counter = goto - 1
                else:
                    print('Error: if statement comparsion operators must be =, < or >')
        elif instruction.startswith('scroll '):
            split = instruction.find(' ') + 1
            display.scroll(instruction[split:])
        elif instruction.startswith('input ') and len(instruction) == 7:
            var_input = instruction[6]
            var_index = ord(var_input) - 97
            if var_index >= 0 and var_index <= 26:
                input_text = ''
                new_char_string = ''
                while new_char_string != '\n':
                    new_char_byte =  uart.readline()
                    if new_char_byte:
                        new_char_string = str(new_char_byte, 'UTF-8')
                        input_text = input_text + new_char_string
                        uart.write(new_char_byte)
                input_text = input_text[:-1]
                try:
                    variables[var_index] = int(input_text)
                except ValueError:
                    variables[var_index] = input_text
            else:
                print('Variable names must be letter a-z.')
        elif instruction.startswith('print '):
            if len(instruction) == 7 and instruction[6].isalpha():
                var_print = instruction[6]
                var_index = ord(var_print) - 97            
                print(variables[var_index])
            else:
                split = instruction.find(' ') + 1
                print(instruction[split:])
        elif instruction.startswith('ink '):
            split = instruction.find(' ') + 1
            if instruction[split:].isalpha():
                if len(instruction[split:]) > 1:
                    uart.write('\x1B[38;5;' + colours[instruction[split:]] + 'm')
                else:
                    uart.write('\x1B[38;5;' + str(variables[ord(instruction[split:])-97]) + 'm')
            else:
                uart.write('\x1B[38;5;' + instruction[split:] + 'm')
        elif instruction.startswith('paper '):
            split = instruction.find(' ') + 1
            uart.write('\x1B[48;5;' + colours[instruction[split:]] + 'm')
        elif instruction.startswith('circle '):
            split = instruction.find(' ') + 1
            xyr = instruction[split:]
            split = xyr.find(' ') + 1
            x = xyr[:split].strip(' ')
            yr = xyr[split:]
            split = yr.find(' ') + 1
            y = yr[:split].strip(' ')
            r = yr[split:]
            if x.isalpha():
                x = str(variables[ord(x)-97])
            if y.isalpha():
                y = str(variables[ord(y)-97])
            if r.isalpha():
                r = str(variables[ord(r)-97])
            uart.write('\x1B[#'+x+';'+y+';'+r+'c')
        elif instruction.startswith('rectangle '):
            split = instruction.find(' ') + 1
            xywh = instruction[split:]
            split = xywh.find(' ') + 1
            x = xywh[:split].strip(' ')
            ywh = xywh[split:]
            split = ywh.find(' ') + 1
            y = ywh[:split].strip(' ')
            wh = ywh[split:]
            split = wh.find(' ') + 1
            w = wh[:split].strip(' ')
            h = wh[split:]
            if x.isalpha():
                x = str(variables[ord(x)-97])
            if y.isalpha():
                y = str(variables[ord(y)-97])
            if w.isalpha():
                w = str(variables[ord(w)-97])
            if h.isalpha():
                h = str(variables[ord(h)-97])
            uart.write('\x1B[#'+x+';'+y+';'+w+';'+h+'r')
        elif len(instruction) == 5 and instruction[3] in operators and instruction[1] == '=' and ord(instruction[0]) > 96 and ord(instruction[0]) < 123 and ord(instruction[2]) > 96 and ord(instruction[2]) < 123 and ord(instruction[4]) > 96 and ord(instruction[4]) < 123:
            var1 = instruction[0]
            var2 = instruction[2]
            var3 = instruction[4]
            operator = instruction[3]
            if operator == '+':
                variables[ord(var1)-97] = variables[ord(var2)-97] + variables[ord(var3)-97]
            elif operator == '-':
                variables[ord(var1)-97] = variables[ord(var2)-97] - variables[ord(var3)-97]
            if operator == '/':
                variables[ord(var1)-97] = variables[ord(var2)-97] / variables[ord(var3)-97]
            if operator == '*':
                variables[ord(var1)-97] = variables[ord(var2)-97] * variables[ord(var3)-97]            
        elif '=' in instruction:
            split = instruction.find('=') + 1
            var_name = instruction[:split-1]
            var_contents = instruction[split:]
            if len(var_name) == 1 and var_name.isalpha():
                if var_contents == 'light':
                    variables[ord(var_name)-97] = display.read_light_level()
                elif var_contents == 'temp':
                    variables[ord(var_name)-97] = temperature()
                elif var_contents == 'sound':
                    variables[ord(var_name)-97] = microphone.sound_level()
                elif var_contents == 'button a':
                    if button_a.was_pressed():
                        variables[ord(var_name)-97] = 1
                    else:
                        variables[ord(var_name)-97] = 0
                elif var_contents == 'button b':
                    if button_b.was_pressed():
                        variables[ord(var_name)-97] = 1
                    else:
                        variables[ord(var_name)-97] = 0
                else:
                    try:
                        variables[ord(var_name)-97] = int(var_contents)
                    except ValueError:
                        variables[ord(var_name)-97] = var_contents
            else:
                print('Variable names must be one letter a-z.')
        elif instruction == 'heart':
            display.show(Image.HEART)
        elif instruction == 'happy':
            display.show(Image.HAPPY)
        elif instruction == 'sad':
            display.show(Image.SAD)
        elif instruction == 'meh':
            display.show(Image.MEH)
        elif instruction == 'confused':
            display.show(Image.CONFUSED)
        elif instruction == 'angry':
            display.show(Image.ANGRY)
        elif instruction == 'asleep':
            display.show(Image.ASLEEP)
        elif instruction == 'yes':
            display.show(Image.YES)
        elif instruction == 'no':
            display.show(Image.NO)
        elif instruction == 'duck':
            display.show(Image.DUCK)
        elif instruction == 'small heart':
            display.show(Image.HEART_SMALL)
        elif instruction == 'pacman':
            display.show(Image.PACMAN)
        elif instruction == 'ghost':
            display.show(Image.GHOST)
        elif instruction == 'skull':
            display.show(Image.SKULL)
        elif instruction == 'rabbit':
            display.show(Image.RABBIT)
        elif instruction == 'diamond':
            display.show(Image.DIAMOND)
        elif instruction == 'small diamond':
            display.show(Image.DIAMOND_SMALL)
        elif instruction == 'star':
            display.show(Image('00300:'
                               '03630:'
                               '36963:'
                               '03630:'
                               '00300'))
        else:
            display.show('?')
    except Exception as e: print(e)
#    except:
#        uart.write('There\'s a mistake in your program.')

sleep(500)

# use print for text etc as it adds a newline. Use uart.write for sending control codes
music.play(['c'])
uart.write('\x1B[2J')       # clear screen
# draw micro:bit logo
uart.write('\x1B[#3;11;7;10A0;2;15;7;0;3;15;1;0;7;15;1;0;2;15;1;0;7;15;1;0;1;15;1;0;2;15;1;0;3;15;1;0;2;15;1;0;1;15;1;0;7;15;1;0;2;15;1;0;7;15;1;0;3;15;7;0;2;')
uart.write('\x1B[#3;240;5d')  
uart.write('\x1B[38;5;11m') # set foreground to yellow
uart.write('\x1B[48;5;12m') # set background to blue
print('BBC micro:bit computer system')
uart.write('\x1B[0m')       # set default colours
print('smolBASIC')

while True:
    uart.write('\n>')
    new_line = ''
    new_char_string = ''
    while new_char_string != '\n':
        new_char_byte =  uart.readline()
        if new_char_byte:
            new_char_string = str(new_char_byte, 'UTF-8')
            new_line = new_line + new_char_string
            uart.write(new_char_byte)
    new_line = new_line[:-1]
    new_line = new_line.rstrip()
    if new_line.startswith('del '):
        if ' ' in new_line:
            split = new_line.find(' ') + 1
            line_number = int(new_line[split:])
            if line_number > -1 and line_number < len(program_list):
                del program_list[line_number]
                print('deleted line',line_number)
            else:
                print('That line doesn\'t exist.')
        else:
            print('You need to tell me which line to delete.')
    elif new_line[:1].isdigit():
        split = new_line.find(' ') + 1
        line_number = int(new_line[:split])
        if line_number >= 0 and line_number < len(program_list):
            program_list[line_number] = new_line[split:]
        else:
            print('Line',line_number,'doesn\'t exist.')
    elif new_line == 'list':
        for i in range(len(program_list)):
            print(i,program_list[i])
    elif new_line == 'new':
        program_list = []
    elif new_line == 'help':
        help()
    elif new_line == 'save':
        my_file = open('data', 'w')
        joined_list = ",".join(program_list)
        my_file.write(joined_list)
        my_file.close()
        print('Program saved.')
    elif new_line == 'load':
        try:
            with open('data') as f:
                joined_list = f.read()
                program_list = joined_list.split(',')
        except:
            uart.write('No file to load.')
    elif new_line == 'fast':
        delay = 0
    elif new_line == 'slow':
        delay = 500
    elif new_line == 'run':
        program_counter = -1
        while program_counter < len(program_list):
            program_counter += 1
            if program_counter == len(program_list):
                break
            else:
                parse(program_list[program_counter])
                sleep(delay)
    else:
        if new_line != '':
            program_list.append(new_line)



