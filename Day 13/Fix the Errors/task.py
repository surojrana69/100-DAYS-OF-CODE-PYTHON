try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please write the numerical number like 12 or 19.")
    age = int(input("How old are you?"))
if age >= 18:
    print(f"You can drive at age {age}.")
