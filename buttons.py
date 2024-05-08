import tkinter as tk

#Создание окна
root = tk.Tk()
#Даём название окна
root.title("Приветствие")

#Выводится сообщение в окне
Label = tk.Label(root, text="введи своё имя")
Label.pack()

#Создание поля для ввода
entry = tk.Entry(root)
#Расположение поля для ввода
entry.pack()

button = tk.Button(root,text="нажми", command=user_names)
button.pack()

root.mainloop()