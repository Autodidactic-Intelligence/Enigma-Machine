import random
from tkinter import *

#Commented out print statements used for debugging purposes
#global variables, used commonly in multiple functions
tf = 25 #used as an index for arrays with 26 elements
ts = 26 #used to represent the length of the alphabet

#---------------Gui code---------------#
window = Tk()
window.title("Engima Machine 1.1")
window.configure(background = "white")
window.geometry("900x500")

#Column 0, Order of the rotors 
Rotor_1_label = Label(window, text="Rotor 1:")
Rotor_1_label.place(x=20, y=30)

Rotor_2_label = Label(window, text="Rotor 2:")
Rotor_2_label.place(x=20, y=60)

Rotor_3_label = Label(window, text="Rotor 3:")
Rotor_3_label.place(x=20, y=90)

#Column 1, rotor cicuit seeds in numeric order top to bottom
rotor_circuit_label = Label(window, text="Rotor Circuit Seeds")
rotor_circuit_label.place(x=80, y=5)

rotor_1_circuit_seed = Entry(window, bg="white")
rotor_1_circuit_seed.place(x=80, y=30)

rotor_2_circuit_seed = Entry(window, bg="white")
rotor_2_circuit_seed.place(x=80, y=60)

rotor_3_circuit_seed = Entry(window, bg="white")
rotor_3_circuit_seed.place(x=80, y=90)

#Column 2, rotor starting indexes
start_index_label = Label(window, text="Rotor Starting Index")
start_index_label.place(x=230, y=5)

rotor_1_start_index= Entry(window, bg="white")
rotor_1_start_index.place(x=230, y=30)

rotor_2_start_index = Entry(window, bg="white")
rotor_2_start_index.place(x=230, y=60)

rotor_3_start_index = Entry(window, bg="white")
rotor_3_start_index.place(x=230, y=90)

#Column 3, rotor increment amount 
increase_index_label = Label(window, text="Rotor Rotation Amount")
increase_index_label.place(x=380, y=5)

rotor_1_increase_index = Entry(window, bg="white")
rotor_1_increase_index.place(x=380, y=30)

rotor_2_increase_index = Entry(window, bg="white")
rotor_2_increase_index.place(x=380, y=60)

rotor_3_increase_index = Entry(window, bg="white")
rotor_3_increase_index.place(x=380, y=90)

#Column 4, used for message state
message_state_label = Label(window, text="Message State Info")
message_state_label.place(x=140, y=140)

ms_seed_label = Label(window, text="Message State Seed")
ms_seed_label.place(x=20, y=170)

message_state_seed = Entry(window, bg='white')
message_state_seed.place(x=140, y=170)

message_state_lower = Entry(window, bg="white")
message_state_lower.place(x=140, y=200)

ms_lower_label = Label(window, text="Lower Bound")
ms_lower_label.place(x=20, y=200)

message_state_upper = Entry(window, bg="white")
message_state_upper.place(x=140, y=230)

ms_upper_label = Label(window, text="Upper Bound")
ms_upper_label.place(x=20, y=230)

#Column 5, Alphabet randomizer
alphabet_seed_label = Label(window, text="Alphabet Randomizer Seed")
alphabet_seed_label.place(x=290, y=140)

alphabet_seed_entry = Entry(window, bg="white")
alphabet_seed_entry.place(x=290, y=170)

#Column 6, Instructions
instructions  = Label(window, justify="left", bg="white", fg="black", text="Instructions:\n Enter an Integer value for all fields.\n Enter the message you want encoded in the Input field.\n Then press Encode to encode the message.")
instructions.place(x=515, y=5)

instructions_decode = Label(window, justify="left", bg="white", fg="black", text="To decode a message:\nInsert the message to be decoded into the input field and press decode.\nTo get the same message as before all integer values\n for the fields need to be the same.")
instructions_decode.place(x=515, y=80)

instructions_message_state = Label(window, justify="left", bg="white", fg="black", text="Message State determines if a character should be encoded or not.\n The closer Upper Bound & Lower bound the more\n characters that aren't encoded.\n If Upper Bound & Lower bound are the same this feature is bypassed.")
instructions_message_state.place(x=515, y=150)

