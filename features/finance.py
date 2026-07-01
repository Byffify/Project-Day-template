def total_income(data):
    money = 0
    for i in data:
        money += i["money"]
    return money
    
def caculate_tax(data):
    tax = total_income(data) * 0.15
    money = total_income(data) - tax
    return money
    
