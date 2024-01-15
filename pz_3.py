element_in_list = (input("Enter elements >>> ")).split()
element_in_list = [int(x) for x in element_in_list]

sum_element = sum(element_in_list)

average = sum_element / len(element_in_list)

print(f"Сумма элементов = {sum_element}")

print(f"Среднее арифметическое = {average}")