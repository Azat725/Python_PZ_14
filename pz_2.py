user_list = input("Enter list >>> ")
element_in_list = input("Enter element in the list >>> ")

if element_in_list in user_list:
    valume = user_list.count(element_in_list)
    print(valume)
