marks1 = float(input("Enter your marks for subject 1: "))
marks2 = float(input("Enter your marks for subject 2: "))
marks3 = float(input("Enter your marks for subject 3: "))
marks4 = float(input("Enter your marks for subject 4: "))
marks5 = float(input("Enter your marks for subject 5: "))
marks = (marks1 + marks2 + marks3 + marks4 + marks5)
perc = (marks/500) * 100
if perc >= 90:
    print("Grade A+")
elif 80 <= perc < 90:
    print("Grade A")
elif 70 <= perc < 80:
    print("Grade B")
elif 60 <= perc < 70:
    print("Grade C")
elif 50 <= perc < 60:
    print("Grade D")
else:
    print("Fail")