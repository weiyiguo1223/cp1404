
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    " gat grade in number and show it in state"
    score = float(input("Enter score: "))
    print(grade_status(score))


def grade_status(score):
    " Determine state of giving score "
    while score < 0 or score > 100:
        print("invalid input,please input 0-100")
        score = float(input("Enter score: "))
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
