# database.py

def show_members(family_members):

    print("\n===== MEMBER LIST =====")

    if len(family_members) == 0:
        print("No Member")
        return

    for i in range(len(family_members)):
        print("----------------------------")
        print("No.", i + 1)
        print("Name :", family_members[i]["name"])
        print("Age :", family_members[i]["age"])
        print("Role :", family_members[i]["role"])
        print("Power :", family_members[i]["power"])
        print("Money :", family_members[i]["money"])


def search_member(family_members):

    print("\n===== SEARCH MEMBER =====")

    name = input("Enter Name : ")

    found = False

    for member in family_members:
        if member["name"].lower() == name.lower():

            print("\nMember Found")
            print("Name :", member["name"])
            print("Age :", member["age"])
            print("Role :", member["role"])
            print("Power :", member["power"])
            print("Money :", member["money"])

            found = True
            break

    if found == False:
        print("Member Not Found")
