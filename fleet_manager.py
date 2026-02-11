def init_database():
    global N, R, D, ID
    N = ["Picard", "Riker", "Data", "Forge", "Crusher"]
    R = ["Captain", "Commander", "Lt.Commander", "Lt.Commander", "Commander"]
    D = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ID = ["001", "002", "003", "004", "005"]
    return N, R, D, ID


def display_menu():
    global N, R, D, ID

    print("Welcome to the Fleet Manager \n -----------------")
    print("Please give your : Name and ID")

    user_ID = user_verification()

    while True:
        print("\n--- ACCESS MENU ---")
        print("1. View Crew Members")
        print("2. Add Crew Member")
        print("3. Remove Crew Member")
        print("4. Update Crew Member Info")
        print("5. Find Crew Member")
        print("6. Crew Cost Analysis")
        print("7. Additional processes")
        print("8. Exit")

        user_option = input("Select option: ").strip()
    
        if user_option == "1":
            display_roster()
        elif user_option == "2":
            add_member(user_ID)
        elif user_option == "3":
            x = 2
        elif user_option == "4":
            x = 3
        elif user_option == "5":
            x = 4
        elif user_option == "6":
            x = 5
        elif user_option == "7":
            x = 6
        elif user_option == "8":
            print("Closing Program. \n .... \n ....")
            break



def user_verification():
    global N, R, D, ID

    user_name = input("Name : ").strip().title()
    if user_name == "":
        print("Name cannot be empty.")
        return user_verification()
    
    while True:

        user_ID = input("ID : ").strip()

        if user_ID in ID:
            print("Access Denied, ID already exists.")
            continue
        elif user_ID == "":
            print("ID cannot be empty.")
            continue
        else:
            print("ID accepted. \n ID registered. \n  Welcome: " + user_name +", " + user_ID)
            ID.append(user_ID)
            break
    return user_ID, user_name