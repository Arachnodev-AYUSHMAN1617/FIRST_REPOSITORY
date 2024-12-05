from tkinter import*
base = Tk()
base.geometry('1000x1000')
base.title('Curvercy Application')

lab_0 = Label(base,text='CURVERCY:The User-Friendly Currency Converter App',width = 50,font = 'bold')
lab_0.place(x=500,y=100)

li_of_curr = ('INR','EUR','USD','JPY','BGN','CZK','DKK','GBP','HUF','PLN','RON','SEK','CHF','ISK','NOK','TRY','AUD','BRL','CAD','CNY','HKD','IDR','KRW','MXN','MYR','NZD','PHP','SGD','THB','ZAR')
cv = StringVar(base)
drp1 = OptionMenu(base,cv,*li_of_curr)
drp1.config(width = 100)
cv.set('INR')
lb1 = Label(base, text="From:",width = 10,font = ('Comic Sans MS',20))
lb1.place(x = 200,y = 200)
drp1.place(x = 500,y = 200)


lb2 = Label(base,text = 'Enter Amount:', width = 15, font = ('Comic Sans MS',20))
lb2.place(x = 215,y = 300)
entry_1 = Entry(base)
entry_1.place(x = 500,y = 315,width = 650)
a = entry_1

li_oc = ('INR','EUR','USD','JPY','BGN','CZK','DKK','GBP','HUF','PLN','RON','SEK','CHF','ISK','NOK','TRY','AUD','BRL','CAD','CNY','HKD','IDR','KRW','MXN','MYR','NZD','PHP','SGD','THB','ZAR')
ab = StringVar(base)
drp2 = OptionMenu(base,ab,*li_oc)
drp2.config(width = 100)
ab.set('USD')
lb3 = Label(base, text="To:",width = 10,font = ('Comic Sans MS',20))
lb3.place(x = 190,y = 400)
drp2.place(x = 500,y = 400)

lb4 = Label(base,text = 'Result Amount:', width = 15, font = ('Comic Sans MS',20))
lb4.place(x = 215,y = 500)
entry_2 = Entry(base)
entry_2.place(x = 500,y = 515,width = 650)

def conv():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    cur_fro = cv.get()
    cur_to = ab.get()

    amt = c.convert(cur_fro,cur_to,float(entry_1.get()))
    entry_2.insert(0,str(amt))

b = Button(base,text = 'Convert',command = conv)
b.place(x = 500,y = 600)
base.mainloop()
