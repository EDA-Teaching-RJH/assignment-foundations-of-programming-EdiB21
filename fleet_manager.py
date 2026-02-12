
def init_database():
    global N, R, D, ID
    N = ["Picard", "Riker", "Data", "Forge", "Crusher"]
    R = ["Captain", "Commander", "Lt.Commander", "Lt.Commander", "Commander"]
    D = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ID = ["001", "002", "003", "004", "005"]
    return N, R, D, ID


def display_menu():
    global N, R, D, ID

    print("Welcome to the Fleet Manager Terminal \n -----------------")
    print("Please give your : Name and ID")

    user_ID, user_name = user_verification()

    while True:
        print("\n--- ACCESS MENU ---")
        print("1. View Crew Members")
        print("2. Add Crew Member")
        print("3. Remove Crew Member")
        print("4. Update Crew Member Rank")
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
            remove_member()
        elif user_option == "4":
            update_rank()
        elif user_option == "5":
            search_crew()
        elif user_option == "6":
            calculate_payroll()
        elif user_option == "7":
            x = 6
        elif user_option == "8":
            print("Closing Terminal. \n. \n.. \n...")
            break



def user_verification():
    global N, R, D, ID

    user_name = input("Name : ").strip().title()
    if user_name == "":
        print("Name cannot be empty.")
        return user_verification()
    
    while True:

        user_ID = input("ID : ").strip()

        if not (len(user_ID) == 3 and user_ID.isdigit()):
            print("Invalid ID. ID must be 3-digits.")
            continue
        if user_ID in ID:
            print("Access Denied, ID already exists.")
            continue
        elif user_ID == "":
            print("ID cannot be empty.")
            continue
        else:
            print("ID accepted. \n  Welcome: " + user_name +", " + user_ID)
            break
    return user_ID, user_name


def display_roster():
    global N, R, D, ID

    print("\n\t\t  --- CREW ROSTER ---")
    print("----------------------------------------------------")
    print(f"{'|Name':<11} | {'Rank':<15} | {'Division':<12} | {'ID  |':<4}")
    print("----------------------------------------------------")
    for i in range(len(N)):
        print(f"|{N[i]:<10} | {R[i]:<15} | {D[i]:<12} | {ID[i]:<3} |")
    print("----------------------------------------------------")



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
        else:
            ID.append(new_member_ID)
            break
    print("-------------------------------")
    print(f"New member added: {new_member_N}, {new_member_R}, {new_member_D}, {new_member_ID}")


def remove_member():
    global N, R, D, ID

    print("\n--- REMOVE CREW MEMBER ---")
    print(" ")


    while True:

        remove_ID = input("Enter the ID of the memeber you wish to remove: ").strip()

        if remove_ID in ID:

            find_ID = ID.index(remove_ID)

            N.pop(find_ID)
            R.pop(find_ID) 
            D.pop(find_ID)
            ID.pop(find_ID)

            print("The member with ID " + "'" + remove_ID + "'" + " and name " + "'" + N[find_ID] + "'" + " has been removed from the system.")
            break
        else:
            print("ID not found. " + remove_ID + " is not registered in the system.")
            return
        

def update_rank():
    global N, R, D, ID

    valid_ranks = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Ensign", "Chief Officer", "Crewman"]

    print("\n--- UPDATE RANK ---")
    print(" ")
    print("These are the valid ranks: " + ", ".join(valid_ranks))

    while True:

        ID_entry = input("Enter the ID of the member that will be updated: ").strip()

        if ID_entry in ID:

            find_rank = ID.index(ID_entry)
            print("Member : " + N[find_rank] + ", Current Rank: " + R[find_rank] + ", ID: " + ID[find_rank])

            new_rank = input("Enter new rank: ").strip().title()
            R[find_rank] = new_rank
            print("Updating\n.\n..\n...")
            print("Rank updated.\n New rank : " + R[find_rank] + ", given to member : " + N[find_rank])
            break
        else:
            print("ID not found. Enter a valid ID.")
            continue


def search_crew():
    global N, R, D, ID

    print("\n--- FIND CREW MEMBER/S ---")
    print(" ")

    while True:

        search_option = input("Search by : \n1. Name \n2. Rank \n3. Division \n4. ID \nSelect option: ").strip()

        if search_option == "1":
            search_name = input("Enter a name to search: ").strip().title()

            if search_name in N:
                find_name = N.index(search_name)
                print("Member found: " + N[find_name] + ", Rank: " + R[find_name] + ", Division: " + D[find_name] + ", ID: " + ID[find_name])
                break
            else:
                print("Name not found.")
                print(" ")
                print("Would you like to use a different search option? (Y/N)")
                search_restart = input(": ").strip().upper()
                if search_restart == "Y":
                    continue
                else:
                    break

        elif search_option == "2":
            find_rank = input("Enter a rank to search: ").strip().title()

            if find_rank in R:
                print("Member/s found with rank: " + find_rank + " are -->")
                for i in range(len(R)):
                    if R[i] == find_rank:
                        print("Name: " + N[i] + ", Rank: " + R[i] + ", Division: " + D[i] +", ID: " + ID[i])
                break
            else:
                print("No members found with rank: " + find_rank)
                print("Would you like to use a different search option? (Y/N)")
                search_restart = input(": ").strip().upper()
                if search_restart == "Y":
                    continue
                else:
                    break

        elif search_option == "3":
            find_division = input("Enter a division to search: ").strip().title()

            if find_division in D:
                print("Member/s found in division: " + find_division + " are -->")
                for i in range(len(D)):
                    if D[i] == find_division:
                        print("Name: " + N[i] + ", Rank: " + R[i] + ", Division: " + D[i] +", ID: " + ID[i])
                break
            else:
                print("No members found with division: " + find_division)
                print("Would you like to use a different search option? (Y/N)")
                search_restart = input(": ").strip().upper()
                if search_restart == "Y":
                    continue
                else:
                    break

        elif search_option == "4":
            search_ID = input("Enter an ID to search: ").strip()

            if search_ID in ID:
                print("Member with ID: " + search_ID + " is:")
                find_ID = ID.index(search_ID)
                print("Name: " + N[find_ID] + ", Rank: " + R[find_ID] + ", Division: " + D[find_ID] +", ID: " + ID[find_ID])
                break
            else:
                print("No member found with ID: " + search_ID)
                print("Would you like to use a different search option? (Y/N)")
                search_restart = input(": ").strip().upper()
                if search_restart == "Y":
                    continue
                else:
                    break


def calculate_payroll():
    global N, R, D, ID

    print("\n--- CREW COST ANALYSIS ---")
    print(" ")

    total_cost = 0

    for i in range(len(R)):
        if R[i] == "Captain":
            total_cost += 1000
        elif R[i] == "Commander":
            total_cost += 800
        elif R[i] == "Lt.Commander":
            total_cost += 600
        elif R[i] == "Lieutenant":
            total_cost += 400
        elif R[i] == "Ensign":
            total_cost += 250
        elif R[i] == "Chief Officer":
            total_cost += 200
        elif R[i] == "Crewman":
            total_cost += 100
    print("Total payroll of crew: " + str(total_cost) + " CRD")



    











#Start Of Program
init_database()

display_menu()  

