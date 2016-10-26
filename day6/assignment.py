'''
Dor Rondel
CSc-113
Section: 9:30 am
'''

#1 - Recursive Factorial
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)

#2 - Month-num, no conditionals or loops
month_dict = {
    "1": "Jan", "2": "Feb", "3": "Mar", "4": "Apr",
    "5": "May", "6": "Jun", "7": "Jul", "8": "Aug",
    "9": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
}

choice = str(input("Enter month number")) # for cross version compatibility
print(month_dict(choice))

#3 - Recursive Fibonnacci
def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
