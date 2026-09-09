marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

if marks >= 80:
    if attendance >= 75:
        if income <= 300000:
            print("Eligible for scholarship")
        else:
            print("Not eligible: Family income is too high")
    else:
        print("Not eligible: Attendance is too low")
else:
    print("Not eligible: Marks are too low")
