import tkinter as tk
# запрос на ввод имени пользователя
def user_names():
    user_name = entry.get()
    Label.config(text=f"Привет, {user_name}!")