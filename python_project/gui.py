from tkinter import Label, Button, Toplevel, Frame, Tk, font, LEFT


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["highlightbackground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['highlightbackground'] = self['activeforeground']

    def on_leave(self, e):
        self['highlightbackground'] = self.defaultBackground


class PlayFrame(Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)
        w, h = original.root.winfo_screenwidth(), original.root.winfo_screenheight()
        self.geometry("{0}x{1}+0+0".format(w, h))
        self.title("Piano Player")
        self.configure(bg='dim grey')

        menu_button = HoverButton(self, text="CLOSE", highlightbackground='dim grey',
                                  activeforeground='light grey', height=h //400, width=w // 140, fg='brown4',
                                  font=('Trattatello', 20), pady=10, padx=10, command=self.on_close)
        menu_button.pack()

    def on_close(self):
        self.destroy()
        self.original_frame.show()


class PianoApp(object):

    def __init__(self, parent, text_path='welcome.txt'):
        self.root = parent
        self.root.title("Piano Player")
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("{0}x{1}+0+0".format(w, h))
        self.root.configure(bg='dim grey')
        self.frame = Frame(parent)
        self.frame.configure(bg='dim grey')
        self.frame.pack()

        with open(text_path, 'r') as file:
            text = file.read()

        label = Label(self.frame, text=text, bg='dim grey', font=('Trattatello', 30), pady=15)
        label.pack()

        play_button = HoverButton(self.frame, text="PLAY", highlightbackground='dim grey',
                                  activeforeground='light grey', height=h//220, width=w//40, fg='brown4',
                                  font=('Trattatello', 40), pady=10, padx=10, command=self.open_frame)
        play_button.pack()

        exit_button = HoverButton(self.frame, text="EXIT", highlightbackground='dim grey',
                                  activeforeground='light grey', height=h//220, width=w//40, fg='brown4',
                                  font=('Trattatello', 40), pady=10, padx=10, command=self.root.quit)
        exit_button.pack()

    def hide(self):
        self.root.withdraw()

    def open_frame(self):
        self.hide()
        play_frame = PlayFrame(self)

    def show(self):
        self.root.update()
        self.root.deiconify()

if __name__ == "__main__":
    root = Tk()
    app = PianoApp(root)
    root.mainloop()
