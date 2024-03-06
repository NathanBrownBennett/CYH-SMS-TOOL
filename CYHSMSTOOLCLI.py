import sys

# Simulate a database with user credentials and poll responses
users = {
    'mr.user@email.com': '7310289491',
    'user' : 'password',
    'user2' : 'password2',
    'guest' : 'guest',
    'admin' : 'admin'
}
poll_responses = {}

def login():
    print("1. Login")
    print("2. Create an account")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return username, password
    elif choice == "2":
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        users[username] = password
        print("Account created successfully!\n")
        return username, password
    else:
        print("Invalid choice. Please try again.")
        return None, None

def main_menu():
    print("1. View your groups")
    print("2. Receive the latest updates from the platform today")
    print("3. Open your conversations")
    print("4. Settings")
    choice = input("Enter your choice: ")
    return choice

def handle_poll():
    print("CYF Connectivity Project Poll")
    print("1. Yes via www.meetingsite.com/link")
    print("2. Yes via call")
    print("3. Not this time, but forward transcript or notes after meeting")
    print("4. Not this time")
    poll_choice = input("Enter your poll choice: ")
    return poll_choice

def application():
    print("Welcome to the CYH SMS Tool Interface.")
    username, password = login()

    # Check if the credentials are correct
    if users.get(username) == password:
        print("Login successful!\n")
        while True:
            choice = main_menu()

            if choice == "1":
                print("View your groups: [Group details not implemented]")
            elif choice == "2":
                print("Latest updates: [Update details not implemented]")
                poll_choice = handle_poll()
                poll_responses[username] = poll_choice
                print("Your response has been recorded.")
            elif choice == "3":
                print("Open your conversations: [Conversation details not implemented]")
            elif choice == "4":
                print("Settings: [Settings details not implemented]")
            else:
                print("Invalid choice. Please try again.")

            # Provide an option to log out
            logout = input("Do you want to log out? (y/n): ")
            if logout.lower() == 'y':
                break
    else:
        print("Login failed. Invalid username or password.")
        

# Run the application
if __name__ == "__main__":
    application()
