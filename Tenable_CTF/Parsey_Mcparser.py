#!/usr/bin/python3

# Get the names depending of a group name.
# You can use this format: Black|+++,Bellhomes LLC.,["age":39, "user_name":"Reid Jolley", "Group":"Black"],+++,Greek Ideas,["age":63, "user_name":"Lucius Chadwell", "Group":"Green"],["age":63, "user_name":"Cary Rizzuto", "Group":"Black"],["age":28, "user_name":"Shoshana Bickett", "Group":"Yellow"],["age":69, "user_name":"Madeleine Swallow", "Group":"Green"],["age":41, "user_name":"Buddy Etter", "Group":"Black"],+++,God fire,["age":26, "user_name":"Carlene Caulder", "Group":"Green"],["age":43, "user_name":"Napoleon Peay", "Group":"Purple"],["age":44, "user_name":"Noemi Constant", "Group":"Green"]
# STDOUT example: ['Reid Jolley', 'Cary Rizzuto', 'Buddy Etter']
# In this specific challenge I used this solution because the name was ever before group.
def ParseNamesByGroup(blob, group_name):
    comillas = blob.split("\"")
    lis = []
    for i in range(len(comillas)):
        if comillas[i] == group_name:
            lis.append(comillas[i-4])
    return lis


data = raw_input()
group_name = data.split('|')[0]
blob = data.split('|')[1]
result_names_list = ParseNamesByGroup(blob, group_name)
print (result_names_list)
