try:
    import Tkinter as tk
except:
    import tkinter as tk

a = []

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="메추리알", font=('Helvetica', 70, "bold")).pack(side="top", fill="x", pady=70)
        tk.Label(self, text="메뉴 추천 리알?", font=('Helvetica', 20)).pack(side="top", fill="x")
        tk.Button(self, text="메뉴 추천 받기",
                  command=lambda: master.switch_frame(PageOne), width=20, height=3).pack(pady=20),
        tk.Button(self, text="메뉴 추천하기",
                  command=lambda: master.switch_frame(PageTwo), width=20, height=3).pack()


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="음식 추천을 위한 설문", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=20)
        tk.Button(self, )
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1000x600")
    app.title("메추리알")
    app.mainloop()