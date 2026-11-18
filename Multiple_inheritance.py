


class Animal():
    def eat(self):
        print("Animal eat")

class Walker():
    def walk(self):
        print("walks")

class Dog(Animal,Walker):
    def bark (self):
        print("bark")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()

print("*********************************************************************************")

class Camera():
    def take_photo(self):
        print("Capture Photo")

class Call:
    def make_call(self):
        print("Calling friend")

class Smart_phone(Camera,Call):
    def internet(self):
        print("Browsing Internet")

phone = Smart_phone()
phone.take_photo()
phone.make_call()
phone.internet()


print("*********************************************************************************")


class Mediaplayer():
    def play_video(self):
        print("playing videos")


class InternetDevice():
    def connect_wifi(self):
        print("connect to wifi")

class SmartTV(Mediaplayer,InternetDevice):
    def change_channel(self):
        print("changing TV channel")

tv = SmartTV()
tv.play_video()
tv.connect_wifi()
tv.change_channel() 