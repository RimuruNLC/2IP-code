import urllib.request
import json
import tabulate
list1 = []
dict1 = {}
def proverk(a, b):
    for i in a:
        if type(a[i]) != dict and type(a[i]) != list:
            if len(dict1[i]) > 0:
                dict1[i+"_2"].append(a[i])
                continue
            dict1[i].append(a[i])
        elif type(a[i]) == list:
            proverk(a[i][0], True)
        else:
            proverk(a[i], True)
def proverk_keys(a):
    for i in a:
        if type(a[i]) == dict:
            proverk_keys(a[i])
        elif type(a[i]) == list:
            print(a[i][0])
            proverk_keys(a[i][0])
        else:
            if i in dict1:
                dict1[i+"_2"] = []
            dict1[i] = []
            list1.append(i)


a = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat=55.30&lon=46.25&exclude=alerts&appid=431db0af393c24ef0b144e28418c63a4")
b = json.load(a)
print(b)
proverk_keys(b)
proverk(b,False)
tablica = tabulate.tabulate(dict1, tablefmt="grid", headers="keys")
print(tablica)
