# author: DMH 9/29/21

grade = input=("What was your grade?")

if grade < 60:
    print("You got an F")
elif grade < 65:
    print("You got a D")
elif grade < 70:
    print("You got a D+")
elif grade < 73:
    print("You got a C-")
elif grade < 77:
    print("You got a C")
elif grade < 80:
    print("You got a C+")
elif grade < 83:
    print("You got a B-")
elif grade < 87:
    print("You got a B")
elif grade < 90:
    print("You got a B+")
elif grade > 93:
    print("You got a A-")
else:
    print("You got an A")