instructions_rando = Label(window, justify="left", bg="white", fg="black", text="Randomizer randomly assigns a positive two digit integer to all fields.")
instructions_rando.place(x=515, y=200)

instructions_getter = Label(window, justify="left", bg="white", fg="black", text="Get button returns all integer values in a list with each value\n delimited by a space.")
instructions_getter.place(x=515, y=220)

instructions_setter = Label(window, justify="left", bg="white", fg="black", text="To use the Set button Input a list of values\n starting & ending with an integer.\n A delimiter cannot come before or after the 1st and last value.\n Each value should have a single\n space, comma, or dash between them to act as a delimiter.")
instructions_setter.place(x=515, y=240)

#Column 7, used for collecting and giving an array of all inputs
arg_array_label = Label(window, justify="left", bg="white", fg="black", text="Array of all inputs:")
arg_array_label.place(x=20, y= 280)

arg_array_entry = Entry(window, bg="white", width=32)
arg_array_entry.place(x=125, y=280)

#Active encoding and decoding elements of the GUI
input_text = Entry(window, bg="white", width=100)
input_text.place(x=100, y= 420)

input_label = Label(window, text="Input")
input_label.place(x=40, y=420)

output_label = Label(window, text="output")
output_label.place(x=40, y=450)

output_text = Entry(window, bg="white", width=100)
output_text.place(x=100, y= 450)
#--------------End GUI code--------------#

class Rotor: #Class to create the rotors
    def __init__(self, start_index, index_amount, circuitry):
        self.start_index = start_index #where the rotor index starts
        self.index_amount = index_amount #amount to 'rotate' the rotor by
        self.current_index = start_index #pointer for the circuitry array
        self.circuitry = circuitry #the circuitry array of random integers 0 to 25
    def reset_index(self): #unused due to how I handle rotors with the GUI now, kept as it may be used in the future
        self.current_index = self.start_index #enures that get_index() will return the proper value, used before decoding 
    def increase_index(self):
        self.current_index += self.index_amount #increses the offset of the encoding and decoding
    def get_index(self):
        if self.current_index > tf:
            self.current_index = self.current_index % ts #ensures that while current_index increases it will never return an int >25 or <0
        elif self.current_index < 0:
            self.current_index = ts - (self.current_index % ts) #used for when the rotor rotates backwards, negative rotation argument, does the same as above
        return self.current_index 
    def num_at(self, index):
        return self.circuitry[index] #the array of the rotor which contains values 0 to 25 in a random order

#Returns an array of ints from 0 to 25 with each integer being unique
#Integer argument acts as a seed for the random number generator for repeatability
def circuit_generator(seed):
    circuit = []
    random.seed(a=seed)
    length = 0
    #adds an integer to the array if it is unique, otherwise it does nothing 
    while length < ts:
        x = random.randint(0,tf)
        if x in circuit: 
            x = 0
        else: 
            circuit += [x]
        length = len(circuit)
    
    return circuit

#Encodes a character from the message then returns it
#Args: message, character to be encoded; rotor_1, 2, & 3 are the rotors used for encoding
def encode(message, alphabet, rotor_1, rotor_2, rotor_3):
    char_index = 0 #index in the alphabet at which the input character is located
    i = 0 # resets i as a break is used
    #sets char_index to the proper index of the alphabet
    for i in range(ts):
        if message == alphabet[i]:
            char_index = i
            break
    #message == 'h' --> char_index = 7
    #print("message: ", message)
    #print("char_index: ", char_index)

    rotor_1_input = char_index + rotor_1.get_index() 
    #adds to get a new index for use in locating an int in rotor 1 circuitry, rotor_1_input means the input for rotor_1.num_at() 
    if rotor_1_input > tf: 
        #if this # is greater than 25 it wraps around; the maximum this number can be is 50 so it can only wrap around once
        #(25 is the max for both char_index and what .get_index() returns) 
        rotor_1_input = rotor_1_input % ts
        #performs the 'wrap around' to get a new index that is in range
    rotor_1_output = rotor_1.num_at(rotor_1_input) 
    #takes the value from rotor_1 that is at this new index and assigns it to rotor_1_output
    #7 + 3 -->  [10] --> 23

    #repeated for rotors 2 & 3
    rotor_2_input = rotor_1_output + rotor_2.get_index()
    if rotor_2_input > tf:
        rotor_2_input = rotor_2_input % ts
    rotor_2_output = rotor_2.num_at(rotor_2_input)
    #output_modifier = random.rand_int(0,24)

    rotor_3_input = rotor_2_output  + rotor_3.get_index()
    if rotor_3_input > tf:
        rotor_3_input = rotor_3_input % ts
    rotor_3_output = rotor_3.num_at(rotor_3_input)
    #output_modifier = random.rand_int(0,24)

    return alphabet[rotor_3_output]

