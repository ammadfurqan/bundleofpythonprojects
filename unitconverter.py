
def units_consumed(consumedunits_001):
    while True:
        units_consumed_input = input(consumedunits_001)
        try:
            consumed_units = float(units_consumed_input)
            print("You consumed:\t", consumed_units)
            return consumed_units
        except ValueError:
            print("You've entered incorrect input, please enter a correct input.")
            """
            This func. will take units as input
            """
#-----------------------------------------------------------------------------------------
def category(category):
    while True:
        category_01 = input(category)
        if category_01 in ["A","B","C","D"]:
            print("You choosed category:", category_01)
            return category_01
        
    else:
            print("Only A,B,C or D are allowed. Please type any one of following\nA\nB\nC\nD")
"""
The fun. will get the category from the user
"""            
#-----------------------------------------------------------------------------------------
consumed_units_01 = units_consumed("How many units you've consumed:\t")
print("What is your category:\nA:\tMillion Class\nB:\tHigh Class\nC:\tMiddle Class\nD:\tLow Class")
category_001 = category("Enter Your Category (e.g. A,B,C or D.):\t")
#-----------------------------------------------------------------------------------------
cost_mc = 1 #per unit
cost_hc = 0.90 #per unit
cost_nc = 0.50 #per unit
cost_lc = 0.10 #per unit
if (category_001 == "A"):
        con_001 = cost_mc * consumed_units_01
        print("Hehe.. Son of musk")
        print(f"You have to pay ${con_001}")
elif (category_001 == "B"):
    con_002 = cost_hc * consumed_units_01
    print("Uff.. Too hot")
    print(f"You have to pay ${con_002}")
elif (category_001 == "C"):
    con_003 = cost_nc * consumed_units_01
    print("Hope to see you progress")
    print(f"You have to pay ${con_003}")
elif (category_001 == "D"):
    con_004 = cost_lc * consumed_units_01
    print("God bless you..")
    print(f"You have to pay ${con_004}")







