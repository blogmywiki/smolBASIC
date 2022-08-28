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

uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin2, rx=pin1)
micropython.kbd_intr(-1) # disable accidental keyboard interrupt

def help():
    uart.write('\nType image names and then \'run\' to display them\n')
    uart.write('\'scroll hello\' scrolls hello on LED display.\n')
    uart.write('\'beep A\' plays the note A\n')
    uart.write('\'stop\' stops the program\n')
    uart.write('\'input a\' prompts user input of a variable\n')
    uart.write('\'a=23\' assigns 23 to variable a\n')
    uart.write('\'random a 99\' assigns a random number between 1 and 99 to a\n')
    uart.write('\'if a>b goto 3\' jumps to line 3 if a>b\n')
    uart.write('You can also use < and = as comparisons\n')
    uart.write('\'list\' to list your program\n')
    uart.write('\'new\' to create a new program\n')
    uart.write('\'save\' stores your program in non-volatile memory\n')
    uart.write('\'load\' to load your program from non-volatile memory\n')
    uart.write('\'del 3\' deletes line 3\n')    
    uart.write('Edit line 3 by typing \'3 happy\'\n')
    uart.write('\'goto 0\' will go back to line 0 in a program\n')
    uart.write('\'help\' to view this help\n')

def parse(instruction):
    global program_counter
#    uart.write(program_counter)
    try:
        if instruction.startswith('goto '):
            split = instruction.find(' ') + 1
            line_number = int(instruction[split:])
            if line_number > -1 and line_number < len(program_list) + 1:
                program_counter = line_number - 1
            else:
                uart.write('Goto error: line doesn\'t exist.')
        elif instruction.startswith('wait '):
            split = instruction.find(' ') + 1
            wait_time = int(instruction[split:])
            sleep(wait_time)
            uart.write('sleep')
        elif instruction == 'clear':
            display.clear()
        elif instruction == 'stop':
            program_counter = len(program_list)
        elif instruction.startswith('beep '):
            music.play(instruction[5])
        elif instruction.startswith('random '):
            # random a 99 puts a random number between 1 and 99 in variable a
            var_rnd = instruction[7]
            var_index = ord(var_rnd) - 97
            rnd_range = int(instruction[9:])
            variables[var_index] = randint(1,rnd_range)
        elif instruction.startswith('if '):
            var1 = ord(instruction[3]) - 97
            operator = instruction[4]
            var2 = ord(instruction[5]) - 97
            goto = int(instruction[12:])
            if goto  < 0 or goto > len(program_list):
                uart.write('Goto error: line doesn\'t exist.')
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
                    uart.write('If error: comparsion operators must be =, < or >')
        elif instruction.startswith('scroll '):
            split = instruction.find(' ') + 1
            display.scroll(instruction[split:])
        elif instruction.startswith('input ') and len(instruction) == 7:
            var_input = instruction[6]
            var_index = ord(var_input) - 97
            if var_index >= 0 and var_index <= 26:
                input_text = input()
                try:
                    variables[var_index] = int(input_text)
                except ValueError:
                    variables[var_index] = input_text
            else:
                uart.write('Variable names must be letter a-z.')
        elif instruction.startswith('print '):
            if len(instruction) == 7 and instruction[6].isalpha():
                var_uart.write = instruction[6]
                var_index = ord(var_uart.write) - 97            
                uart.write(variables[var_index])
            else:
                split = instruction.find(' ') + 1
                uart.write(instruction[split:])
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
                try:
                    variables[ord(var_name)-97] = int(var_contents)
                except ValueError:
                    variables[ord(var_name)-97] = var_contents
        #            uart.write(var_name, '=', var_contents)
            else:
                uart.write('Variable names must be one letter a-z.')
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
    except:
        uart.write('There\'s a mistake in your program.')

sleep(500)

music.play(['c'])
uart.write('\x1B[2J')       # clear screen
uart.write('\x1B[38;5;11m') # set foreground to yellow
uart.write('\x1B[48;5;12m') # set background to blue
uart.write('BBC micro:bit computer system\n')
uart.write('\x1B[0m')       # set default colours
uart.write('7167 bytes free\n')
uart.write('smolBASIC\n')

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
    if new_line.startswith('del '):
        if ' ' in new_line:
            split = new_line.find(' ') + 1
            line_number = int(new_line[split:])
            if line_number > -1 and line_number < len(program_list):
                del program_list[line_number]
                uart.write('deleted line ' + str(line_number))
            else:
                uart.write('That line doesn\'t exist.')
        else:
            uart.write('You need to tell me which line to delete.')
    elif new_line[:1].isdigit():
        split = new_line.find(' ') + 1
        line_number = int(new_line[:split])
        if line_number >= 0 and line_number < len(program_list):
            program_list[line_number] = new_line[split:]
        else:
            uart.write('Line' + str(line_number) + ' doesn\'t exist.')
    elif new_line == 'list':
        for i in range(len(program_list)):
            uart.write(str(i)+' '+program_list[i]+'\n')
    elif new_line == 'new':
        program_list = []
    elif new_line == 'help':
        help()
    elif new_line == 'save':
        my_file = open('data', 'w')
        joined_list = ",".join(program_list)
        my_file.write(joined_list)
        my_file.close()
        uart.write('Program saved.')
    elif new_line == 'load':
        try:
            with open('data') as f:
                joined_list = f.read()
                program_list = joined_list.split(',')
#            for i in range(len(program_list)):
#                uart.write(i,program_list[i])
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
#                display.clear() <- used to clear display after showing image, now leaves it as is
    else:
        if new_line != '':
            program_list.append(new_line)


while True:
    if uart.any():
#       msg_bytes = uart.readline()
        msg_bytes = uart.read()
        msg_str = str(msg_bytes, 'UTF-8')
        if len(msg_str) > 0:
            try:
                for char in msg_str:
                    display.show(char)
                    uart.write(char)
            except:
                display.show('?')

