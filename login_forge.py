import datetime


users = {
    "admin": {"password": "1234", "attempts": 0, "locked": False},
    "guest": {"password": "guest", "attempts": 0, "locked": False},
}
# constants
SUCCESS = "success"
RETRY = "retry"
LOCKED = "locked"
MAX_ATTEMPTS = 3

# logger
login_log = []

# states
current_user = None


def login():
    """Info: user login"""

    global current_user

    username = input("Username: ").strip().lower()

    if username not in users:
        print("User does not exist.")
        return

    if not users[username]["locked"]:
        while users[username]["attempts"] < MAX_ATTEMPTS:
            password = input("Password: ")
            result = password_validation(username, password)

            if result == SUCCESS:
                users[username]["attempts"] = 0
                current_user = username

                add_log(username, SUCCESS)

                print("Login successful.")
                return

            if result == LOCKED:
                add_log(username, LOCKED)
                print("Account locked.")
                return

            add_log(username, RETRY)

            print(
                f"Incorrect. Attempts left: {MAX_ATTEMPTS - users[username]['attempts']}"
            )
    else:
        print("Cannot authenticate. Your account is locked.")


def password_validation(user, password):
    """Info: checks if password is correct, if not give attempts, otherwise lock user"""

    if password == users[user]["password"]:
        return SUCCESS

    # wrong password
    users[user]["attempts"] += 1
    if users[user]["attempts"] >= MAX_ATTEMPTS:
        users[user]["locked"] = True
        return LOCKED
    return RETRY


def password_change():
    """Info: update the password"""
    old_password = input("Old password: ")

    if users[current_user]["password"] == old_password:
        while True:
            new_password = input("New password: ")

            if len(new_password) == 0:
                print("Password cannot be empty.")
            else:
                users[current_user]["password"] = new_password
                break


def add_log(user, status):
    login_log.append(
        {
            "user": user,
            "status": status,
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )


def track_login_attempts():
    """Info: amount of attempted logins"""
    global login_log

    for entry in login_log:
        print(entry)


def admin_unlock():
    """Info: unlock a locked user. Only admin user can perform this action."""
    user = input("Choose user: ").strip().lower()

    if user not in users:
        print("User does not exist.")
        return

    if users[user]["locked"] is True:
        users[user]["locked"] = False
        users[user]["attempts"] = 0
        print("User unlocked successfully.")
        return

    print("User is not locked.")


def logout():
    global current_user

    current_user = None
    print("User signed out.")


def show_menu():
    """Info: show CLI menu"""
    print("|------------------------------------------|")
    print("|                 COMMANDS                 |")
    print("|------------------------------------------|")
    print("| - login: authentication                  |")
    print("| - unlock: unlock users                   |")
    print("| - change password: update password       |")
    print("| - history: see login attempts            |")
    print("| - logout: sign out                       |")
    print("| - help: show manual with commands        |")
    print("| - exit: exit the program                 |")
    print("|------------------------------------------|")


show_menu()

while True:
    command = input("command: ")

    if command == "login":
        if not current_user:
            login()
        else:
            print("User already authenticated")
    elif command == "unlock":
        if current_user == "admin":
            admin_unlock()
        else:
            print("You do not have access to this command.")
    elif command == "change password":
        if current_user:
            password_change()
        else:
            print("You must be logged to change password.")
    elif command == "history":
        if current_user == "admin":
            track_login_attempts()
    elif command == "logout":
        logout()
    elif command == "help":
        show_menu()
    elif command == "exit":
        print("Exiting program...")
        break
