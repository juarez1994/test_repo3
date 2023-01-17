#3.Check if a variable is a string. If yes, print out the string, if not, print out a warning
#message.


def typechecker(variable):
    if type(variable)==str:
        print(variable)
    else:
        print("Warning variable is NOT a string")
#test
a_string="Hello world"
an_integer=5

typechecker(a_string)
typechecker(an_integer)
