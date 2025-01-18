from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def odi_na_stranicu():
    global tekst_sadrzaj
    link = link_input.get()
    driver.get(f"https://en.wikipedia.org/wiki/{link}")
    try:
        elemenat = driver.find_element(By.ID, "bodyContent")
        tekst_sadrzaj = elemenat.text
        text_widget.delete("1.0", END)
        text_widget.insert(END, tekst_sadrzaj)
    except Exception as e:
        text_widget.delete("1.0", END)
        text_widget.insert(END, f"Error: {e}")


def pretrazi_reci():
    rec = word_input.get()
    if rec and 'tekst_sadrzaj' in globals():
        rezultat = ""
        for linija in tekst_sadrzaj.splitlines():
            if rec.lower() in linija.lower():
                rezultat += linija + "\n"
        text_widget.delete("1.0", END)
        text_widget.insert(END, rezultat if rezultat else f"No results found for '{rec}'")
    else:
        text_widget.delete("1.0", END)
        text_widget.insert(END, "Please load a Wikipedia page first and enter a word to search.")


gg = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=gg)

prozor = Tk()
prozor.title("Wikipedia")
prozor.geometry("600x900")
prozor.config(bg="lightblue")

tekst = Label(prozor, text="Wikipedia\n\nsearch whatever you want", font=("Arial", 20), bg="lightblue")
tekst.place(x=125, y=30)

link_input = Entry(prozor, width=30)
link_input.place(x=200, y=250)

potvrdi_dugme = Button(prozor, text="Confirm", bg="gray", fg="Black", command=odi_na_stranicu)
potvrdi_dugme.place(x=375, y=250)

word_label = Label(prozor, text="Search by word:", bg="lightblue", font=("Arial", 12))
word_label.place(x=50, y=280)

word_input = Entry(prozor, width=30)
word_input.place(x=200, y=280)

word_search_btn = Button(prozor, text="Search Word", bg="gray", fg="Black", command=pretrazi_reci)
word_search_btn.place(x=375, y=280)

text_widget = Text(prozor, wrap=WORD, width=70, height=30)
text_widget.place(x=50, y=320)

prozor.mainloop()
