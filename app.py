#Welcome message 
print("Welcome to my Python program!")

#Ask user for their input
hours = input("How many hours did you study today?")

#Convert input safely with error handling 
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number for hours.")
    exit()

#Perform a calculation (weekly study estimate)
weekly_hours = hours * 7

#Display the result clearly
print(f"You are on track to study approximately {weekly_hours} hours this week.")

#Encourage the user
print("Keep up the awesome work!")
#testchanges