"""
Final Project
-------------

Author: Dor Rondel
Course: CSc 11300
File: main.py
"""

#####################
###### Imports ######
#####################


from tkinter import *
from turtle import *

# NOTE: letter_frequency.py should be in the same folder you're running main.py from
from letter_frequency import *


#####################
###### Tkinter ######
#####################


def get_input_close_window(window, entry, array):
    ''' Closes Tkinter window and get's user input '''
    array.append(entry.get())
    if (int(array[-1]) in range(1, 27)):  # to ensure user input is valid
        window.destroy()

user_input = []  # will be used later to store user input

window = Tk()
frame = Frame(window)
frame.pack()

bottomframe = Frame(window)
bottomframe.pack(side = BOTTOM)  # to put button beneath text and entry box

instructions = Label(window, text = "Enter the amount of letters whose frequency you want to find out (1-26): ")
instructions.pack(side = LEFT)
entry_box = Entry(window, bd = 4)
entry_box.pack(side = RIGHT)

button = Button(bottomframe, text = "Submit", command = lambda: get_input_close_window(window, entry_box, user_input))
button.pack(side = BOTTOM)
window.mainloop()


#####################
### File Analysis ###
#####################

# NOTE: Words.txt should be in the same folder you're running main.py from
usr_file = open('Words.txt', 'r')
file_content = usr_file.read().upper()  # since letter case doesnt matter we wont have to treat e and E differently
usr_file.close()


#####################
## Letter Analysis ##
#####################


letter_probability_list = letter_probability(file_content)
upper_bound = int(user_input[-1])
sorted_array = sorted(letter_probability_list)[::-1]  # sort from greatest to least

used_letters = get_used()

n_letters = []
for i in range(upper_bound):
    n_letters.append(
        [used_letters[letter_probability_list.index(sorted_array[i])],
        sorted_array[i]]
    )
    used_letters = used_letters.replace(used_letters[letter_probability_list.index(sorted_array[i])], "")  # remove letter
    letter_probability_list.remove(sorted_array[i])  # remove letter probability

#####################
##### Pie Chart #####
#####################


rad = 250
colors = (  # 26 colors to match n upper bound and have unique color per arc
    "black",
    "orange",
    "pink",
    "purple",
    "palegreen",
    "brown",
    "white",
    "green",
    "blue",
    "cyan",
    "orchid",
    "salmon",
    "sienna",
    "snow",
    "violet",
    "wheat",
    "tan",
    "tomato",
    "turquoise",
    "yellow",
    "azure",
    "red",
    "plum",
    "peru",
    "navy",
    "moccasin"
)

def end():
    ''' Keep Code DRYer by storing three function calls together '''
    end_fill()
    pu()
    home()

# make screen size large so no text leaves screen
window = Screen()
window.screensize(1200, 1200)
window.setup(width=1.0, height=1.0, startx=None, starty=None)

# center circle
pu()
forward(rad)
pd()
left(90)

# fill circle
color('grey')
begin_fill()
circle(rad)
end()

# prepare to cut circle
color('black')
pd()
forward(rad)
pu()
home()


def separate_circle():
    ''' make seperate segments for circle based on appropriate size '''
    degrees_rotated = 0
    for num in range(len(n_letters)):
        arc = n_letters[num][1] * 360  # percentage of 360 degrees to give arc in degrees
        degrees_rotated += arc
        seth(degrees_rotated)
        color(colors[num])
        begin_fill()
        pd()
        forward(rad)
        end()

def make_legend():
    ''' makes legends for circle arcs '''
    degrees_rotated = 0
    for num in range(len(n_letters)):
        tmp = degrees_rotated
        half_arc = (n_letters[num][1] * 360) / 2  # half way through segment to give legend
        degrees_rotated += half_arc
        seth(degrees_rotated + tmp)
        color(colors[num])
        begin_fill()
        pd()
        forward(rad)
        end_fill()
        color("white")
        begin_fill()
        forward(40)
        end_fill()
        color("black")
        begin_fill()
        # Can't see space, tab, and newline so write them out
        if (n_letters[num][0] == " "):
            write("space" + " : " + str(round(n_letters[num][1],4)), font=("Arial", 11, "normal"))
        elif (n_letters[num][0] == "\n"):
            write("new-line" + " : " + str(round(n_letters[num][1],4)), font=("Arial", 11, "normal"))
        elif (n_letters[num][0] == "\t"):
            write("tab" + " : " + str(round(n_letters[num][1],4)), font=("Arial", 11, "normal"))
        else:  # any other VISIBLE characters
            write(n_letters[num][0] + " : " + str(round(n_letters[num][1],4)), font=("Arial", 11, "normal"))
        end()


def fill_circle():
    ''' Fills circle arcs '''
    degree = 0
    degrees_rotated = 0
    pensize(6)
    for num in range(len(n_letters)):
        degrees_rotated += n_letters[num][1] * 360
        while (degree <= degrees_rotated):
            seth(degree)
            color(colors[num])
            begin_fill()
            pd()
            forward(rad)
            end()
            degree += 1

        if (num == len(n_letters) - 1):
            pensize(2)
            total_degrees = sum([idx[1] * 360 for idx in n_letters])
            total_percentages = sum([idx[1] for idx in n_letters])
            seth(degree+15)  # whatever degrees are left is the other section with small offset
            color("grey")
            begin_fill()
            pd()
            forward(rad)
            end_fill()
            color("white")
            begin_fill()
            forward(35)
            end_fill()
            color("black")
            begin_fill()
            write("All other characters: " + str(round(1 - total_percentages, 4)), font=("Arial", 11, "normal"))
            end()


if __name__ == "__main__":
    separate_circle()
    fill_circle()
    make_legend()
    mainloop()  # tkinter method to keep turtle window open after completion
