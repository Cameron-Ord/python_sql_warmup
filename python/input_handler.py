def option():

    option_input = input("enter input:")
    
    if(option_input == "1"):
        return option_input
    elif(option_input == "2"):
        return option_input
    elif(option_input == "3"):
        return option_input
    else:
        print("oops")


def sales():
    sales_opt = input("enter name:")

    return sales_opt


def item():
    
    item_name = input("enter item name:")

    return item_name
    

def item_price():

    item_price = input("enter price")
    item_price = int(item_price)
    return item_price
    

def per_id():
    id = input("enter ID:")
    id = int(id)
    return id


def item_id():
    item_id = input("enter item ID:")
    item_id = int(item_id)
    return item_id