#1
mouth = int(input("Enter mouth number: "))

if mouth in [3, 4, 5]:
    print("Spring")
elif mouth in [6, 7, 8]:
    print("Summer")
elif mouth in [9, 10, 11]:
    print("Autumn")
elif mouth in [12, 1, 2]:
    print("Winter")
else:
    print("Exception")

#2
logged_in = True
has_items = True
has_address = True
total_purchase = 0
min_total = 0
is_first = False

if logged_in & has_items & has_address & total_purchase >= min_total and not is_first:
    print("Has sale")
else:
    print("LOL)))")

#3
number = int(input("Enter number: "))

if number in range(1, 101):
    print("In range")
    if number in [7, 13, 21]:
        print("Lucky")
else:
    print("LOL")