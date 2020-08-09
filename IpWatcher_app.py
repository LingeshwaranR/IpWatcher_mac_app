from requests import get
from tkinter import *
import time
import os

# CONSTANTS
TITLE = 'IpWatcher'
SUBTITLE = 'Your Ip has been changed'
SOUND = '/System/Library/Sounds/Submarine.aiff'
ICON = '/Users/lingesh/PycharmProjects/WeekendBuff/icons/ipwatcher.icns'
FILE = 'file:/Users/lingesh/PycharmProjects/WeekendBuff/ip.txt'

while 1:

    try:
        # GLOBAL VARIABLE
        public_ip_existing = get('https://api.ipify.org').text + 'a'
        window = Tk()
        window.withdraw()


        # def notify(title, subtitle, text, sound): os.system(""" osascript -e 'display notification "{}" with title "{}"
        # subtitle "{}" sound name "{}"'""".format(text, title, subtitle, sound))

        def notify(title, subtitle, message, sound, icon, file):
            t = '-title {!r}'.format(title)
            s = '-subtitle {!r}'.format(subtitle)
            m = '-message {!r}'.format(message)
            sd = '-sound {!r}'.format(sound)
            i = ' -appIcon {!r}'.format(icon)
            f = '-open {!r}'.format(file)
            os.system('terminal-notifier {}'.format(' '.join([m, t, s, sd, i, f])))


        while 1:
            try:
                public_ip = get('https://api.ipify.org').text
                print(public_ip, "/", public_ip_existing)
                if public_ip_existing != public_ip:
                    public_ip_existing = public_ip_existing + public_ip
                    notify(TITLE,
                           SUBTITLE,
                           public_ip_existing,
                           SOUND,
                           ICON,
                           FILE)
                    f = open("/Users/lingesh/PycharmProjects/WeekendBuff/ip.txt", "w")
                    f.write(f"Ip : {public_ip_existing}")
                    f.close()

                window.update()
                time.sleep(5)
            except EXCEPTION as e:
                print(e)
                time.sleep(5)

    except EXCEPTION as e:
        print(e)
        print("No Internet Connection")
        time.sleep(5)
