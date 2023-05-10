import time # this is optional - time library is there so we can check how fast is our code later

# we declare the important variables we get from the input
width = 0 # width of the grid
height = 0 # height of the grid
num_commands = 0 # number of commands
commands = [] # container to store the commands
canvas = [] # the final 2D grid were we are drawing the result of the commands



def get_data():
    # this function gets the data from the input
    global width
    global height
    global commands
    global num_commands
    global canvas

    width, height, num_commands = input().split()
    # .split() separates the string at " " and saves values to separate variables
    # example of split  "a b c" ---> "a", "b", "c"
    width = int(width) # we convert the values into integers
    height = int(height)
    num_commands = int(num_commands)
    # print(width, height, num_commands)

    # we fill in the 2D canvas matrix with dots as dots are considered background in our picture
    # so it is a 2D matrix (height x width) having a "." in each cell
    canvas = [["."] * width for i in range(height)]

    # now we save the commands into a container (it will be a list of lists)
    for row in range(num_commands):
        row = input().strip() #.strip() is there just to delete the last " " at the end of line
        row = row.split() # split() separates the values so we get instead of "P 8 2 15 A" ---> ["P", "8", "2", "15", "A"]
        # print(new_row)
        commands.append(row) # we append the commands in the form ["P", "8", "2", "15", "A"] to a list
        # So commands has the form of:
        # [ ["P", "8", "2", "15", "A"], ["C", "8", "2", "15", "A"], ["R", "8", "2", "15", "A"] ]


def read_command():
    # This is the function which is going to go through the list of the commands
    # and performs the actions which are there in the commands
    global commands
    global canvas

    # we go from index 0 of items in the commands list to the last one
    # and process one command at a time
    for i in range(num_commands):

        # each command has the following example format:
            # pyramid  ["P", "8", "2", "15", "A"]
            # rectangle ["R", "1", "13", "2", "18", "B"]
            # clear ["C", "7", "6", "10", "10"]
            # substitute ["S", "3", "9", "7", "16", "A", "I"]

        # if the 0th element of the current command is "P" it´s "pyramid"
        if commands[i][0] == "P":
            # print(i, "This is pyramid command")
            # example: ["P", "8", "2", "15", "A"]
            # we transform coordinates into integers
            y1 = int(commands[i][1])
            x1 = int(commands[i][2])
            x2 = int(commands[i][3])
            char = commands[i][4]

            # we call the function which draws the pattern into canvas matrix
            pyramid(y1, x1, x2, char)

        # if the 0th element of the current command is "R" it´s "rectangle"
        elif commands[i][0] == "R":
            # print(i, "This is a rectangle command")
            # example ["R", "1", "13", "2", "18", "B"]

            # we transform coordinates into integers
            y1 = int(commands[i][1])
            x1 = int(commands[i][2])
            y2 = int(commands[i][3])
            x2 = int(commands[i][4])
            char = commands[i][5]

            # if our coordinate is outside the size of canvas we will get error
            # so we use only those coordinates which are inside our range for canvas
            # if x2 coordinate is bigger than number of columns in canvas
            # we set it to the last column in canvas
            if x2 > width-1:
                x2 = width-1

            # if y2 coordinate is bigger than number of rows in canvas
            # we set it to the last row in canvas
            if y2 > height-1:
                y2 = height-1

            # we call the function which draws the pattern into canvas matrix
            rectangle(y1, x1, y2, x2, char)


        # if the 0th element of the current command is "C" it´s "clear"
        elif commands[i][0] == "C":
            # print(i, "This is a clear command")
            # example: ["C", "7", "6", "10", "10"]

            # we transform coordinates into integers
            y1 = int(commands[i][1])
            x1 = int(commands[i][2])
            y2 = int(commands[i][3])
            x2 = int(commands[i][4])

            # if our coordinate is outside the size of canvas we will get error
            # so we use only those coordinates which are inside our range for canvas

            # if x2 coordinate is bigger than number of columns in canvas
            # we set it to the last column in canvas
            if x2 > width - 1:
                x2 = width - 1

            # if y2 coordinate is bigger than number of rows in canvas
            # we set it to the last row in canvas
            if y2 > height - 1:
                y2 = height - 1

            # we call the function which draws the pattern into canvas matrix
            clear(y1, x1, y2, x2)

        # if the 0th element of the current command is "S" it´s "substitute"
        elif commands[i][0] == "S":
            # print(i, "This is a substitute command")
            # example: ["S", "3", "9", "7", "16", "A", "I"]

            # we transform coordinates into integers
            y1 = int(commands[i][1])
            x1 = int(commands[i][2])
            y2 = int(commands[i][3])
            x2 = int(commands[i][4])
            char1 = commands[i][5]
            char2 = commands[i][6]

            # if our coordinate is outside the size of canvas we will get error
            # so we use only those coordinates which are inside our range for canvas
            # We Don´t do same on pyramid function because we actually DO draw things even if the coordinates are outside canvas

            # you can print the "old values" which are not in the range (in case it happens)
            # print("Old values", y1, x1, y2, x2)

            # if x2 coordinate is bigger than number of columns in canvas
            # we set it to the last column in canvas
            if x2 > width-1:
                x2 = width-1

            # if y2 coordinate is bigger than number of rows in canvas
            # we set it to the last row in canvas
            if y2 > height-1:
                y2 = height-1

            # we can see the "new values" in case they needed to be adjusted to the range of the canvas size
            # print("New values", y1,x1,y2,x2)
            # same can be done for rectangle and clear commands, you can print the old and new coordinates to see how they change

            # we call the function which draws the pattern into canvas matrix
            substitute(y1, x1, y2, x2, char1, char2)


