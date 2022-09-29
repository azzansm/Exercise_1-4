bill = int(input("Enter amount of bill: "))
people = int(input("Enter number of people: "))
tips = int(input("Enter amount of tips (%): "))
tip_amount = bill*(tips/100)
print(f"Tip amount per person is ${tip_amount/people:.2f}")
total_amount = ((bill + tip_amount)/people)
print(f"Total amount per person is ${total_amount:.2f}")

sec = int(input("Enter time in second: "))
h = int(sec/3600)
sec = sec%3600
m = int(sec/60)
s = int(sec%60)
print("Result: ",h,":",m,":",s)
