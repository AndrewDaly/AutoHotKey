import pyautogui as pg
import tkinter as tk


class Example(tk.Frame):
    def move_mouse(self):
        pg.moveTo(self.x_axis, self.y_axis)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=100, height=100)

        self.label = tk.Label(self, text="last key pressed:  ", width=20)
        self.label.pack(fill="both", padx=10, pady=10)
        self.x_axis = 960
        self.y_axis = 540
        pg.moveTo(self.x_axis, self.y_axis)

        self.label.bind("<w>", self.on_wasd)
        self.label.bind("<a>", self.on_wasd)
        self.label.bind("<s>", self.on_wasd)
        self.label.bind("<d>", self.on_wasd)

        self.label.bind("<W>", self.on_wasd)
        self.label.bind("<A>", self.on_wasd)
        self.label.bind("<S>", self.on_wasd)
        self.label.bind("<D>", self.on_wasd)
        self.label.bind("<space>", self.on_wasd)

        # give keyboard focus to the label by default, and whenever
        # the user clicks on it
        self.label.focus_set()
        self.label.bind("<1>", lambda event: self.label.focus_set())

    def on_wasd(self, event):
        key_pressed = event.keysym
        print(key_pressed)
        self.label.configure(text="last key pressed: " + key_pressed)
        if key_pressed == 's':
            self.y_axis = self.y_axis + 15
            self.move_mouse()
            return
        if key_pressed == 'w':
            self.y_axis = self.y_axis - 15
            self.move_mouse()
            return
        if key_pressed == 'a':
            self.x_axis = self.x_axis - 15
            self.move_mouse()
            return
        if key_pressed == 'd':
            self.x_axis = self.x_axis + 15
            self.move_mouse()
            return
        if key_pressed == 'S':
            self.y_axis = self.y_axis + 80
            self.move_mouse()
            return
        if key_pressed == 'W':
            self.y_axis = self.y_axis - 80
            self.move_mouse()
            return
        if key_pressed == 'A':
            self.x_axis = self.x_axis - 80
            self.move_mouse()
            return
        if key_pressed == 'D':
            self.x_axis = self.x_axis + 80
            self.move_mouse()
            return
        if key_pressed == 'space':
            pg.click(self.x_axis, self.y_axis)


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
    pg.mouseInfo()
