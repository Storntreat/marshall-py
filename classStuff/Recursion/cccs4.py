target = int(input())
clubs = int(input())
clubs_list = []
clubs_dict = {}
for value in range(len(clubs)):
    clubs_list.append(int(input()))
clubs_list.sort()
for i in range(len(clubs)):
    clubs_dict[i] = clubs_list[i]

def roberta(target, dict_clubs):
    answer = dict_clubs.copy()
    if target in list_clubs:
        return 1
    elif target < min(dict_clubs):
        return -1
 #   else: 
       # for i in range(max(dict_clubs), target+1):
         #   answer[i] = answer[]

#tabulaization
# in an array, table all indexes to get to the end
# track minimums for each index








    
def stairsDict(steps):
    answer = {0:0,1:1,2:2}
    
    if steps in answer:
        return answer[steps]
    else:
        for i in range (3,steps+1):
            answer[i] = answer[i-1] + answer[i-2]
        return answer[steps]

