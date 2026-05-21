import cv2
image = cv2.imread("1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(0,0))
for i in faces:
    cv2.rectangle(image, (i[0], i[1]), (i[0]+i[2], i[1]+i[3]), (255, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import tabulate as tb
class Material:
    def __init__(self, root):
        self.file = cv2.imread(root)
        self.table = {
            0:["Координаты","Количество"]
        }
    def print_material(self, Name_window):
        cv2.imshow(f"{Name_window}", self.file)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def get_coords_for_cascad(self,cascad):
        self.gray = cv2.cvtColor(self.file, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascad)
        coords = cascade.detectMultiScale(self.gray, scaleFactor=1.2, minNeighbors=5, minSize=(0, 0))
        self.table[f"{cascad}"] = [coords,len(coords)]
        return [[i[0], i[1],i[0]+i[2], i[1]+i[3]] for i in coords]
    def draw(self, coords):
        for i in coords:
            cv2.rectangle(self.file, (i[0], i[1]), (i[2], i[3]), (255, 255, 0), 2)
a = Material("img_1.png")
a.draw(a.get_coords_for_cascad("haarcascade_frontalface_default.xml"))
a.print_material("HEHEHHEHE")
