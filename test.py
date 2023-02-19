import tkinter
from tkinter import *
from tkinter import ttk
import scripts

if __name__ == '__main__':
    def makesmth():
        way_of_code = coding_type.get()
        x = entry.get()
        x2 = entry1.get()
        match way_of_code:
            case "Message to Bits":
                vvod_txt.delete(0, END)
                code = scripts.encrypt_msg(x, x2)
            case "Bits to Message":
                vvod_txt.delete(0, END)
                code = scripts.decrypt_msg(x, x2)
            case "Message to Bits(16base key)":
                vvod_txt.delete(0, END)
                code = scripts.encrypt_msg(x, x2)
            case "Bits to Message(16base key)":
                vvod_txt.delete(0, END)
                code = scripts.decrypt_msg(x, x2)
            case "Select an Option":
                print(1)

        vvod_txt.insert(0, code)


    def callback(*args):
        print(args)
        print("новый тип ввода")
    root = tkinter.Tk()  # создаем корневой объект - окно
    # root.overrideredirect(1)
    # root.lift()
    # root.attributes('-topmost',True)
    # root.after_idle(root.attributes,'-topmost',True)
    root.title("нож")  # устанавливаем заголовок окна
    w, h = 600, 600
    # root.geometry(f"{w}x{h}+{(root.winfo_screenwidth()-w)//2}+{(root.winfo_screenheight()-h)//2}")
    root.geometry(f"{w}x{h}")
    # root.attributes("-fullscreen", True)
    entry = ttk.Entry()
    entry.pack()
    entry.place(x=450, y=0)

    label2 = ttk.Label(text="Введите ваше замечателное значение", font=("Arial", 18))
    label2.pack()
    label2.place(x=0, y=0)

    # scrollbar = tkinter.Scrollbar(orient="horizontal")
    entry1 = ttk.Entry()  # xscrollcommand=scrollbar.set
    entry1.pack()
    entry1.place(x=450, y=30)
    # scrollbar.pack(fill="x")
    # scrollbar.config(command=entry1.xview)

    label21 = ttk.Label(text="Введите ваш замечательный ключ", font=("Arial", 18))
    label21.pack()
    label21.place(x=0, y=30)

    btn = ttk.Button(text="вычислить", command=makesmth)
    btn.pack()
    btn.place(x=0, y=60)

    options_list = ["Message to Bits", "Bits to Message", "Option 3", "Option 4"]
    coding_type = tkinter.StringVar(root)
    coding_type.set("Select an Option")
    coding_type.trace("w", callback)
    question_menu = tkinter.OptionMenu(root, coding_type, *options_list)
    question_menu.pack()
    question_menu.place(x=450, y=60)

    vvod_txt = ttk.Entry()
    vvod_txt.pack()
    vvod_txt.place(x=0, y=90)

    label_text = ttk.Label(text="", font=("Arial", 18))
    label_text.pack()
    label_text.place(x=0, y=90)

    label = ttk.Label(text="СУПЕР-ПУПЕР ПРОГРАММА СДЕЛАНА МНОЮ", font=("Arial", 32), background="#FFCDD2",
                      foreground="#B71C1C", padding=8)
    label.pack()  # создаем текстовую метку
    label.place(x=0, y=120)

    root.mainloop()
