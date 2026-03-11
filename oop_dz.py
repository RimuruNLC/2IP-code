import numpy as np
list_temperature = []
list_humidity = []
list_snow_cover = []
list_wind_speed = []
list_atmospheric_pressure = []
class Weather:
    def __init__(self, temperature, humidity, snow_cover, wind_speed, atmospheric_pressure):
        self.temperature = temperature
        list_temperature.append(self.temperature)
        self.humidity = humidity
        list_humidity.append(self.humidity)
        self.snow_cover = snow_cover
        list_snow_cover.append(self.snow_cover)
        self.wind_speed = wind_speed
        list_wind_speed.append(self.wind_speed)
        self.atmospheric_pressure = atmospheric_pressure
        list_atmospheric_pressure.append(self.atmospheric_pressure)
day1 = Weather(4, 79,20, 4, 756)
day2 = Weather(4, 76,14, 6, 760)
day3 = Weather(6, 78,4, 3, 761)
day4 = Weather(6, 73,0, 3, 763)
tablica = np.array([list_temperature,list_humidity,list_snow_cover,list_wind_speed,list_atmospheric_pressure])
max = list(tablica.max(axis=1))
min = list(tablica.min(axis=1))
mean = list(tablica.mean(axis=1))
print(f"Максимальные величины. \nТемпература:{int(max[0])} градусов по цельсию\nВлажность: {int(max[1])}%\nСнежный покров: {int(max[2])} см\nСкорость ветра: {int(max[3])} м/с\nАтмосферное давление: {int(max[4])} мм рт. ст\n")
print(f"Минимальные величины. \nТемпература:{int(min[0])} градусов по цельсию\nВлажность: {int(min[1])}%\nСнежный покров: {int(min[2])} см\nСкорость ветра: {int(min[3])} м/с\nАтмосферное давление: {int(min[4])} мм рт. ст\n")
print(f"Средние величины. \nТемпература:{float(mean[0])} градусов по цельсию\nВлажность: {float(mean[1])}%\nСнежный покров: {float(mean[2])} см\nСкорость ветра: {float(mean[3])} м/с\nАтмосферное давление: {float(mean[4])} мм рт. ст\n")
list_uchenicov = ["Семаева", "Данилов","Денисов", "Паштынов", "Мешалкин", "Афоркин","Аня","Исправников"]
dict1 = [f"{i + 1} {list_uchenicov.pop(random.randint(0,len(list_uchenicov)-1))} {list_uchenicov.pop(random.randint(0,len(list_uchenicov)-1))}" for i in range(len(list_uchenicov)//2)]
print(dict1)
