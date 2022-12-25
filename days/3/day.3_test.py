s = "EwaldIsGay"
x = list(s)


list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10, 11]


set1 = (set(list1))
set2 = (set(list2))

new_list = list(set1.intersection(set2))

my_str = "A"

numbers = [ord(char) - 96 for char in my_str.lower()]

print([ord(char) for char in my_str])
