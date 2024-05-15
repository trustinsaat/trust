print("hoş geldin")
while True:
    print("giriş için g")
    print("kayıt için k")
    print("çıkış için ç")

    secim=input("ne yapmak istersiniz")

    if secim == "k":
        ki=input("isim gir")
        kş=input("şifre gir")
        if len(kş)>= 8:
            print("kayıt başarılı")

        else:
            print("şifre en az `8` karakter olmalı>!")

    if  secim == "g":
        gi=input("ism gir ")
        gş=input ("şifre gir")
        if ki == gi and kş == gş:
            print("giriş başarılı")
