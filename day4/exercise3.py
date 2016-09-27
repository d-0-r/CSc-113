__author__ = "Dor Rondel"
__session__ = "9:30am"

#A

def did_pass(score):
    print("Did pass?  ", end="")
    return True if score >= 50 else False

user_score = int(input("What was your score for the exam?   "))

# print(did_pass(user_score))
# Entered 5 got False

#B
def abs_zero(scale):
    scale = scale.upper()
    if scale == 'K':
        print("0 K")
    elif scale == 'C':
        print("-273.15 C")
    elif scale == 'F':
        print("-459.67 F")
    else:  # Assume K
        print("0 R")

#abs_zero('F')
#Entered F got -459.67 F

#C
def avg_score_letter():
    one = int(input("Enter your first score"))
    two = int(input("Enter your second score"))
    avg = round((one+two)/2.0)  # round up avg to whole number
    if avg >= 97 and avg <= 100:
        return "A+"
    elif avg >= 93 and avg <= 96:
        return "A"
    elif avg >= 90 and avg <= 92:
        return "A-"
    elif avg >= 87 and avg <= 89:
        return "B+"
    elif avg >= 83 and avg <= 86:
        return 'B'
    elif avg >= 80 and avg <= 82:
        return 'B-'
    elif avg >= 77 and avg <= 79:
        return 'C+'
    elif avg >= 73 and avg <= 76:
        return 'C'
    elif avg >= 70 and avg <= 72:
        return 'C-'
    elif avg >= 67 and avg <= 69:
        return 'D+'
    elif avg >= 65 and avg <= 66:
        return 'D'
    else:
        return 'F'

#print(avg_score_letter())
# entered 88 and 99 got A
# true because average rounded is 94

#D
def num_day():
    day = int(input("Enter a number between 1-7 "))
    if day != 1 and day != 2 and day != 3 and day != 4 and day != 5 and day != 6 and day != 7:
        print("Invalid input, enter a number between 1-7")
        num_day()  # recall function recursively, wait for valid input
    else:
        if day == 1:
            return "Monday"
        elif day == 2:
            return "Tuesday"
        elif day == 3:
            return "Wednesday"
        elif day == 4:
            return "Thursday"
        elif day == 5:
            return "Friday"
        elif day == 6:
            return "Saturday"
        else:
            return "Sunday"

#print(num_day())
# Entered 4 got thursday


#E
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number:  "))
operation = ("Type 's' for subtraction or 'a' for addition").upper()
if operation == 'S':
    print(num1-num2)
else:
    print(num1+num2)

#F
def fit_in_cube(cube_side, a):
    if cube_side > a:
        print("Cube's side is greater than prism's width, cube cannot fit geometrically")
        c2 = int(input("Enter new cube side measurement"))
        a2 = int(input("Enter new prism smallest side measurement"))
        fit_in_cube(c2, a2)
    else:
        prism_vol = a*(9.0*a)*(8*a)
        cube_vol = cube_side ** 3.0
        print("{} cubes fit in the rectangular prism".format(prism_vol/cube_vol))


#fit_in_cube(2, 7)
# Entered 2 and 7 got 3087
# Entered 7 and 2 got geometrical error message
