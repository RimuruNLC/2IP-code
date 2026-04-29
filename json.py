import json
import urllib.request
import tabulate
list1 = []
dict1 = {}
def proverk(a, b):
    for i in a:
        if type(a[i]) != dict:
            if i == "name":
                if b == True:
                    dict1['company_name'].append(a[i])
                    continue
            dict1[i].append(a[i])
        else:
            proverk(a[i], True)
def proverk_keys(a):
    for i in a.keys():
        if type(a[i]) == dict:
            proverk_keys(a[i])
        else:
            if i == "name":
                if i in dict1:
                    dict1["company_"+i] = []

            dict1[i] = []
            list1.append(i)


a = urllib.request.urlopen("https://jsonplaceholder.typicode.com/users")
b = json.load(a)
for i in b:
    proverk_keys(i)
for i in b:
    proverk(i,False)
tablica = tabulate.tabulate(dict1, tablefmt="grid", headers="keys")
print(tablica)
