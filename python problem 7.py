'''Author = Nitesh
    Date = 14 May 2021
    Topic = Create a local search engine
'''


sentences = ["this is good", "python is good",
             "python is not python snake", "Rohan is a python developer"]

# empty list filled during process
dict1 = {}
l = []
keys = []
storage = []
s = 1

# query taken from the user
query = (input("Please input your query string:\n").lower()).split(' ')

# adding data in dictionary
for i in query:
    for j in sentences:
        if i in j.lower():
            matches = j.count(i)

            if j in dict1:
                found = dict1[j]+matches
                dict1[j] = found
            else:
                dict1[j] = matches

# adding data to list
for x in dict1:
    l.append(dict1[x])
    keys.append(x)

# apstracting data from list and dict

print(f"\n{len(keys)} results found:\n")
for t in range(len(keys)):
    max_value = max(l)
    for y in keys:
        if dict1[y] == max_value:
            if y not in storage:
                storage.append(y)
                print(f"{s}. {y}")
                s += 1

    l.remove(max_value)

if len(keys) == 0:
    print('sorry! your query not found')
