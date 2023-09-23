def menu():
    display = """
    Please select from the menu.
    A or a to add customer.
    L or l to list customers.
    Q or q to exit.
    """
    select = input(display)
    select = select.upper()
    if select == "A":
        addcustomer()
    elif select == "L":
        listcustomers()
    elif select == "Q":
        print("Bye!")
        return
    else:
        print("Please select a valid function")
    menu()


def listcustomers():
    print("***in list customer function***")

def addcustomer():
    print("***in add customer function***")


menu()