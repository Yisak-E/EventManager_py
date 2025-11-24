import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1200x700")
        self.title("Event Manager")
        self.configure(background="dark gray")










if __name__ == "__main__":
    app = App()
    app.mainloop()
    app.destroy()

