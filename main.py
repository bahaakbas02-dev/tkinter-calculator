import tkinter as tk

def topla():
    global sonuc

    sayi1get = int(sayi1.get())
    sayi2get = int(sayi2.get())

    sonuc = sayi1get + sayi2get 

    sonuclabel.config(text=sonuc)


def cikar():
    global sonuc

    sayi1get = int(sayi1.get())
    sayi2get = int(sayi2.get())

    sonuc = sayi1get - sayi2get 

    sonuclabel.config(text=sonuc)    

def carp():
    global sonuc

    sayi1get = int(sayi1.get())
    sayi2get = int(sayi2.get())

    sonuc = sayi1get * sayi2get 

    sonuclabel.config(text=sonuc)      

def bol():
    global sonuc

    sayi1get = int(sayi1.get())
    sayi2get = int(sayi2.get())

    sonuc = sayi1get / sayi2get 

    sonuclabel.config(text=sonuc)     

   
root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("600x600")

baslik = tk.Label(text="Hesap Makinesi", font=("Arial", 20))
baslik.pack(pady=5)

# 1. Sayı
sayi1label = tk.Label(text="1. Sayı", font=("Arial", 10))
sayi1label.pack(pady=5)
sayi1 = tk.Entry()
sayi1.pack(pady=5)

# 2. Sayı
sayi2label = tk.Label(text="2. Sayı", font=("Arial", 10))
sayi2label.pack(pady=5)
sayi2 = tk.Entry()
sayi2.pack(pady=5)

# Toplama Butonu
toplama = tk.Button(text="Topla", command=topla)
toplama.pack(pady=5)

# Çıkarma Butonu
toplama = tk.Button(text="Çıkar", command=cikar)
toplama.pack(pady=5)

# Çarpma Butonu
toplama = tk.Button(text="Çarp", command=carp)
toplama.pack(pady=5)

# Bölme Butonu
toplama = tk.Button(text="Böl", command=bol)
toplama.pack(pady=5)

# Sonuç
sonuclabel = tk.Label(text="")
sonuclabel.pack(pady=5)

root.mainloop()