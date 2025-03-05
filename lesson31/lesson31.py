# Lesson 31
a_string = input()
b_string = input()
a_list = list(a_string)
b_list = list(b_string)
a_list.sort()
b_list.sort()
print(a_list)
print(b_list)
if a_list == b_list:
    print("Anagrams")
else:
    print("Not Anagrams")