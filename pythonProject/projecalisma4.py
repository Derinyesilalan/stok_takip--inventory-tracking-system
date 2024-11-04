from tkinter import *
import tkinter as tk
from tkinter import ttk, Tk,Radiobutton,messagebox,PhotoImage, Toplevel


#PENCEREMİZİ OLUŞTURDUK
pen = Tk()
pen.title("proje deneme")
pen.geometry("300x300")
pen.config(bg="#333333")

#SQL LİTE İLE BAĞLANTISINI KURDUM
import sqlite3
db = sqlite3.connect("loginsayfasi.db")
yetki = db.cursor()

#LOGİN ADINDA TABLO OLUŞTURDUM
def sqlbaglanti():
    yetki.execute("CREATE TABLE IF NOT EXISTS login(ad TEXT NOT NULL,sifre TEXT NOT NULL)")
    db.commit()

sqlbaglanti()#ÇAĞIRDIK

#KARGOLAR SAYFASI
def kargolar():
    yetki.execute("""
        CREATE TABLE IF NOT EXISTS kargo (
            kargo_id INTEGER PRIMARY KEY,
            kargo_ad TEXT NOT NULL,
            alici_ad TEXT NOT NULL,
            durum TEXT NOT NULL,
            takip_no TEXT NOT NULL,
            teslimat_tarihi DATE
        )
    """)
    db.commit()
    nick = entry1.get()
    password = entry2.get()
    yetki.execute("SELECT * FROM login WHERE ad=? AND sifre=?", (nick, password))
    kullanici = yetki.fetchone() #BURADA DOĞRULAMA YAPIYOR EĞER BÖYLE Bİ KULLANICI VARSA FETCHONE İLE KULLANICI BULUNUYOR FETCHONE TEK ALIYOR FETCHALL TÜM SATIRLARI ALIYOR
    if kullanici:
        global entryyyy
        global entryyyy1
        global entryyyy2
        global entryyyy3
        global entryyyy4
        global entryyyy5
        global treeview3
        global combo_kargo_ad

        pen.destroy()
        pen4 = Tk()
        pen4.geometry("1750x500")
        pen4.config(bg="#333333")
        pen4.title("Ana menü")

        labellll = Label(pen4, text="kargo_id =", bg="#333333", fg="white", font=("Arial", 15))
        labellll1 = Label(pen4, text="kargo_ad =", bg="#333333", fg="white", font=("Arial", 15))
        labellll2 = Label(pen4, text="alici_ad =", bg="#333333", fg="white", font=("Arial", 15))
        labellll3 = Label(pen4, text="durum =", bg='#333333', fg="white", font=("Arial", 15))
        labellll4 = Label(pen4, text="takip_no =", bg='#333333', fg="white", font=("Arial", 15))
        labellll5 = Label(pen4, text="teslimat_tarihi =", bg='#333333', fg="white", font=("Arial", 15))

        labellll.grid(row=0, column=0)
        labellll1.grid(row=1, column=0)
        labellll2.grid(row=2, column=0)
        labellll3.grid(row=3, column=0)
        labellll4.grid(row=4, column=0)
        labellll5.grid(row=5, column=0)

        entryyyy = Entry(pen4)
        entryyyy1 = Entry(pen4)
        entryyyy2 = Entry(pen4)
        entryyyy3 = Entry(pen4)
        entryyyy4 = Entry(pen4)
        entryyyy5 = Entry(pen4)

        entryyyy.grid(row=0, column=1)
        entryyyy1.grid(row=1, column=1)
        entryyyy2.grid(row=2, column=1)
        entryyyy3.grid(row=3, column=1)
        entryyyy4.grid(row=4, column=1)
        entryyyy5.grid(row=5, column=1)

        kargo_ad = ["Aras", "Yurtiçi", "Sürat"]
        combo_kargo_ad = ttk.Combobox(pen4, values=kargo_ad)
        combo_kargo_ad.set(kargo_ad[0])  # Set default value
        combo_kargo_ad.grid(row=1, column=1)

        treeview3 = ttk.Treeview(pen4, columns=("kargo_id", "kargo_ad", "alici_ad", "durum", "takip_no", "teslimat_tarihi"), show="headings")
        treeview3.grid(row=0, column=3, rowspan=6, columnspan=3, padx=10, pady=10)

        treeview3.heading("#0", text="Index")
        treeview3.heading("kargo_id", text="Kargo ID")
        treeview3.heading("kargo_ad", text="Kargo Ad")  # Updated heading
        treeview3.heading("alici_ad", text="Alıcı Ad")
        treeview3.heading("durum", text="Durum")
        treeview3.heading("takip_no", text="Takip No")
        treeview3.heading("teslimat_tarihi", text="Teslimat Tarihi")

        butonnnn1 = Button(pen4, text="Hepsini Göster", fg="white", bg='#333333', width=12, command=hepsini_goster_kargolar)
        butonnnn2 = Button(pen4, text="Ekle", fg="white", bg='#333333', width=12, command=kargo_ekle)
        butonnnn3 = Button(pen4, text="Sil", fg="white", bg='#333333', width=12, command=kargo_sil)
        butonnnn4 = Button(pen4, text="Ara", fg="white", bg='#333333', width=12, command=kargo_ara)
        butonnnn5 = Button(pen4, text="Güncelle", fg="white", bg='#333333', width=12, command=kargo_guncelle)

        butonnnn1.grid(row=7, column=0, pady=10)
        butonnnn2.grid(row=8, column=0, pady=10)
        butonnnn3.grid(row=9, column=0, pady=10)
        butonnnn4.grid(row=7, column=1, pady=10)
        butonnnn5.grid(row=8, column=1, pady=10)
        #ORTAYA HİZZALAMA
        pen4.update_idletasks()
        width = pen4.winfo_width()
        height = pen4.winfo_height()
        x = (pen4.winfo_screenwidth() // 2) - (width // 2)
        y = (pen4.winfo_screenheight() // 2) - (height // 2)
        pen4.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        pen4.mainloop()
    else:
        messagebox.showerror(title="hata", message="yanlış isim veya şifre")


def hepsini_goster_kargolar():
    yetki.execute("SELECT * FROM kargo")
    kargolar = yetki.fetchall()
    treeview3.delete(*treeview3.get_children())  # Önceki verileri temizle
    for kargo in kargolar:
        treeview3.insert("", "end", values=kargo)


def kargo_ekle():
    kargo_ad = combo_kargo_ad.get()  # Get the selected value from ComboBox
    alici_ad = entryyyy2.get()
    durum = entryyyy3.get()
    takip_no = entryyyy4.get()
    teslimat_tarihi = entryyyy5.get()

    if kargo_ad and alici_ad and durum and takip_no and teslimat_tarihi:
        yetki.execute("INSERT INTO kargo (kargo_ad, alici_ad, durum, takip_no, teslimat_tarihi) VALUES (?, ?, ?, ?, ?)",
                      (kargo_ad, alici_ad, durum, takip_no, teslimat_tarihi))
        db.commit()
        messagebox.showinfo("Başarı", "Kargo başarıyla eklendi.")
        hepsini_goster_kargolar()
    else:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")


def kargo_sil():
    #Seçili satırın ID'sini aldık
    selected_item = treeview3.selection()
    if not selected_item:
        messagebox.showwarning("Uyarı", "Lütfen silinecek bir satır seçin.")
        return

    kargo_id = treeview3.item(selected_item)['values'][0] #0 OLMASININ SEBEBİ LİSTENİN İLK ÖĞESİNİ ALMASI

    #VERİTABANINDAN SİLdim
    yetki.execute("DELETE FROM kargo WHERE kargo_id=?", (kargo_id,))
    db.commit()

    #TREEVİEW'DAN SİLDİK
    treeview3.delete(selected_item)
    messagebox.showinfo("Başarı", "Kargo başarıyla silindi.")


def kargo_ara():
    kargo_ad = combo_kargo_ad.get()
    yetki.execute("SELECT * FROM kargo WHERE kargo_ad=?", (kargo_ad,))
    sonuclar = yetki.fetchall()
    treeview3.delete(*treeview3.get_children())
    for kargo in sonuclar:
        treeview3.insert("", "end", values=kargo)


def kargo_guncelle():
    selected_item = treeview3.selection()[0]
    yeni_kargo_ad = combo_kargo_ad.get()
    yetki.execute("UPDATE kargo SET kargo_ad=? WHERE kargo_id=?", (yeni_kargo_ad, selected_item))
    db.commit()# YERİNE GETİRİYOR KENDİ ÜSTÜNDEKİ KODU
    messagebox.showinfo("Başarı", "Kargo başarıyla güncellendi.")
    hepsini_goster_kargolar()


def kisiler():
    yetki.execute("""
        CREATE TABLE IF NOT EXISTS kisi (
            kisi_id INTEGER PRIMARY KEY,
            ad TEXT NOT NULL,
            soyad TEXT NOT NULL,
            cinsiyet TEXT NOT NULL,
            yas INTEGER,
            adres TEXT,
            email TEXT
        )
    """)
    db.commit()
    nick = entry1.get()
    password = entry2.get()
    yetki.execute("SELECT * FROM login WHERE ad=? AND sifre=?", (nick, password))
    kullanici = yetki.fetchone()
    if kullanici:
        global entryyy
        global entryyy1
        global entryyy2
        global entryyy3
        global entryyy4
        global entryyy5
        global entryyy6
        global treeview2

        pen.destroy()
        pen4 = Tk()
        pen4.geometry("1750x500")
        pen4.config(bg="#333333")
        pen4.title("Ana menü")

        labelll = Label(pen4, text="kisi_id  =", bg="#333333", fg="white", font=("Arial", 15))
        labelll1 = Label(pen4, text="ad  =", bg="#333333", fg="white", font=("Arial", 15))
        labelll2 = Label(pen4, text="soyad  =", bg="#333333", fg="white", font=("Arial", 15))
        labelll3 = Label(pen4, text="cinsiyet  =", bg='#333333', fg="white", font=("Arial", 15))
        labelll4 = Label(pen4, text="yas  =", bg='#333333', fg="white", font=("Arial", 15))
        labelll5 = Label(pen4, text="adres  =", bg='#333333', fg="white", font=("Arial", 15))
        labelll6 = Label(pen4, text="email  =", bg='#333333', fg="white", font=("Arial", 15))

        labelll.grid(row=0, column=0)
        labelll1.grid(row=1, column=0)
        labelll2.grid(row=2, column=0)
        labelll3.grid(row=3, column=0)
        labelll4.grid(row=4, column=0)
        labelll5.grid(row=5, column=0)
        labelll6.grid(row=6, column=0)

        entryyy = Entry(pen4)
        entryyy1 = Entry(pen4)
        entryyy2 = Entry(pen4)
        entryyy3 = StringVar()
        entryyy4 = Entry(pen4)
        entryyy5 = Entry(pen4)
        entryyy6 = Entry(pen4)

        entryyy.grid(row=0, column=1)
        entryyy1.grid(row=1, column=1)
        entryyy2.grid(row=2, column=1)

        #RADİO BUTTON KISIM
        entryyy3 = StringVar()
        entryyy3.set("erkek")
        male_radio = Radiobutton(pen4, text="Male", variable=entryyy3, value="erkek", bg='#333333', fg="white", font=("Arial", 8))
        female_radio = Radiobutton(pen4, text="Female", variable=entryyy3, value="kadın", bg='#333333', fg="white", font=("Arial", 8))
        male_radio.grid(row=3, column=1, sticky=W,padx=10)
        female_radio.grid(row=3, column=1, sticky=E,padx=5)

        entryyy4.grid(row=4, column=1)
        entryyy5.grid(row=5, column=1)
        entryyy6.grid(row=6, column=1)

        treeview2 = ttk.Treeview(pen4, columns=("kisi_id", "ad", "soyad", "cinsiyet", "yas", "adres", "email"), show="headings")
        treeview2.grid(row=0, column=3, rowspan=6, columnspan=3, padx=10, pady=10)

        treeview2.heading("#0", text="Index")
        treeview2.heading("kisi_id", text="Kişi ID")
        treeview2.heading("ad", text="Ad")
        treeview2.heading("soyad", text="Soyad")
        treeview2.heading("cinsiyet", text="Cinsiyet")
        treeview2.heading("yas", text="Yaş")
        treeview2.heading("adres", text="Adres")
        treeview2.heading("email", text="Email")

        butonnn1 = Button(pen4, text="Hepsini Göster", fg="white", bg='#333333', width=12,command=hepsini_goster_kisiler)
        butonnn2 = Button(pen4, text="Ekle", fg="white", bg='#333333', width=12,command=kisi_ekle)
        butonnn3 = Button(pen4, text="Sil", fg="white", bg='#333333', width=12,command=kisi_sil)
        butonnn4 = Button(pen4, text="Ara", fg="white", bg='#333333', width=12,command=kisi_ara)
        butonnn5 = Button(pen4, text="Güncelle", fg="white", bg='#333333', width=12,command=kisi_guncelle)

        butonnn1.grid(row=7, column=0, pady=10)
        butonnn2.grid(row=8, column=0, pady=10)
        butonnn3.grid(row=9, column=0, pady=10)
        butonnn4.grid(row=7, column=1, pady=10)
        butonnn5.grid(row=8, column=1, pady=10)



        pen4.update_idletasks()
        width = pen4.winfo_width()
        height = pen4.winfo_height()
        x = (pen4.winfo_screenwidth() // 2) - (width // 2)
        y = (pen4.winfo_screenheight() // 2) - (height // 2)
        pen4.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        pen4.mainloop()
    else:
        messagebox.showerror(title="hata", message="yanlış isim veya şifre")
def hepsini_goster_kisiler():
    yetki.execute("SELECT * FROM kisi")
    kisiler = yetki.fetchall()
    treeview2.delete(*treeview2.get_children())  # Önceki verileri temizle
    for kisi in kisiler:
        treeview2.insert("", "end", values=kisi)

def kisi_ekle():
    ad = entryyy1.get()
    soyad = entryyy2.get()
    cinsiyet = entryyy3.get()
    yas = entryyy4.get()
    adres = entryyy5.get()
    email = entryyy6.get()

    if ad and soyad and cinsiyet and yas and adres and email:
        yetki.execute("INSERT INTO kisi (ad, soyad, cinsiyet, yas, adres, email) VALUES (?, ?, ?, ?, ?, ?)",#SORU İŞARETİ KOYMA SEBEBİMİZ SORGU ÇALIŞTIRMADAN ÖNCE YERİNE GEÇİCEK DEĞERLERİ YAZICAZ
                      (ad, soyad, cinsiyet, yas, adres, email))
        db.commit()
        messagebox.showinfo("Başarı", "Kişi başarıyla eklendi.")
        hepsini_goster_kisiler()
    else:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")

def kisi_sil():
    selected_item = treeview2.selection()
    if not selected_item:
        messagebox.showwarning("Uyarı", "Lütfen silinecek bir satır seçin.")
        return

    kisi_id = treeview2.item(selected_item)['values'][0]
    yetki.execute("DELETE FROM kisi WHERE kisi_id=?", (kisi_id,))
    db.commit()
    treeview2.delete(selected_item)
    messagebox.showinfo("Başarı", "Kişi başarıyla silindi.")

def kisi_ara():
    ad = entryyy.get()
    yetki.execute("SELECT * FROM kisi WHERE ad=?", (ad,))
    sonuclar = yetki.fetchall()
    treeview2.delete(*treeview2.get_children())
    for kisi in sonuclar:
        treeview.insert("", "end", values=kisi)

def kisi_guncelle():
    selected_item = treeview2.selection()[0]
    yeni_ad = entryyy.get()
    yetki.execute("UPDATE kisi SET ad=? WHERE kisi_id=?", (yeni_ad, selected_item))
    db.commit()
    messagebox.showinfo("Başarı", "Kişi başarıyla güncellendi.")
    hepsini_goster_kisiler()

def urunler():
    yetki.execute("""
        CREATE TABLE IF NOT EXISTS urun (
            urun_id INTEGER PRIMARY KEY,
            urun_adi TEXT NOT NULL,
            urun_modeli TEXT NOT NULL,
            urun_fiyati INTEGER,
            urun_turu TEXT NOT NULL,
            urun_siparis_tarihi DATE,
            urun_stok INTEGER DEFAULT 0
        )
    """)
    db.commit()
    nick = entry1.get()
    password = entry2.get()
    yetki.execute("SELECT * FROM login WHERE ad=? AND sifre=?", (nick, password))
    kullanici = yetki.fetchone()
    if kullanici:
#BAŞKA BİR FONKSİYONDAN ERİŞEBİLEYİM DİYE GLOBAL YAPTIM BAŞKA BİR ÇÖZÜM YOLU GELMEDİ AKLIMA
        global entryy
        global entryy1
        global entryy2
        global entryy3
        global entryy4
        global entryy5
        global entryy6
        global treeview


        pen.destroy()
        pen2 = Tk()
        pen2.geometry("1750x500")
        pen2.config(bg="#333333")
        pen2.title("Ana menü")
#LABELLAR
        labell = Label(pen2, text="ürün_id  =", bg="#333333", fg="white", font=("Arial", 15))
        labell1 = Label(pen2, text="ürün_adi  =", bg="#333333", fg="white", font=("Arial", 15))
        labell2 = Label(pen2, text="ürün_modeli  =", bg="#333333", fg="white", font=("Arial", 15))
        labell3 = Label(pen2, text="ürün_fiyati  =", bg='#333333', fg="white", font=("Arial", 15))
        labell4 = Label(pen2, text="ürün_türü  =", bg='#333333', fg="white", font=("Arial", 15))
        labell5 = Label(pen2, text="ürün_siparis_tarihi  =", bg='#333333', fg="white", font=("Arial", 15))
        labell6 = Label(pen2, text="ürün_stok  =", bg='#333333', fg="white", font=("Arial", 15))
#LABELLARI KONUMLANDIRDIK
        labell1.grid(row=1, column=0)
        labell.grid(row=0, column=0)
        labell2.grid(row=2, column=0)
        labell3.grid(row=3, column=0)
        labell4.grid(row=4, column=0)
        labell5.grid(row=5, column=0)
        labell6.grid(row=6, column=0)

#ENTRYLERİ TANIMLADIK
        entryy = Entry(pen2)
        entryy1 = Entry(pen2)
        entryy2 = Entry(pen2)
        entryy3 = Entry(pen2)
        entryy4 = Entry(pen2)
        entryy5 = Entry(pen2)
        entryy6 = Entry(pen2)

#ENTRYLERİN KONUMLANDIRILMASI
        entryy.grid(row=0, column=1)
        entryy1.grid(row=1, column=1)
        entryy2.grid(row=2, column=1)
        entryy3.grid(row=3, column=1)
        entryy4.grid(row=4, column=1)
        entryy5.grid(row=5, column=1)
        entryy6.grid(row=6, column=1)

#TREEVİEW KISMI
        treeview = ttk.Treeview(pen2, columns=("ürün_id", "ürün_adi", "ürün_modeli", "ürün_fiyati", "ürün_turu", "ürün_siparis_tarihi", "ürün_stok"), show="headings")
        treeview.grid(row=0, column=3, rowspan=6, columnspan=3, padx=10, pady=10)

#TREEVİEW BASLIK EKLEME
        treeview.heading("#0", text="Index")
        treeview.heading("ürün_id", text="Ürün ID")
        treeview.heading("ürün_adi", text="Ürün Adı")
        treeview.heading("ürün_modeli", text="Ürün Modeli")
        treeview.heading("ürün_fiyati", text="Ürün Fiyatı")
        treeview.heading("ürün_turu", text="Ürün Türü")
        treeview.heading("ürün_siparis_tarihi", text="Ürün Sipariş Tarihi")
        treeview.heading("ürün_stok", text="Ürün Stok")

#BUTONLAR
        butonn1 = Button(pen2, text="Hepsini Göster", fg="white", bg='#333333', width=12, command=hepsini_goster)
        butonn2 = Button(pen2, text="Ekle", fg="white", bg='#333333', width=12, command=urun_ekle)
        butonn3 = Button(pen2, text="Sil", fg="white", bg='#333333', width=12, command=urun_sil)
        butonn4 = Button(pen2, text="Ara", fg="white", bg='#333333', width=12, command=urun_ara)
        butonn5 = Button(pen2, text="Güncelle", fg="white", bg='#333333', width=12, command=urun_guncelle)

#BUTON KONUMLANDIRDIM
        butonn1.grid(row=7, column=0, pady=10)
        butonn2.grid(row=8, column=0, pady=10)
        butonn3.grid(row=9, column=0, pady=10)
        butonn4.grid(row=7, column=1, pady=10)
        butonn5.grid(row=8, column=1, pady=10)

#YİNE ORTALADIK
        pen2.update_idletasks()
        width = pen2.winfo_width()
        height = pen2.winfo_height()
        x = (pen2.winfo_screenwidth() // 2) - (width // 2)
        y = (pen2.winfo_screenheight() // 2) - (height // 2)
        pen2.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        pen2.mainloop()
    else:
        messagebox.showerror(title="hata", message="yanlış isim veya şifre")

def hepsini_goster():
    treeview.delete(*treeview.get_children())  # Treeview'ı temizle
    yetki.execute("SELECT * FROM urun")
    urunler = yetki.fetchall()
    for urun in urunler:
        treeview.insert("", "end", values=urun)

#VERİLEN İD YE GÖRE ÜRÜN GETİRİYORUM
def urun_ekle():
    urun_id = entryy.get()
    urun_adi = entryy1.get()
    urun_modeli = entryy2.get()
    urun_fiyati = entryy3.get()
    urun_turu = entryy4.get()
    urun_siparis_tarihi = entryy5.get()
    urun_stok = entryy6.get()

    yetki.execute("INSERT INTO urun VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (urun_id, urun_adi, urun_modeli, urun_fiyati, urun_turu, urun_siparis_tarihi, urun_stok))
    db.commit()
    hepsini_goster()

def urun_sil():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("Uyarı", "Lütfen silinecek bir satır seçin.")
        return

    urun_id = treeview.item(selected_item)['values'][0]
    yetki.execute("DELETE FROM urun WHERE urun_id=?", (urun_id,))
    db.commit()
    treeview.delete(selected_item)

def urun_ara():
    urun_id = entryy.get()
    yetki.execute("SELECT * FROM urun WHERE urun_id=?", (urun_id,))
    urunler = yetki.fetchall()
    treeview.delete(*treeview.get_children())  # Treeview'ı temizle
    for urun in urunler:
        treeview.insert("", "end", values=urun)

def urun_guncelle():
    urun_id = entryy.get()
    urun_adi = entryy1.get()
    urun_modeli = entryy2.get()
    urun_fiyati = entryy3.get()
    urun_turu = entryy4.get()
    urun_siparis_tarihi = entryy5.get()
    urun_stok = entryy6.get()  # Yeni eklenen satır

    yetki.execute("UPDATE urun SET urun_adi=?, urun_modeli=?, urun_fiyati=?, urun_turu=?, urun_siparis_tarihi=?, urun_stok=? "
                  "WHERE urun_id=?", (urun_adi, urun_modeli, urun_fiyati, urun_turu, urun_siparis_tarihi, urun_stok, urun_id))
    db.commit()
    hepsini_goster()

def giris():
    nick = entry1.get()
    password = entry2.get()
    yetki.execute("SELECT * FROM login WHERE ad=? AND sifre=?", (nick, password))
    kullanici = yetki.fetchone()
    if kullanici:

        ana_menu = Toplevel()
        ana_menu.geometry("1400x500")
        ana_menu.title("Ana Menü")
        ana_menu.config(bg="#333333")
        label = Label(ana_menu, text="Lütfen bir seçenek seçin", fg="white", bg="#333333")
        label.config(font=("Times New Roman", 20))
        label.grid(row=0, column=0, pady=20, columnspan=3)

    #RESİM DOSYALARINI EKLEYİN (DOSYA YOLLARINI GÜNCELLEDİK)
        img_urunler = PhotoImage(file="ürün.png")
        img_kisiler = PhotoImage(file="imresizer-1702897985469.png")
        img_kargo = PhotoImage(file="imresizer-1702897975584.png")

    #BUTONLAR
        btn_urunler = Button(ana_menu, text="Ürünler", fg="white", command=urunler,image=img_urunler, compound=tk.TOP, width=300, height=300, bg="#333333")#COMPOUND TK TOP KODU GÖRSELİN YAZININI ÜSTÜNE GELMESİNİ SAĞLIYOR
        btn_urunler.grid(row=1, column=0, padx=10, pady=10)

        btn_kisiler = Button(ana_menu, text="Kişiler", fg="white",command=kisiler, image=img_kisiler, compound=tk.TOP, width=300, height=300, bg="#333333")
        btn_kisiler.grid(row=1, column=1, padx=200)

        btn_kargo = Button(ana_menu, text="Kargo Firmaları", fg="white",command=kargolar,image=img_kargo, compound=tk.TOP, width=300, height=300, bg="#333333")
        btn_kargo.grid(row=1, column=2, padx=10, pady=10)

    #ORTAYA KONUNMLANDIRMA
        ana_menu.update_idletasks()
        width = ana_menu.winfo_width()
        height = ana_menu.winfo_height()
        x = (ana_menu.winfo_screenwidth() // 2) - (width // 2)
        y = (ana_menu.winfo_screenheight() // 2) - (height // 2)
        ana_menu.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        ana_menu.mainloop()
    else:
        messagebox.showerror(title="hata", message="yanlış isim veya şifre")


#VERİTABANINA KULLANICI EKLEME KODUM
def kullanıcıekle():
    pen3 = Toplevel()  # YENİ PENCERE AÇ
    pen3.geometry("200x200")
    pen3.config(bg="#333333")
    pen3.title("Kullanıcı ekleme ekranı")

# KULLANICI ADI VE ŞİFRE İÇİN ENTRY WİDGET'LARI
    entry3 = Entry(pen3)
    entry4 = Entry(pen3)

# VARSAYILAN METİNLERİ AYARLA
    entry3.insert(0, "kullanıcı adını giriniz")
    entry4.insert(0, "şifrenizi giriniz")

# BUTON FONKSİYONU: VERİTABANINA KULLANICIYI EKLE
    def kullanici_ekle():
        yeni_nick = entry3.get()
        yeni_password = entry4.get()

# SQL SORGUSU İLE VERİTABANINA KULLANICI EKLE
        yetki.execute("INSERT INTO login(ad, sifre) VALUES (?, ?)", (yeni_nick, yeni_password))
        db.commit()
# İŞLEM TAMAMLANDIKTAN SONRA PENCEREYİ KAPATMA KODU
        pen3.destroy()

    buton4 = Button(pen3, text="Ekle", fg="white", bg='#333333', command=kullanici_ekle)

# KONUMLANDIRMA
    entry3.grid(row=1, column=2, pady=10)
    entry4.grid(row=2, column=2, pady=10)
    buton4.grid(row=3, column=2, pady=10)

# ORTAYA KONUMLANDIRDIM
    pen3.update_idletasks()
    width = pen3.winfo_width()
    height = pen3.winfo_height()
    x = (pen3.winfo_screenwidth() // 2) - (width // 2)
    y = (pen3.winfo_screenheight() // 2) - (height // 2)
    pen3.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pen3.mainloop()

#DEF GÖSTER FONKSİYONU İLE GÖSTERE BUTONUNU BASILDIĞINDA ŞİFRE GÖSTERİLDİ
def göster():
    if entry2.cget("show") == "":
        entry2.config(show="*")
    else:
        entry2.config(show="")

#LABELLARIMIZI OLUŞTURDUK
label1 = Label(pen, text="İSİM", bg="#333333", fg="white", font=("Arial", 15))
label2 = Label(pen, text="ŞİFRE", bg="#333333", fg="white", font=("Arial", 15))
login_label = Label(pen, text="Login", bg='#333333', fg="white", font=("Arial", 30))

#ENTRYLERİMİZİ OLUŞTURDUK
entry1 = Entry(pen)
entry2 = Entry(pen, show="*")

#BUTONLARIMIZI OLUŞTURDUK
buton1 = Button(pen, text="GİRİŞ YAP", command=giris, font=("Arial", 8))
buton2 = Button(pen, text="GÖSTER", command=göster, font=("Arial", 7))
buton3 = Button(pen, text="KULLANICI EKLE", command=kullanıcıekle, font=("Arial", 7),bg='#333333',fg="white")

#HEPSİNİ KONUMLANDIRDIK
label1.grid(row=1, column=0, pady=10)
label2.grid(row=2, column=0, padx=10, pady=10)
buton2.grid(row=2, column=2, padx=10, pady=10)
buton3.grid(row=3, column=0, padx=10)
entry1.grid(row=1, column=1, pady=10)
entry2.grid(row=2, column=1, pady=10)
buton1.grid(row=3, column=1, pady=10)
login_label.grid(row=0, column=1, pady=20)

#PENCEREYİ EKRANIN ORTASINA YERLEŞTİRME
pen.update_idletasks()
width = pen.winfo_width()
height = pen.winfo_height()
x = (pen.winfo_screenwidth() // 2) - (width // 2)
y = (pen.winfo_screenheight() // 2) - (height // 2)
pen.geometry('{}x{}+{}+{}'.format(width, height, x, y))

pen.mainloop()