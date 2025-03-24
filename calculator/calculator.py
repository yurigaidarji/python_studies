import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = { "+":add, "-": subtract, "*": multiply, "/":divide }

# print(operations.get("*")(4, 8))

print(art.logo)
must_save_result = False
while not must_save_result:
    number1 = float(input("What's the first number? "))
    must_save_result = True

    while must_save_result:
        for op in operations:
            print(op)
        user_operation = input("Pick an operation: ")
        number2 = float(input("What's the second number? "))
        result = operations.get(user_operation)(number1, number2)
        print(f"{number1} {user_operation} {number2} = {result}")

        user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if user_choice == 'y':
            number1 = result
        else:
            must_save_result = False
            print("\n" * 10)
