age = 20
if age < 18:
    print('Eligible to drive')
else:
    print('Not eligible to drive')

# if_elif_else
marks = int(input("What did you score?\n"))
if marks > 80:
    print("Grade A")
elif marks > 70 and marks <= 80:
    print("Grade B")
elif marks > 60 and marks <= 70:
    print("Grade C")
elif marks > 50 and marks <= 60:
    print("Grade D")
else:
    print("You failed")
