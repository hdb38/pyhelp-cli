import tkinter as tk
from subprocess import run
def init_file_gui():
    window2 = tk.Tk()
    window2.title("初始化文件")
    window2.geometry("500x300")
    l = tk.Label(window2, text="文件名:")
    l.place(x=50, y=50)
    e = tk.Entry(window2)
    e.place(x=150, y=50)
    l2 = tk.Label(window2, text="拓展名:")
    l2.place(x=50, y=100)
    e2 = tk.Entry(window2)
    e2.place(x=150, y=100)
    l3 = tk.Label(window2, text="初始化模板:")
    l3.place(x=50, y=150)
    e3 = tk.Entry(window2)
    e3.place(x=150, y=150)
    def get():
        run(["pyhelp","init-file","-ifn",e.get(), "-ifen", e2.get(), "-im", e3.get()])
    b = tk.Button(window2, text="写好文件名和拓展名后点我", command=get)
    b.place(x=50, y=200)
    window2.mainloop()

