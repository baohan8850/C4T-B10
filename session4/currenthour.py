import datetime
import pyglet
datetime.datetime.now()
print("bay gio la:",datetime.datetime.now().strftime("%H:%M"))
alarmClock = input("gio ban muon hen: ")
while True:
    currentTime = datetime.datetime.now().strftime("%H:%M")
    if alarmClock == currentTime:
        print("bao thuc")
        

        music = pyglet.resource.media('crowd-cheering.mp3')
        music.play()

        pyglet.app.run()