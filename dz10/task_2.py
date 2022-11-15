def check_ints_list(a):
    try:
        for i in a:
            i = int(i)
        if len(set(a)) == len(a):
            print("Yes, you have list of unique numbers")
        else:
            print("No, your list contains duplicates")
    except ValueError as ex:
        print("Yo, your set of ints includes some sht")


numbers = (1, 2, 3, 4, 4, 4)
check_ints_list(numbers)

