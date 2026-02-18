list1 =[
    ["Москва",-21,-10,-11,-11,-11,-4,-3],
    ["Санкт-Перербург",-16,-16,-12,-12,-7,-11,-12],
    ["Нижний новгород",-24,-16,-11,-14,-14,-7,-7],
    ["Шумерля",-23,-17,-10,-14,-16,-11,-9],
    ["Чебоксары",-21,-21,-11,-15,-15,-11,-10],
    ["Верхоянск",-49,-50,-46,-44,-44,-32,-32],
]
list_sr_temp_pokaz = []
list_sr_temp = []
for i in range(len(list1)):
    s = 0
    for j in range(1,len(list1[i])):
        s += list1[i][j]
    s /=7
    list_sr_temp_pokaz.append(f"средняя температура города - \"{list1[i][0]}\" - равна - \"{int(s)}\"")
    list_sr_temp.append(int(s))
for i in list_sr_temp_pokaz:
    print(i)
min_temp = min(list_sr_temp)
max_temp = max(list_sr_temp)
print(f"Максимальная средняя температура - {max_temp}\nМинимальная средняя температура - {min_temp}")
