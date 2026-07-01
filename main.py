# main.py

# Import ระบบต่างๆ ที่เพื่อนในกลุ่มเขียนไว้
from features import recruitment, database, finance, missions

# ข้อมูลตั้งต้น (Initial Data) สำหรับเอาไว้เทสต์โปรแกรม
family_members = [
    {"name": "Tony", "age": 35, "role": "Boss", "power": 10, "money": 5000000},
    {"name": "Luigi", "age": 28, "role": "Hitman", "power": 8, "money": 150000},
    {"name": "Mario", "age": 22, "role": "Slave", "power": 4, "money": 500}
]

# main.py

while True:
    print("\n========== MAFIA MANAGEMENT SYSTEM ==========")
    print("1. HR")
    print("2. Database")
    print("3. Finance")
    print("4. Missions")
    print("0. Exit")

    choice = input("เลือกเมนู : ")

    match choice:
        case "1":
            while True:
                print("\n----- HR -----")
                print("1. Add Member")
                print("2. Remove Member")
                print("0. Back")

                hr_choice = input("เลือกเมนู : ")

                match hr_choice:
                    case "1":
                        recruitment.add_member(family_members)
                    case "2":
                        recruitment.remove_member(family_members)
                    case "0":
                        break
                    case _:
                        print("กรุณาเลือกใหม่")

        case "2":
            while True:
                print("\n----- Database -----")
                print("1. Show Members")
                print("2. Search Member")
                print("0. Back")

                db_choice = input("เลือกเมนู : ")

                match db_choice:
                    case "1":
                        database.show_members(family_members)
                    case "2":
                        database.search_member(family_members)
                    case "0":
                        break
                    case _:
                        print("กรุณาเลือกใหม่")

        case "3":
            while True:
                print("\n----- Finance -----")
                print("1. Total Income")
                print("2. Calculate Tax (15%)")
                print("0. Back")

                finance_choice = input("เลือกเมนู : ")

                match finance_choice:
                    case "1":
                        total_income()
                    case "2":
                        calculate_tax()
                    case "0":
                        break
                    case _:
                        print("กรุณาเลือกใหม่")

        case "4":
            while True:
                print("\n----- Missions -----")
                print("1. Send Mission")
                print("0. Back")

                mission_choice = input("เลือกเมนู : ")

                match mission_choice:
                    case "1":
                        send_mission()
                    case "0":
                        break
                    case _:
                        print("กรุณาเลือกใหม่")

        case "0":
            print("ปิดระบบ...")
            break

        case _:
            print("กรุณาเลือกเมนูให้ถูกต้อง")
