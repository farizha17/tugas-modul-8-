import tkinter as tk

from controllers.auth_controller import AuthController


root = tk.Tk()

AuthController(root)

root.mainloop()