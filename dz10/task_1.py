month_list = {1 : "January", 2 : "February",3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}

def Month(a):
    try:
        a = int(a)
        print(month_list[a])
    except ValueError as ex:
        print("You should input int")
    except KeyError as ex:
        print("Nope!", "There is no", a, "month")


Month("sad")