#Decodes a character from the message then returns it
#Args: message, character to be decoded; rotor_1, 2, & 3 are the rotors used for Decoding    
def decode(message, alphabet, rotor_1, rotor_2, rotor_3):
    char_index = 0 #index in the alphabet at which the character is located
    i = 0 #resets the i in the for loop as break is used
    for i in range(ts):
        if message == alphabet[i]: #gets the index the input character is at in alphabet 
            char_index = i
            break

    i = 0 
    for i in range(ts):
        if char_index == rotor_3.num_at(i): #gets the index where char_index appears in rotor_3's circuitry array.
            rotor_3_out = i - rotor_3.get_index() 
            #takes that # and subtracts rotor_3's index from it to get the actual number that was passed to rotor_3 during encoding
            if rotor_3_out < 0: # if it's less than zero it wraps around backwards
                x = ts - rotor_3.get_index() #gets the distance from rotor_3.get_index() to the end of the array
                rotor_3_out = x + i 
                #i is the distance from the start of the array to char_index, i + x will give the total distance between where the starting index is and where char_index is
                #which is the number that was passed to this array
            break
    #print("rotor 3 out: ", rotor_3_out)

    #repeated for rotors 2 & 1
    i = 0
    for i in range(ts):
        if rotor_3_out == rotor_2.num_at(i):
            rotor_2_out = i - rotor_2.get_index()
            if rotor_2_out < 0: 
                x = ts - rotor_2.get_index()
                rotor_2_out = x + i
            break
    #print("rotor 2 out: ", rotor_2_out)

    i = 0
    for i in range(ts):
        if  rotor_2_out == rotor_1.num_at(i):
            rotor_1_out = i - rotor_1.get_index()
            if rotor_1_out < 0:
                x = ts - rotor_1.get_index()
                rotor_1_out = x + i
            break
    #print("rotor 1 out: ", rotor_1_out)
    return alphabet[rotor_1_out]

#Creates a binary array that matches the entire length of the message to determine whether a character should go through the encoding process or not
def message_state(message, alphabet):
    try: #Acquires info from the GUI
        seed = int(message_state_seed.get())
        lower_bound = int(message_state_lower.get())
        upper_bound = int(message_state_upper.get())
    except: #Prevents bad info from the GUI from crashing the program
        output_text.delete(0, END)
        output_text.insert(0, "An incorrect value has been entered, all values must be integers")

    message_bits = [] #Initializes the array
    random.seed(a=seed) #Sets the random seed
    if upper_bound == lower_bound: #If upper_bound and lower_bound are the same the entire message_bits array will be zero to bypass this feature if wanted.
        for i in range(len(message)): 
            message_bits +=[0]
    else: #Loop for if you want to use this feature of the program
        for i in range(len(message)): #Loop to iterate over the length of message
            if message[i] in alphabet: #If it's in alphabet it has the chance to either be 1 or 0, this chance can be changed by modifying the bounds.
                x = random.randint(lower_bound, upper_bound) #Roll of the dice
                if x == upper_bound: #checks to see if the 'roll' matches the upperbound, If it does 1 is pushed to message_bits, if not then 0
                    message_bits += [1]
                else:
                    message_bits += [0]
            else: #this is used to ensure message_bits has the same length as the message to prevent issues/make it easier
                message_bits +=[0]
    return message_bits

