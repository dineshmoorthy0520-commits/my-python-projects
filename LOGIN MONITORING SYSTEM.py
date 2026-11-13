print("=== LOGIN MONITORING SYSTEM ===")

correct_username = "dinesh"
correct_password = "arul"
attempts = 3

while attempts > 0:
    username = input("Enter your username:").strip()
    password = input("Enter your password:").strip()

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Invalid credentials. You have {attempts} attempts left.")

if attempts == 0:
    print("Too many failed attempts. Access denied.")