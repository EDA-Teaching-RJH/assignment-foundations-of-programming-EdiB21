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












def add_member(user_ID):
    global N, R, D, ID

    valid_ranks = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Ensign", "Chief Officer", "Crewman"]
    valid_divisions = ["Command", "Operations", "Sciences", "Engineering", "Medical", "Security"]

    print("\n--- ADD CREW MEMBER ---")
    print(" ")
    print("These are the valid ranks: " + ", ".join(valid_ranks))
    print("------------------------------")
    print("These are the valid divisions: " + ", ".join(valid_divisions))
    print("------------------------------")


    print("Now please enter the new crew member's information: ")

    while True:
        new_member_N = input("Name: ").strip().title()

        if new_member_N == "":
           print("Name cannot be empty.")
           continue
        elif new_member_N in N:
           print("Name already exists. Please enter a unique name.")
           continue
        else:
            N.append(new_member_N)
            break
    

    while True:

        new_member_R = input("Rank: ").strip().title()

        if new_member_R not in valid_ranks:
            print("Invalid rank. Please enter a valid rank.")
            continue
        elif new_member_R == "":
            print("Rank cannot be empty.")
            continue
        else:
            R.append(new_member_R)
            break


    while True:   

        new_member_D = input("Division: ").strip().title()
        
        if new_member_D not in valid_divisions:
            print("Invalid division. Please enter a valid division.")
            continue
        elif new_member_D == "":
            print("Division cannot be empty.")
            continue
        else:
            D.append(new_member_D)
            break
    

    while True:

        new_member_ID = input("ID: ").strip()

        if new_member_ID in ID:
            print("ID already exists. Please enter a unique ID.")
            continue
        elif new_member_ID == "":
            print("ID cannot be empty.")
            continue
        elif new_member_ID == user_ID:
            print("Your ID is already registered.")
            break
        else:
            ID.append(new_member_ID)
            break
    print("-------------------------------")
    print(f"New member added: {new_member_N}, {new_member_R}, {new_member_D}, {new_member_ID}")