#Randomizes the order in which the letters of the alphabet appear and returns an array of characters
def alphabet_randomizer():
    new_alpha = [] #The new alphabet
    length = len(new_alpha) #length of the new alphabet 
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    try: #prevents bad GUI info from being entered, if so it will default to the standard alphabet
        seed = int(alphabet_seed_entry.get())
        random.seed(a=seed)
        if seed != 0: #creates the new alphabet with the letters in random order
            while length < ts:
                x = random.randint(0,99)
                if letters[x] in new_alpha: 
                    x = 0
                else: #if a zero is entered it will also stay the default alphabet
                    new_alpha = letters
                    break
                length = len(new_alpha)
        else:
            new_alpha = letters
    except:
        new_alpha = letters
    #print(new_alpha)
    return new_alpha

#Acquires the info needed to make the rotors from the GUI, builds the rotors, then returns all three rotors in numeric order
def rotor_builder():
    try: #Gets the info from the GUI. 
        #All info acquired from the GUI is taken in as a string
        rotor_1_cir_se = int(rotor_1_circuit_seed.get())
        rotor_2_cir_se = int(rotor_2_circuit_seed.get())
        rotor_3_cir_se = int(rotor_3_circuit_seed.get())

        rotor_1_start = int(rotor_1_start_index.get())
        rotor_2_start = int(rotor_2_start_index.get())
        rotor_3_start = int(rotor_3_start_index.get())

        rotor_1_increment = int(rotor_1_increase_index.get())
        rotor_2_increment = int(rotor_2_increase_index.get())
        rotor_3_increment = int(rotor_3_increase_index.get())

        r1_circuit = circuit_generator(rotor_1_cir_se) 
        r2_circuit = circuit_generator(rotor_2_cir_se)
        r3_circuit = circuit_generator(rotor_3_cir_se)

        rotor_1 = Rotor(rotor_1_start, rotor_1_increment, r1_circuit)
        rotor_2 = Rotor(rotor_2_start, rotor_2_increment, r2_circuit)
        rotor_3 = Rotor(rotor_3_start, rotor_3_increment, r3_circuit)

    except: #Catches errors 
        output_text.delete(0, END)
        output_text.insert(0, "An incorrect value has been entered, all values must be integers")
    
    return(rotor_1, rotor_2, rotor_3)

#Function to encode the message
def encode_loop():
    alphabet = alphabet_randomizer() #sets the alphabet to a random order
    rotor_1, rotor_2, rotor_3 = rotor_builder() #builds the rotors to be used
    message = input_text.get() #message to be encoded
    message = message.lower() #Sets the message to all lowercase to be compatible with alphabet
    message_bits = message_state(message, alphabet) #gets the message state
    #print(alphabet)
    chare = '' #encoded message placeholder
    for i in range(len(message)):
        if message[i].isspace(): #skips if it is a space
            chare += ' '
        elif message[i] not in alphabet: #If non alphabet character it simply puts that character in the encoded string
            chare += message[i]
        else: #encodes the character and increases the index of the rotors
            if message_bits[i] == 0: #only encodes if the characters bit is equal to 0
                chare += encode(message[i], alphabet, rotor_1, rotor_2, rotor_3) 
                rotor_1.increase_index()
                rotor_2.increase_index()
                rotor_3.increase_index()
            else:
                chare += message[i] #puts the unencoded character into the encoded string
        
    output_text.delete(0, END) #removes what's in the needed text field
    output_text.insert(0, chare) #outputs the encoded message

#Function to decode the message, logic is the same as encode_loop as decoding may be done 1st
def decode_loop():
    alphabet = alphabet_randomizer()
    rotor_1, rotor_2, rotor_3 = rotor_builder() #builds the rotor, necessary as the program may be used to decode first
    chare = input_text.get() #message to be decoded
    chare = chare.lower()
    message_bits = message_state(chare, alphabet)
    #print(alphabet) 
    chard = "" #decoded message 
    i = 0
    #loop to decode the message
    for i in range(len(chare)):
        if chare[i].isspace():
            chard += ' '
        elif chare[i] not in alphabet:
            chard += chare[i]
        else:
            if message_bits[i] == 0:
                chard += decode(chare[i], alphabet, rotor_1, rotor_2, rotor_3)
                rotor_1.increase_index()
                rotor_2.increase_index()
                rotor_3.increase_index()
            else:
                chard += chare[i]

    output_text.delete(0, END)
    output_text.insert(0, chard)

