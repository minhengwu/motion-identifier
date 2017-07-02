import tkinter as tk
from keras.models import load_model
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from PIL import ImageTk, Image
import os
import matplotlib
matplotlib.use('TkAgg')


def load_img(n):
    path = '/Users/minheng/Downloads/imgs/test/'
    pic_list = os.listdir('/Users/minheng/Downloads/imgs/test/')[:n]
    pic_list = [os.path.join(path, i) for i in pic_list]
    return pic_list


class show():
    def __init__(self, root):
        self.i = 0
        # root = tk.Tk()
        # root.title('pic')
        img = ImageTk.PhotoImage(Image.open(pic_list[0]))
        self.panel = tk.Label(root, image=img)
        self.panel.pack()

        f = Figure(figsize=(5, 4), dpi=100)
        self.a = f.add_subplot(111)
        target_img = np.expand_dims(np.array(Image.open(pic_list[0])), axis=0)
        pred = model.predict(target_img)
        self.t = np.arange(0, 10, 1)

        self.a.bar(self.t, height=pred[0], align='center', alpha=0.5)
        self.a.set_title('prediction')
        self.a.set_xlabel('classes')
        self.a.set_ylabel('probability')
        self.canvas = FigureCanvasTkAgg(f, master=root)
        self.canvas.show()

        self.canvas._tkcanvas.pack()

        self.but = tk.Button(root, text='next', command=self.next_one)
        self.but.pack()

    def next_one(self):
        if self.i < 19:
            self.i += 1
        else:
            self.i = 0
        img = ImageTk.PhotoImage(Image.open(pic_list[self.i]))
        self.panel.config(image=img)
        self.panel.image = img

        self.a.clear()
        target_img = np.expand_dims(np.array(Image.open(pic_list[self.i])),
                                    axis=0)
        pred = model.predict(target_img)

        self.a.bar(self.t, height=pred[0], align='center', alpha=0.5)
        self.a.set_title('prediction')
        self.a.set_xlabel('classes')
        self.a.set_ylabel('probability')
        self.canvas.draw()


if __name__ == '__main__':
    model = load_model('my_model.h5')
    pic_list = load_img(20)
    root = tk.Tk()
    App = show(root)
    root.mainloop()
