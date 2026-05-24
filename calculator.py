def get_val_001(arg_001):
    while True:
        val = input(arg_001)
        try:
            number = float(val)
            print(f"The first number is: {number}")
            return number
        except ValueError:
            print("You entered an incorrect format! Letters are not allowed. Only numbers please!\n")
            """
            The function will keep asking for input until a valid number is entered. If the user enters something that cannot be converted to a float, it will catch the ValueError and prompt the user again.
            """
no_001 = get_val_001("Enter the first value:\t")
# -----------------------------------------------------------------------------------
def get_val_002(arg_002):
    while True:
        val1 = input(arg_002)
        try:
            number1 = float(val1)
            print(f"The second number is: {number1}")
            return number1
        except ValueError:
            print("You entered an incorrect format! Letters are not allowed. Only numbers please!\n")
            """
            Similar to the first function, this one will also keep asking for input until a valid number is entered. If the user enters something that cannot be converted to a float, it will catch the ValueError and prompt the user again.
            """
no_002 = get_val_002("Enter the second value:\t")
# ------------------------------------------------------------------------------------
def operator_01(op_001):
    while True:
        operatorinput = input(op_001)
        if operatorinput in ["+","-","*","/"]:
            print("The operator you entered is:", operatorinput)
            return operatorinput
        else:
            print("You entered an inappropriate operator! Use only: +, -, *, /")
"""
This func. will simply ask for operator for operation. Allowed Operators are + - * /.
"""           
print("What operator do you want to use:\n1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)")
operator_ask = operator_01("Enter Your Operator:\t")

# ------------------------------------------------------------------------------------
# For addition
if operator_ask in ["+"]:
    result_001 = no_001 + no_002
    print("The result is ", result_001)
# For subtraction
if operator_ask in ["-"]:
    result_002 = no_001 - no_002
    print("The result is ", result_002)
# For multiplication
if operator_ask in ["*"]:
    result_003 = no_001 * no_002
    print("The result is ", result_003)
# For division
if operator_ask in ["/"]:
    result_004 = no_001 / no_002
    print("The result is ", result_004)
# ------------------------------------------------------------------------------------
"""
END OF THE PROGRAM
"""