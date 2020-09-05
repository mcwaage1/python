import tkinter as tk

import random

class Magic:
    def __init__(self):

        self.main_window = tk.Tk()

        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        self.descr_label = tk.Label(self.top_frame, text="Magic 8 ball says...")

        self.value = tk.StringVar()
        self.eightball = tk.Label(self.top_frame, textvariable=self.value)

        self.descr_label.pack(side="left")
        self.eightball.pack(side="left")
        
        self.again_button = tk.Button(self.bottom_frame, text="Again?", command=self.getAnswer)
        self.quit_button = tk.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.again_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def getAnswer(self):

        answerNumber = random.randint(1, 9)

        if answerNumber == 1:
            answer = 'It is certain'
        elif answerNumber == 2:
            answer = 'It is decidedly so'
        elif answerNumber == 3:
            answer = 'Yes'
        elif answerNumber == 4:
            answer = 'Reply hazy try again'
        elif answerNumber == 5:
            answer = 'Ask again later'
        elif answerNumber == 6:
            answer = 'Concentrate and ask again'
        elif answerNumber == 7:
            answer = 'My reply is no'
        elif answerNumber == 8:
            answer = 'Outlook not so good'
        elif answerNumber == 9:
            answer = 'Very doubtful'

        self.value.set(answer)
    
magic = Magic()