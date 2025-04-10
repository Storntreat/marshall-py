firstInput = input() 
inputArr = firstInput.split()
N = int(inputArr[0])
D = int(inputArr[1])
int_dict = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
answers_list = []
answers_dict = {}
for i in range(N-1,0,-1):
    if i % D == 0:
        i_string = str(i)
        answers_list.append(i)
        for value in i_string:
            int_dict[value] += 1
        max_value = max(int_dict.values())
        answers_dict[i] = max_value
        for value in "0123456789":
            int_dict[value] = 0
values_list = list(answers_dict.values())
max_repeat = max(values_list)
answer_index = values_list.index(max_repeat)
print(answers_list[answer_index])

