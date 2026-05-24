def user_in(inputfromuser):
    while True:
        input_001 = input(inputfromuser)
        try:
            finalinput_user = float(input_001)
            print(f"The number you've entered is {finalinput_user}")
            if finalinput_user > 0:
                print(f"The number {finalinput_user} is positive.")
            elif finalinput_user < 0:
                 print(f"The number {finalinput_user} is negative.")
            elif finalinput_user == 0:
             print(f"The number {finalinput_user} is null or zero(0).")
            return finalinput_user
        except:
            print("Please enter the input in a correct format (e.g. 1,5,88,77,77.5,-77.5 e.t.c)")
            """
            User Input
            """
            # Func. 1 End
readnum = user_in("Enter The Number:")