#Clears text in the input & output entry fields in the GUI
def clear_text():
    output_text.delete(0, END)
    input_text.delete(0, END)

#An array of all fields in the GUI that take Integer arguements, needed for the functions randomizer, arg_array_getter, & arg_array_setter
field_arr = [rotor_1_circuit_seed, rotor_2_circuit_seed, rotor_3_circuit_seed, rotor_1_start_index, rotor_2_start_index, rotor_3_start_index,
                 rotor_1_increase_index, rotor_2_increase_index, rotor_3_increase_index, message_state_seed, message_state_lower, message_state_upper,
                 alphabet_seed_entry]
field_arr_len = len(field_arr) #the number of fields that take an integer arguement


#Creates a random array then assigns those contents to the various integer input fields
def randomizer():
    lower = 0
    for i in range(field_arr_len):
        field_arr[i].delete(0, END) #Clears out any previous values
        rando = random.randint(0,50) #gets a random int
        
        # some logic to ensure upper bound is always higher or equal to the lower bound
        if i == (field_arr_len-2):
            if lower > rando:
                field_arr[i-1].delete(0, END)
                field_arr[i-1].insert(0, rando)
                rando = lower

        field_arr[i].insert(0, rando) #assigns it to the respective entry field in the array
        lower = rando

#Allows user to collect an array of all integer inputs used
def arg_array_getter():
    int_arg_array = [] #array to store all the integer arguements
    i = 0 #resets i in case a break is used 
    for i in range(field_arr_len):
        try:
            int_arg_array += [int(field_arr[i].get())] #gets what's in the integer fields and adds them to this array, has to be cast to int as it's taken in as a string
        except:
            output_text.delete(0, END)
            output_text.insert(0, "Error: A field has an incorrect value, all values should be integers.")
            break
    arg_array_entry.delete(0, END)
    arg_array_entry.insert(0, int_arg_array)

#Takes an inputted set of integers and assigns those values to all integer fields
def arg_array_setter():
    str_arg_array = arg_array_entry.get() #Array of inputted values
    int_str = '0123456789' #String to compare the inputted value to
    input_str = '' #input string for the field, it can be a string as it's taken in as a string anyway
    iterate = 0 #used to index what field the value goes to in field_arr
    try:
        for i in range(len(str_arg_array)):
            if str_arg_array[i] in int_str: #if the current index is in int_str it adds it to input_str
                input_str += str_arg_array[i] 
            else: #when it hits a value not in int_str it will take what value it has and assign it to the proper field.
                field_arr[iterate].delete(0, END) #removes what is currently in the field 
                field_arr[iterate].insert(0, input_str) #sets the field to the value that is created, it is delimited by anything not in int_str
                iterate += 1 #Increments to the next field
                input_str = '' #resets the input string
        #    print(i)     
        #print(len(str_arg_array))
        #Outside of the for loop to finish for the final field
        field_arr[iterate].delete(0, END) #removes what is currently in the field 
        field_arr[iterate].insert(0, input_str) #sets the field to the value that is created, it is delimited by anything not in int_str
    except:
        output_text.delete(0, END)
        output_text.insert(0, "A value has two delimiters placed between it and the previous value. Fix to continue")
        

#Buttons have to come after functions to avoid conflicts
encode_button = Button(window, text="Encode", command=encode_loop)
encode_button.place(x=150, y=370)

decode_button = Button(window, text="Decode", command=decode_loop)
decode_button.place(x=240, y=370)

clear_button = Button(window, text="Clear Input & Output", command=clear_text)
clear_button.place(x=330, y=370)

randomizer_button = Button(window, text="Random Assigner", command=randomizer)
randomizer_button.place(x=290, y=200)

get_int_args = Button(window, text="Get", command=arg_array_getter)
get_int_args.place(x=340, y=280)

set_int_args = Button(window, text="Set", command=arg_array_setter)
set_int_args.place(x=380, y= 280)

window.mainloop() #runs the GUI
   





    
        




    


    
