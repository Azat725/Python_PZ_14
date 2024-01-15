import string

text = input("Enter some text >>> ")

after_symbol = text.split(". " or "." or "? " or "?" or "! " or "!")
print(type(after_symbol))
print()

capitalize_text = []

for i in after_symbol:
    capitalize_text.append(i.strip().capitalize())
    
capitalize_text_str = ". ".join(capitalize_text)

print(capitalize_text_str)
print()

numbers_of_text = [int(i) for i in text if i.isdigit()]
numbers = len(numbers_of_text)
print(numbers)
print()

symbol_in_text = [",", ".", "?", ":", "!"]

s = sum(k in symbol_in_text for k in text)

print(s)
print()

alarm_in_text = text.count("!")

print(alarm_in_text)