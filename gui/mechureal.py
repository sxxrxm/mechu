try:
    import Tkinter as tk
except:
    import tkinter as tk

ftemp = tk.IntVar()
fspicy = tk.IntVar()
fjong = tk.IntVar()
fsoup = tk.IntVar()
fmeat = tk.IntVar()
fcoun = tk.IntVar()
fcal = tk.IntVar()
fpric = tk.IntVar()

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
        egg = tk.PhotoImage(file='egg.png')
        tk.Label(self, image=egg).pack(side="top")
        tk.Label(self, text="메추리알", font=('Helvetica', 70, "bold")).pack(side="top", fill="x", pady=20)
        tk.Button(self, text="메뉴 추천 받기",
                  command=lambda: master.switch_frame(polls1), width=20, height=3).pack(pady=20),
        tk.Button(self, text="메뉴 추천하기",
                  command=lambda: master.switch_frame(PageTwo), width=20, height=3).pack()


class polls1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="음식 추천을 위한 설문", font=('Helvetica', 20, "bold")).pack(side="top", fill="x", pady=20)
        # ftemp = tk.IntVar()
        # fspicy = tk.IntVar()
        # fjong = tk.IntVar()

        tk.Label(self, text="원하는 음식의 온도는?", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=20)

        radio1 = tk.Radiobutton(self, text="뜨거운 음식", value=0, variable=ftemp)
        radio1.pack()

        radio2 = tk.Radiobutton(self, text="차가운 음식", value=1, variable=ftemp)
        radio2.pack()

        radio3 = tk.Radiobutton(self, text="상관 없어요", value=2, variable=ftemp)
        radio3.pack()

        tk.Label(self, text="원하는 음식의 맵기?", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=20)

        radio4 = tk.Radiobutton(self, text="매운 음식", value=0, variable=fspicy)
        radio4.pack()

        radio5 = tk.Radiobutton(self, text="안 매운 음식", value=1, variable=fspicy)
        radio5.pack()

        radio6 = tk.Radiobutton(self, text="상관 없어요", value=2, variable=fspicy)
        radio6.pack()

        tk.Label(self, text="원하는 음식의 종류?", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=20)

        tk.Radiobutton(self, text="밥", value=0, variable=fjong).pack()
        tk.Radiobutton(self, text="면", value=1, variable=fjong).pack()
        tk.Radiobutton(self, text="빵", value=2, variable=fjong).pack()
        tk.Radiobutton(self, text="상관 없어요", value=3, variable=fjong).pack()

        tk.Button(self, text="다음 페이지",
                      command=lambda: master.switch_frame(polls2), width=10, height=3).pack(pady=10)


class polls2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # fsoup = tk.IntVar()
        # fmeat = tk.IntVar()
        # fcoun = tk.IntVar()
        tk.Label(self, text="음식 추천을 위한 설문", font=('Helvetica', 20, "bold")).pack(side="top", fill="x", pady=20)

        tk.Label(self, text="국물 유무?", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=20)

        tk.Radiobutton(self, text="국물 좋아요", value=0, variable=fsoup).pack()
        tk.Radiobutton(self, text="국물 싫어요", value=1, variable=fsoup).pack()
        tk.Radiobutton(self, text="상관 없어요", value=2, variable=fsoup).pack()

        tk.Label(self, text="고기 종류?", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=20)

        tk.Radiobutton(self, text="고기", value=0, variable=fmeat).pack()
        tk.Radiobutton(self, text="생선", value=1, variable=fmeat).pack()
        tk.Radiobutton(self, text="상관 없어요", value=2, variable=fmeat).pack()

        tk.Label(self, text="원하는 나라의 음식?", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=20)

        tk.Radiobutton(self, text="한식", value=0, variable=fcoun).pack()
        tk.Radiobutton(self, text="중식", value=1, variable=fcoun).pack()
        tk.Radiobutton(self, text="일식", value=2, variable=fcoun).pack()
        tk.Radiobutton(self, text="그 외(베트남 등)", value=3, variable=fcoun).pack()
        tk.Radiobutton(self, text="상관 없어요", value=4, variable=fcoun).pack()

        tk.Button(self, text="다음 페이지",
                  command=lambda: master.switch_frame(polls3)).pack()

class polls3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # fcal = tk.IntVar()
        # fpric = tk.IntVar()
        tk.Label(self, text="음식 추천을 위한 설문", font=('Helvetica', 20, "bold")).pack(side="top", fill="x", pady=20)

        tk.Label(self, text="어느 정도의 칼로리를 원하시나요?", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=20)

        tk.Radiobutton(self, text="낮음", value=0, variable=fcal).pack()
        tk.Radiobutton(self, text="중간", value=1, variable=fcal).pack()
        tk.Radiobutton(self, text="높음", value=2, variable=fcal).pack()
        tk.Radiobutton(self, text="상관 없어요", value=3, variable=fcal).pack()

        tk.Label(self, text="어느 정도의 칼로리를 원하시나요?", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=20)

        tk.Radiobutton(self, text="낮음", value=0, variable=fpric).pack()
        tk.Radiobutton(self, text="중간", value=1, variable=fpric).pack()
        tk.Radiobutton(self, text="높음", value=2, variable=fpric).pack()
        tk.Radiobutton(self, text="상관 없어요", value=3, variable=fpric).pack()

        tk.Button(self, text="다음 페이지",
                  command=lambda: master.switch_frame(results)).pack()

class results(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1000x600")
    app.title("메추리알")
    app.mainloop()