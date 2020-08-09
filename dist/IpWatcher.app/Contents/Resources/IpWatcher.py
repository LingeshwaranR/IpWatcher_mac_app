import threading
from requests import get
from tkinter import *
import time
import os
from rumps import *
import clipboard
import tkinter as tk

# CONSTANTS
TITLE = 'IpWatcher'
SUBTITLE = 'Your Ip has been changed'
SOUND = '/System/Library/Sounds/Submarine.aiff'
ICON = '/Users/lingesh/PycharmProjects/WeekendBuff/icons/icon.png'
FILE = 'file:/Users/lingesh/PycharmProjects/WeekendBuff/ip.txt'

MENU_ICON = "/Users/lingesh/PycharmProjects/WeekendBuff/icons/green_icon.png"

# GLOBAL VARIABLE
public_ip_existing = ' '
watching = True


# def on_closing():
#     print("Closed")
#     rumps.quit_application()
#     window.destroy()
#
#
# window = Tk()
# window.withdraw()
# window.protocol("WM_DELETE_WINDOW", on_closing)


def get_ip():
    threading.Timer(5.0, get_ip).start()
    if watching:
        global public_ip_existing
        try:
            public_ip = get('https://api.ipify.org').text
            if public_ip_existing != public_ip:
                print(public_ip_existing, "->", public_ip, " Ip Changed")
                public_ip_existing = public_ip
                # notify(TITLE,
                #        SUBTITLE,
                #        public_ip_existing,
                #        SOUND,
                #        ICON,
                #        FILE)
                rumps.notification(title=TITLE,
                                   subtitle=SUBTITLE,
                                   message=public_ip_existing,
                                   sound=True,
                                   )
            else:
                print(public_ip_existing, "/", public_ip, ' No Change')

                f = open("/Users/lingesh/PycharmProjects/WeekendBuff/ip.txt", "w")
                f.write(f"Ip : {public_ip_existing}")
                f.close()
                time.sleep(5)

        except EXCEPTION as e:
            print("No Internet Connection")
            time.sleep(5)


def notify(title, subtitle, message, sound, icon, file):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    sd = '-sound {!r}'.format(sound)
    i = ' -appIcon {!r}'.format(icon)
    f = '-open {!r}'.format(file)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, sd, i, f])))


# def about_window():
#     print("entered")
#     window.deiconify()
#     window.geometry('350x200')


class IpWatcherApp(rumps.App):
    def __init__(self):
        super(IpWatcherApp, self).__init__("IpWatcher")
        self.menu = [rumps.MenuItem('IpWatcher is Running',
                                    icon=MENU_ICON),
                     None,
                     "About IpWatcher",
                     "Copy Public IP              📋",
                     "Turn Off Watching",
                     None,
                     "Quit IpWatcher"]
        self.icon = ICON
        self.quit_button = None

    @rumps.clicked("About IpWatcher")
    def about_ipwatcher(self, _):
        rumps.alert(title=TITLE,
                    message="IpWatcher keep watching your Public Ip Address and notifies you when it gets changed!",
                    icon_path=ICON
                    )
    @rumps.clicked("Turn Off Watching")
    def on_off_ipwatcher(self, sender):
        global watching, MENU_ICON
        sender.title = 'Turn Off Watching' if sender.title == 'Turn On Watching' else 'Turn On Watching'
        if sender.title == 'Turn On Watching':
            watching = False
        else:
            watching = True
        if watching:
            msg = "IpWatcher has started Watching"
            MENU_ICON = "/Users/lingesh/PycharmProjects/WeekendBuff/icons/green_icon.png"
            title = "IpWatcher is Running"
        else:
            msg = "IpWatcher has stopped Watching"
            MENU_ICON = "/Users/lingesh/PycharmProjects/WeekendBuff/icons/grey_icon.png"
            title = "IpWatcher is Paused"

        rumps.notification(title=TITLE,
                           subtitle="",
                           message=msg,
                           sound=True
                           )
        # notify(TITLE,
        #        "",
        #        msg,
        #        SOUND,
        #        ICON,
        #        FILE)
        self.menu["IpWatcher is Running"].icon = MENU_ICON
        self.menu["IpWatcher is Running"].title = title

    @rumps.clicked("Quit IpWatcher")
    def quit_ipwatcher(self, _):
        rumps.quit_application()

    @rumps.clicked("Copy Public IP              📋")
    def copy_ip(self, sender):
        # sender.state = not sender.state
        public_ip = get('https://api.ipify.org').text
        clipboard.copy(public_ip)

    # @rumps.clicked("Say hi")
    # def sayhi(self, _):
    #     rumps.notification(title=TITLE,
    #                        subtitle=SUBTITLE,
    #                        message="hi!!1",
    #                        sound=True,
    #                        icon=ICON,
    #                        )
        # notify(TITLE,
        #        SUBTITLE,
        #        "public_ip_existing",
        #        SOUND,
        #        ICON,
        #        FILE)


if __name__ == "__main__":
    get_ip()
    IpWatcherApp().run()
