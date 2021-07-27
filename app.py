from tkinter import *

def search():
    pass
 
app = Tk()

app.title("Weather app")
app.geometry("200x150")

city_text = StringVar()
city_entry = Entry(app , textvariable = city_text)
city_entry.pack()
search_btn = Button(app, text="search" , width=12 , command=search)
search_btn.pack()

app.mainloop()