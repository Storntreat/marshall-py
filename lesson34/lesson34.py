# Lesson 34

a_string = input()
string_list = a_string.split(",")
for i in range(len(string_list)):
    string_list[i] = int(string_list[i])
#or for value in a_string.split(","):
#new_list.append(value)
print(string_list)