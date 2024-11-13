# Ian Bullard
# UWYO COSC 1010
# 11/11/24
# HW 01
# Lab Section: 14
# Sources, people worked with, help given to:



#  You will be reading from and writing to a file.
# You will read from prompt.txt
# You will write to a file called "out.txt".

# Look at prompt.txt to understand its structure.

# It contains key-value pairs on each line of the file.
# The keys are 'w' and '*'.
# 'w' stands for white space, and '*' is an asterisk (*).
# The numeric value shows how many of each of those characters there are for each line in your output file.
# Each line in prompt.txt corresponds to one line in out.txt.

# For example, the line:
# "w:101    *:020    w:026    *:004    w:017    *:030"
# You will output a line with 101 white spaces, 20 asterisks, 26 white spaces, 4 asterisks, 17 white spaces, and 30 asterisks.
# All of that will be on ONE line of your output file.

# Each of the key-value pairs is separated by a tab '\t' character.
# The key values are separated by a ':' character.

# You can use the .split() function on strings to create a list. For example, pairs = line.split("\t") will give you a list of all the pairs in a line.

# You can multiply strings by an integer, x, to create a string repeated x times. So, string_val = "*" * 10 would create a string with 10 asterisks: "**********".

# You will be outputting a VERY recognizable ASCII art with this. If you are looking at the output file and you aren't sure what it is, you are likely doing it incorrectly. It can help if you zoom out on your output file.


from pathlib import Path
path = Path('prompt.txt')
contents = path.read_text()
lines = contents.splitlines()
out = ""
#print(lines)
key_value_dict = {}
for line in lines:
    #print(line)
    pairings = line.split("\t")
    

    #print(pairings)

    for pair in pairings:
        #print(pair)
        key, sep, value = pair.partition(":")
        
        if sep == ":" and value:
            value = int(value.strip())
            key_value_dict[key.strip()] = value
        #print(key)
        #print(value)
            

        if key.strip() == "w":
            out = " " * value + out
            #print(f' Adding {value} spaces')
        elif key.strip() == "*":
            out = "*" * value + out
            #print(f' Adding {value} astericks')
#print(len(out))
output_path = Path('output.txt')
output_path.write_text(out)