hour = int(input("Enter the hour (0-23): "))

if hour >= 5 and hour < 12:
    print("Morning")
elif hour >=12 and hour < 17:
    print("Afternoon")
elif hour >= 17 and hour < 21:
    print("Evening")
else:
    print("Night")            