# Here we have the group of functions which takes the coordinates and draws the given pattern to canvas

def rectangle(y1, x1, y2, x2, char): # functions has 4 coordinates and the character as input
    global canvas
    # we go through rows, columns of 2D matrix and in the range determined by the coordinates it changes "." to a char given
    for i in range(y1, y2 + 1): #
        for j in range(x1, x2 + 1):
            canvas[i][j] = char



def clear(y1, x1, y2, x2): # same principle as rectangle
    global canvas
    # we go through rows, columns of 2D matrix and in the range determined by the coordinates it changes char that is there back to a  "."
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            canvas[i][j] = "."



def substitute(y1, x1, y2, x2, char1, char2): # same principle as rectangle but with additional if-condition
    global canvas
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if canvas[i][j] == char1: # it changes ONLY the char1 to char2, it does not change other characters or "." to char2
                canvas[i][j] = char2



def pyramid(y1, x1, x2, char):
    # pyramid function has as input the following variables:
    # y1 - is the row where the pyramid is SUPPOSED to start, not necessarily inside the canvas
    # x1 ... x2 the length of pyramid base - it goes from column x1 to column x2
    global canvas
    global height
    global width

    # for the pyramid we have two cases:
    # 1) when the base has odd number of cells in the base -> one cell on top
    # 2) when the base has even number of cells in the base -> two cells on top

    # This is the part when we have odd base length (one cell on top)
    if (x2-x1) % 2 == 1:
        s1, s2, t = x1, x2, y1 # we assign our coordinates to other variables that we are going to change
        while s2-s1 > 0: # meanwhile the row length in the pyramid is bigger than zero (until the we get to the top of the pyramid)
            for i in range(s1, s2+1):  # in range of s1 (left column coordinate) to s2 (right column coordinate)
                if height - 1 >= t >= 0: # whatever part of the pyramid vertically is in the range of canvas size
                    if width - 1 >= i >= 0: # whatever part of the pyramid horizontally is in the range of canvas size
                        canvas[t][i] = char # we print it in the canvas
            s1 = s1+1 # we move the left column coordinate one cell to the right
            s2 = s2-1 # we move the right column coordinate one cell to the left
            t = t-1  # we move the row coordinate one cell up

    # This is the part when we have even base length (two cells on top)
    elif (x2-x1) % 2 != 1:
        s1, s2, t = x1, x2, y1
        while s2 - s1 >= 0:  # everything is same as above but the exit condition for while loop (until we get to row length is equal to zero is possible)
            for i in range(s1, s2 + 1):
                if height - 1 >= t >= 0:
                    if width - 1 >= i >= 0:
                        canvas[t][i] = char
            s1 = s1 + 1
            s2 = s2 - 1
            t = t - 1


# +++++++++++++++++ MAIN part for calling functions  +++++++++++++++++

# we call the function to get the data from the input
get_data()

# we call the function to read the commands and draw patterns
read_command()

# the last line prints the canvas matrix nicely
print(*(''.join(row) for row in canvas), sep='\n')

