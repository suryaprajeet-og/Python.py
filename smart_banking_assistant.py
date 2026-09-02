# #####################################################################
# PROJECT 3: SMART BANKING ASSISTANT (FUNCTION-BASED)
# #####################################################################

name = input(" Enter Customer Name: ")
current_balance = int(input(" Enter current balance: "))
def welcome():
    print("Welcome ", name)
    
(welcome())

def check_balance():
    print(" Current Balance is: ", current_balance)
    
def deposit():
    print(" Current Balance is: ", current_balance)
    deposit = int(input(" Enter Deposit Amount: "))
    new = current_balance + deposit 
    print(" Your New balance is: ", new)
    
def withdraw():
    print(" Current Balance Is: ", current_balance)
    withdraw = int(input(" Enter Withdraw amount: "))
    if current_balance < withdraw:
        print(" Transaction failed Due to Insufficient Balance! ")
    else:
            final_balance = current_balance - withdraw
            
            if final_balance > 1000:
                print(" Transaction succesful! ")
            else:
                    print(" Transaction successful! ")
                    print(" WAENING! MAINTAIN MINIMUM BALANCE.")
                    
def change_pin():
    global pin
    print(" Your Current Pin is: ", pin)
    change = input(" Do you want to Change your pin, Yes or No: ")
    if change == "Yes":
        while True:
            new_pin = int(input(" Enter your New pin: "))
            confirm = int(input(" Confirm New Pin: "))
            if new_pin == confirm:
                pin = new_pin
                print(" Pin changed Successfully! ")
                break
                
            else:
                print(" Check your new pin matching Confirm new pin! ")
                
    else:
                print(" Pin Unchanged! ")
                

attempt = 0
pin = 1234
while attempt < 3:
    pin = int(input(" Enter Pin: "))
    if pin == 1234:
        print(" Login Successful! ")
        break
    else:
        if attempt < 3:
            attempt = attempt + 1
            attempts_left = 3 - attempt
            print(" Incorrect Pin! Try again.")
            print(" Attempts Left: ", attempts_left)
        else:
            print(" Login failed! Too many attrmpts. Try again after 24 hours.")
        

if pin == 1234:
                while True:
                    choice = input(" Enter Check Balance or Deposit or Withdraw or Change Pin or Exit: ")
                    
                    if choice == "check balance":
                        check_balance()
                    
                    elif choice == "deposit":
                        deposit()
                    
                    elif choice == "withdraw":
                        withdraw()
                        
                    elif choice == "change pin":
                        change_pin()
                        
                    elif choice == "exit":
                        print(" Exit Successful! Thank You.")
                        break
                        
                    else:
                        print(" Invalid Choice! ")
                        
                        
                
                    
                    
                    
                    
            

        
        
        
        
    

