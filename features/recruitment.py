# recruitment.py

def add_member(family_members):

    print("\n=== Add Member ===")

    name = input("Name : ")
    age = int(input("Age : "))
    role = input("Role : ")
    power = int(input("Power : "))
    money = int(input("Money : "))

    member = {
        "name": name,
        "age": age,
        "role": role,
        "power": power,
        "money": money
    }

    family_members.append(member)

    print("Add Member Success")


def remove_member(family_members):

    print("\n=== Remove Member ===")

    if len(family_members) == 0:
        print("No Member")
        return

    print("\nMember List")

    for i in range(len(family_members)):
        print(i + 1, family_members[i]["name"])

    choose = int(input("Choose Number : "))

    if choose >= 1 and choose <= len(family_members):
        family_members.pop(choose - 1)
        print("Remove Success")
    else:
        print("Wrong Number")
