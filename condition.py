marks=int(input("Marks : "))

def show_grade(grade):
    print(f"You got : {grade}")


if marks>=80:
    show_grade("A+")
elif marks<80 and marks>=70:
    show_grade("A")
elif marks<70 or marks>60:
    show_grade("A-")
elif marks>33:
    show_grade("Passed")
else: show_grade("FAILED")

