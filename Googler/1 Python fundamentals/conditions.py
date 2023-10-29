marks = int(input("What is your mark in programming: "))


def show_grade(grade):
    print(f"you got {grade}")

if marks >= 80:
    show_grade("A+")

elif marks >= 70 and marks < 80:
    show_grade("A")

elif marks >= 60 and marks < 70:
    show_grade("A-")

elif marks > 40:
    show_grade("passed")

else:
    show_grade("F")