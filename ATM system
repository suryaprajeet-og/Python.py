# #####################################################################
# PROJECT 2: ATM SYSTEM
# #####################################################################

name = input(" Enter Name: ")
print(" Hello", name)

correct_pin = 1234
attempt = 0

while attempt < 3:
    pin = int(input(" Enter PIN: "))

    if pin == correct_pin:
        print(" Welcome back!")
        break

    else:
        print(" Wrong Pin, Try Again!")
        attempt = attempt + 1

        if attempt < 3:
            attempts_left = 3 - attempt
            print(" Attempts Left:", attempts_left)

if pin == correct_pin:

    while True:

        choice = input(" Choose Check Balance or Deposit or Withdraw or Exit: ")

        if choice == "Check Balance":

            balance = int(input(" Enter Current Balance: "))
            print(" Your Balance is:", balance)
            print(" Thank You!")

        elif choice == "Deposit":

            current_balance = int(input(" Enter Current Balance: "))
            deposit = int(input(" Enter Deposit Amount: "))

            final_balance = current_balance + deposit

            print(" Final Balance:", final_balance)

        elif choice == "Withdraw":

            current_balance = int(input(" Enter Current Balance: "))
            withdraw = int(input(" Enter Withdraw Amount: "))

            if withdraw > current_balance:
                print(" Transaction Failed! Insufficient Balance!")

            else:
                final_balance = current_balance - withdraw

                print(" Transaction Successful!")
                print(" Final Balance:", final_balance)

                if final_balance < 1000:
                    print(" WARNING! Maintain Minimum Balance!")

        elif choice == "Exit":

            print(" Exit Successful!")
            print(" Thank You! Visit Again.")
            break

        else:
            print(" Invalid Choice!")

else:
    print(" Too Many Wrong Attempts!")
    print(" Card Blocked. Try Again Later.")
    

