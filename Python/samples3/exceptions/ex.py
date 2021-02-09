try:
    num = (1/float(input("\nEnter a number: ")))
except(ValueError):
    print("Not number")
except(KeyboardInterrupt):
    print("KeyboardInt happened")
except(ZeroDivisionError):
    print("Division by zero")
else:
    print(f"You entered the number - {num}")
