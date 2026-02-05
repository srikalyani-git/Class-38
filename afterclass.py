print("Exam eligibility test")
total = int(input("Enter total working days:"))
present = int(input("Enter number of days present:"))
percent = (present/total)*100
if percent>=75:
    print("You are eligible for the exam")
else:
    print("You are not eligible for the exam")