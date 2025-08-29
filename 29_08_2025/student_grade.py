# Assignment 2
score = 65
if score > 90:
    print("Grade A")
elif score > 80:
    print("Grade B")
elif score > 70:
    print("Grade C")
elif score > 60:
    print("Grade D")
else:
    print("Grade F")

# Assignment 2 - Defferent variant
score = 90
if score > 90:
    print("Grade A")
else:
    if score > 80:
        print("Grade B")
    else:
        if score > 70:
            print("Grade C")
        else:
            if score > 60:
                print("Grade D")
            else:
                print("Grade F")
