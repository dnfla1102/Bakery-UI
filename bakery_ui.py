import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window,text ='샌드위치 (5000원)').grid(column = 0,row = 0)
        Label(window,text='케이크 (20000원)').grid(column=0, row=1)
        self.sand_num = Entry(window)
        self.sand_num.grid(column=2,row=0)
        self.cake_num = Entry(window)
        self.cake_num.grid(column=2, row=1)
        Button(window, text='주문하기', command = self.send_order).grid(column=0, row=2)


    def send_order(self):
        order_text = str(self.name)+' : '
        s = self.sand_num.get()
        c = self.cake_num.get()

        if s.isnumeric() == True:
            if int(s) > 0:
                order_text += '샌드위치 (5000원) ' + str(s) +'개'

        if s.isnumeric() == True and c.isnumeric() == True:
            if int(s) > 0 and int(c) >0 :
                order_text += ', '

        if c.isnumeric() == True:
            if int(c) > 0:
                order_text += '케이크 (20000원) ' + str(c) +'개'

        ss = s.isnumeric()
        cc = c.isnumeric()




        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
