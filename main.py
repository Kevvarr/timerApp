# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import threading
from tkinter import Tk as tk
from tkinter import Label as label
from tkinter import Entry as entry
from tkinter import Frame as frame
from tkinter import Button as button

class MainWindow(tk):
    def __init__(self):
        super().__init__()
        self.geometry("140x80")
        self.config(bg="black")
        self.createFrameButtons().pack(expand=True)

    def createFrameButtons(self) -> frame:
        self.frameMain = frame(self)
        self.btnStartTimer = button(self.frameMain, text="Start Timer", command=self.onDownLoadButtonClicked())
        self.btnText = button(self.frameMain, text="Start Text")
        self.lblStatus = label(self.frameMain)
        #lol
        self.btnStartTimer.pack()
        self.btnText.pack()
        self.lblStatus.pack()

        return self.frameMain

    def onDownLoadButtonClicked(self):
        thrd1 = threading.Thread(target=self.download, args=("elpepe.jpg", ) ,daemon=True)
        thrd1.start()
    def download(self, fileName: str):
        for progress in range(1,10):
            time.sleep(1)

if __name__ == "__main__":
    mainWindow = MainWindow()
    mainWindow.mainloop()