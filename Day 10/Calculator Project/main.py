from art import logo


def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def calculator():
    print(logo)
    should_accumulate = True
    num1=float(input("Enter the first number: "))
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operator=input("Enter the operation you want to do: ")
        num2=float(input("Enter the second number: "))
        answer=(operations[operator](num1 ,num2))
        print(f"{num1} {operator} {num2} = {answer}")

        choice=input(f"Type 'y to conitnue calculating with {answer}, or type 'n' to start new calculations: ")

        if choice =='y':
            num1=answer
        else:
            should_accumulate=False
            print("\n"*40)
            calculator()

calculator()