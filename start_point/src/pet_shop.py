# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, money):
    pet_shop["admin"]["total_cash"] += money

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,sold):
    pet_shop["admin"]["pets_sold"] += sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop,pet_breed):
    animal_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            animal_list.append(pet)
    return animal_list

def find_pet_by_name(pet_shop,pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop,pet_name):
    index_number = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            break
        else:
            index_number += 1
    del(pet_shop["pets"][index_number])

def add_pet_to_stock(pet_shop,pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(cust):
    return cust["cash"]

def remove_customer_cash(cust,cash):
    cust["cash"] -= cash 

def get_customer_pet_count(cust):
    return len(cust["pets"])

def add_pet_to_customer(cust,new_pet):
    cust["pets"].append(new_pet)


def customer_can_afford_pet(cust,pet):
    return cust["cash"] >= pet["price"]





def sell_pet_to_customer(pet_shop,pet,cust):
    if pet == None:
        print(f'Sorry {cust["name"]} but this animal doesnt exist')
    elif customer_can_afford_pet(cust,pet) == False:
        print(f"Sorry {cust['name']} but you currently have insufficient funds")

    else:
        add_pet_to_customer(cust,pet)
        increase_pets_sold(pet_shop,len([pet]))
        remove_customer_cash(cust,pet["price"])
        add_or_remove_cash(pet_shop,pet["price"])

