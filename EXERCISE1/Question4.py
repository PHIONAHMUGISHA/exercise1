# 4 witi academy is proposing a sacco to help students save their money 
           # Design a platform that will do the following
           # welcome to, WITIAcademy Sacco
           #1. Deposit money
           #2. Withdraw money
           #3. Check balance
           # ensure if the students selects 1, money is deposited and the minimum deposit should be 1000.
           #if the student selects 2, money is withdrawn and a minimum withdraw is 500.
           # if the student selects 3, the account balance should be displayed. 
           def sacco_transactions():
            account_balance = 0
            run = 1
            while run == 1:
              print("\nwelcome to,WITI Academy sacco.")
              # menu
              print("1. Deposit money")
              print("2. Withdraw money")
              print("3. Check Balance")
              student_choice =int(input("Enter your selection")(1,2or3):)
              if student_choice == 1:
              print("\n...processing a deposit amount transaction...")
              deposit_amount=(input'enter the amount to be deposited:')
              
              #check if deposit amount is less than 1000
              if deposit_amount<1000:
              print('\nminimum deposit is 1000')
              else:account_balance+=deposit_amount
              print("Dear students you have deposited{deposit_amount:,}and your new acount balance is{acount_balance
              }")
              if student_choice==2:
                print("\n...processing a withdraw")
                withdraw_amount=int(input("Enter the amount to be withdraw:"
                if acount_balance==0
                print("your account_balance iso")
                else:
                  account_balance-=withdraw_amount
                  print(f"Dear students,you have withdrawn{withdraw_amount:,and your new account_balance is{acount_balance:,}}")
              elifstudent_choice === 3:
              print("you have entered a wroing choice!select from 1,2,or 3")
              run =int(input("Enter 1 to continue or any number to exist:"))
              if run != 1:
                print("Thanks for using the sacco")

                sacco_transactionOS
  