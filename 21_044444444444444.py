import matplotlib.pyplot as plt
import numpy as np
nazv = ["Нижегородская область","Марий Эл","Татарстан","Мордовия","Ульяновская область"]
znach = np.array([3039421,666202,4019606,758895,1165334])
coord = [0.15,0,0,0,0]
plt.pie(znach,labels=nazv, explode=coord, colors=["lightgrey","indigo","salmon","yellow","palegreen"],autopct="%.2f%%")
plt.axis('equal')
plt.show()
