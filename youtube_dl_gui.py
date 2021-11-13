from __future__ import unicode_literals
import threading
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
#import youtube_dl
import yt_dlp as youtube_dl
import option_dict


OPTION_DICT = option_dict.OPTION_DICT


class App(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.is_processing = False

        master.protocol("WM_DELETE_WINDOW", lambda:self.close(master))
        master.title("youtube-dl")
        master.geometry("300x200")

        self.create_widgets()
        self.pack(expand=True, fill=tkinter.BOTH)

        self.grid_columnconfigure(1, weight=1)

        for num in range(4):
            self.rowconfigure(num, weight=1)

    def create_widgets(self):
        self.label0 = ttk.Label(self, text="URL:")
        self.label0.grid(column=0, row=0, padx=10, pady=10, sticky="e")

        self.entry = ttk.Entry(self)
        self.entry.grid(column=1, row=0, padx=10, pady=10, sticky="we")

        self.label1 = ttk.Label(self, text="オプション:")
        self.label1.grid(column=0, row=1, padx=10, pady=10, sticky="e")

        self.string_var0 = tkinter.StringVar()

        self.combox = ttk.Combobox(self, textvariable=self.string_var0, values=list(OPTION_DICT.keys()))
        self.combox.set(list(OPTION_DICT.keys())[0])
        self.combox.grid(column=1, row=1, padx=10, pady=10, sticky="we")

        self.label2 = ttk.Label(self, text="保存先:")
        self.label2.grid(column=0, row=2, padx=10, pady=10, sticky="e")

        self.string_var1 = tkinter.StringVar(value="選択")

        self.button0 = ttk.Button(self, textvariable=self.string_var1, command=self.select_dir)
        self.button0.grid(column=1, row=2, padx=10, pady=10, sticky="we")

        self.string_var2 = tkinter.StringVar(value="実行")

        self.button1 = ttk.Button(self, textvariable=self.string_var2, command=self.run)
        self.button1.grid(column=0, row=3, padx=10, pady=10, sticky="we", columnspan=2)

    def select_dir(self):
        path = filedialog.askdirectory()

        if path != "":
            self.string_var1.set(path)

    def close(self, master):
        if not self.is_processing:
            master.destroy()

    def run(self):
        thread = threading.Thread(target=self.dl)
        thread.start()

    def dl(self):
        if self.entry.get() == "":
            messagebox.showerror("エラー", "URLを入力してください。")
            return

        if self.string_var0.get() not in list(OPTION_DICT.keys()):
            messagebox.showerror("エラー", "オプションを設定してください。")
            return

        self.is_processing = True
        self.string_var2.set("処理中")
        for child in self.winfo_children():
            child.config(state="disable")

        url = self.entry.get()
        options = OPTION_DICT[self.string_var0.get()]
        path = self.string_var1.get()

        if path == "選択":
            options.update({"outtmpl":"%(title)s.%(ext)s"})
        else:
            options.update({"outtmpl":f"{path}/%(title)s.%(ext)s"})

        print("\n===\n")

        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([url])
        except:
            messagebox.showerror("エラー", "ダウンロードに失敗しました。")
        else:
            messagebox.showinfo("通知", "処理が終了しました。")
        finally:
            for child in self.winfo_children():
                child.config(state="active")
            self.string_var2.set("実行")
            self.is_processing = False


if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(root)
    app.mainloop()
