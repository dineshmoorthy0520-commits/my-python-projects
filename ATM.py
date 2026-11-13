
Balance = 10000
correct_PIN = "0512"
attempt = 3

while attempt > 0:

    PIN = input("Enter your PIN: ")

    if PIN == correct_PIN:

        print("=== WELCOME TO PRIVY BANK ===")

        while True:
            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Your bank balance: ₹{Balance}")
                break

            elif choice == "2":
                deposited = int(input("Enter deposit amount: "))
                if deposited > 0:
                    Balance += deposited
                    print(f"Your new balance: ₹{Balance}")
                else:
                    print("Enter a valid amount")
                break

            elif choice == "3":
                withdrew = int(input("Enter withdrawal amount: "))

                if withdrew <= 0:
                    print("Enter a valid amount")
                elif withdrew <= Balance:
                    Balance -= withdrew
                    print(f"Your new balance: ₹{Balance}")
                else:
                    print("Insufficient balance!")
                break

            elif choice == "4":
                print("Thank you for using Privy Bank!")
                break

            else:
                print("Invalid choice!")

        break

    else:
        attempt -= 1
        print(f"Wrong PIN! {attempt} attempts remaining.")

if attempt == 0:
    print("ATM ACCESS LOCKED")

        
            
        
        
    
    
    
        
        
        

