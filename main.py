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
from queue import Queue
from enum import Enum, auto

class TicketPurpose(Enum):
    UPDATE_PROGRESS_TEST = auto()

class Ticket:
    def __init__(self,
                 ticket_type: TicketPurpose,
                 ticket_value: str):
        self.ticket_type = ticket_type
        self.ticket_value = ticket_value

class MainWindow(tk):
    def __init__(self):
        super().__init__()
        self.geometry("140x80")
        self.config(bg="black")
        self.createFrameButtons().pack(expand=True)
        self.bind("<<CheckQueue>>", self.check_queue)

        self.queue_message = Queue()

    def check_queue(self, event):
        "Read the queue"
        msg: Ticket
        msg = self.queue_message.get()

        if msg.ticket_type == TicketPurpose.UPDATE_PROGRESS_TEST:
            self.lblStatus.configure(text=msg.ticket_value)
    def createFrameButtons(self) -> frame:
        self.frameMain = frame(self)
        self.btnStartTimer = button(self.frameMain, text="Start Timer", command=self.onDownLoadButtonClicked)
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
        return
    def download(self, fileName: str):
        'Download in separate thread'
        for progress in range(1,10):
            ticket = Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS_TEST,
                            ticket_value=f"Downloading {fileName}...{progress}")
            self.queue_message.put(ticket)
            self.event_generate("<<CheckQueue>>")

            '26:56'
            time.sleep(1)

if __name__ == "__main__":
    mainWindow = MainWindow()
    mainWindow.mainloop()