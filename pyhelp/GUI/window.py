import tkinter as tk
from .create_file_gui import create_file_gui
from .remove_file_gui import remove_file_gui
from .init_file_gui import init_file_gui
def start_GUI():
    window = tk.Tk()
    window.title("PyHelp - Python 文件快速管理工具")
    window.geometry("500x300")
    menu = tk.Menu(window)
    filemenu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="文件",menu = filemenu)
    filemenu.add_command(label="新建文件", command=create_file_gui)
    filemenu.add_command(label="删除文件", command=remove_file_gui)
    filemenu.add_command(label="初始化文件", command=init_file_gui)
    window.config(menu=menu)
    window.mainloop()
