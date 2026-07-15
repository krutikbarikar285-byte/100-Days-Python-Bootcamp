print("Welcome to the Tip Calculator!!")
try:
    total_bill=int(input("Enter the total bill:$"))
    tip_percent=int(input("Ënter the total percent of bill you wanna give tip off:%"))
    split=int(input("With how many people you wanna split the bill:"))
    final_amount=total_bill + (total_bill/100)*tip_percent
    amount_perhead=format(final_amount/split,".2f")
except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("invalid input")
else:
    print(f"Each person should pay:${amount_perhead}")
finally:
    print("Thanks for using the Tip Calculator.")




