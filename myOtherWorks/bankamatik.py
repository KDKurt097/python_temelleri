
hesapA = {
    "ad": "Kuzey Kurt",
    "hesapNo": "1",
    "bakiye": 3000,
    "ekHesap": 2000
}

AliHesap = {
    "ad": "Eray Kaşinakurban",
    "hasapNo": "2",
    "bakiye": 9999,
    "ekHesap": 9000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}.")

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı çekebilirsiniz.")

    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (evet/hayır) :")

            if ekHesapKullanimi == "evet":
                
                print("Paranızı çekebilirsiniz.")

            else:
                print("Bakiyeniz yetersiz.")

        else:
            print(f"Toplam bakiyeniz {miktar - toplam} TL eksik kaldığı için paranızı çekemezsiniz.")

paraCek(hesapA, int(input("Çekmek istediğiniz miktarı giriniz: ")))

