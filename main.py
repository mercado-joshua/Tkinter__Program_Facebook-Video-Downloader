#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

import re
import requests
import urllib.request
import os
import pyperclip

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_widgets()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(True, True)
        self.title('Facebook Video Downloader Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        self.searchform = ttk.Frame(self)
        self.searchform.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.fieldset = ttk.LabelFrame(self.searchform, text='Download Facebook Video')
        self.fieldset.pack(side=tk.TOP, expand=True, padx=10, pady=10, fill=tk.BOTH)

        label = ttk.Label(self.fieldset, text='Video URL *copy the video url first')
        label.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10, pady=(10, 0))

        self.query = tk.StringVar()
        self.query.set(pyperclip.paste())
        entry = ttk.Entry(self.fieldset, width=80, textvariable=self.query)
        entry.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10)

        label = ttk.Label(self.fieldset, text='File Name')
        label.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10, pady=(10, 0))

        self.filename = tk.StringVar()
        entry = ttk.Entry(self.fieldset, width=50, textvariable=self.filename)
        entry.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10)

        self.button = ttk.Button(self.fieldset, text='Download', command=self.download)
        self.button.pack(side=tk.RIGHT, anchor=tk.W, padx=(0, 10), pady=10)

    # -------------------------------------------
    def download(self):
        html = requests.get(self.query.get())
        file = f'{self.filename.get()}.mp4'

        # parse url
        try:
            url = re.search('hd_src:"(.+?)"', html.text)[1]
            # print('HD Video')
        except:
            url = re.search('sd_src:"(.+?)"', html.text)[1]
            # print('SD Video')

        # download file
        urllib.request.urlretrieve(url, file)
        # play the video
        os.startfile(file)


#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()