from tkinter import *
from tkhtmlview import HTMLLabel
import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry('300x200')
root.title('Weather Tkinter')
root.resizable(0,0)


def weatherparser():
    url = 'https://pogoda.mail.ru/prognoz/moskva/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    bso = BeautifulSoup(response.text, "lxml")

    temp = bso.find('div', class_="information__content__temperature")
    weatherinfo = temp.text
    return weatherinfo


myvar = HTMLLabel(root, html="""
    <h2 style="text-align:center;">Погода сейчас""" + weatherparser() + """</h2>

    """)


myvar.pack()

root.mainloop()
