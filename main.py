import csv  # csv dosyasını okuyup yazabilmek için import edilmesi gereken kütüphane
import datetime  # python projlerinde zamansal işlemler yapabilmek için kullanacağımz kütüphane
import csv
import re


class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def getDescription(self):
        return self.description

    def getCost(self):
        return self.cost


class Margarita(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Özenle Seçilmiş Kaşar peynrleri"
        self.cost = 60


class Turkpizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Sucuk ve salçalı özel karışım"
        self.cost = 80


class PlainPizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Acılı karışık pizza"
        self.cost = 90


class Salami(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Özenle hazırlnamış salamlı Pizza"
        self.cost = 75


class Italian(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Özel italyan peynileri ile italyan sucuğu"
        self.cost = 90


class Vegan(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Vegan Peynirleri süslenmiş enfes pizza"
        self.cost = 70


class Vegetarian(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Vejateryan sevenlere özel"
        self.cost = 75


class Mix(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Karışık enfes lezzet"
        self.cost = 100


class Decarator(Pizza):
    def __init__(self, companent, description, cost):
        super().__init__(description, cost)
        self.companent = companent

        def get_cost(self):
            return self.companent.get_cost() + Pizza.getCost(self)

        def get_description(self):
            return self.companent.get_description() + Pizza.getDescription(self)


class Olives(Decarator):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Özel zeytinlerle pizzanızı tadlandırın"
        self.cost = 15


class Mushrooms(Decarator):
    def __init__(self, companent, description, cost):
        super().__init__(companent, description, cost)
        self.description = "Özel mantarlarla pizzanızı tadlandırın"
        self.cost = 13


class GoatCheese(Decarator):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Özel keçi peyniri lezzetini pizzada yaşayaın"
        self.cost = 20


class Meat(Decarator):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Özel Dana Etlerimizle pizzanızı tadlandırın"
        self.cost = 25


class Onions(Decarator):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Soğan severlerele özel ekstra soğan"
        self.cost = 10


class Corn(Decarator):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        self.description = "Mısırlarla pizzanıza hem lezzet hemde görsel şölen yaşatın"
        self.cost = 12


def kontrol(a, b):
    if a not in ["1", "2", "3", "4"]:
        print("Hatalı Pizza Seçimi Yaptınız")
    else:
        pass
    if b not in ["11", "12", "13", "14",
                 "15", "16", "17"]:
        print("Hatalı Sos Seçimi Yaptınız")
    else:
        pass


def main():
    menu = open("Menu.txt", "r", encoding="UTF-8")
    print(menu.read())
    while 1:
        pizza = input("Lütfen Pizza Taban seçinizi giriniz:")
        sos = input("Lütfen Sos seçiminiz Giriiniz \nSos seçmek isteimyorsanız 17 tuşlayınz:")
        kontrol(pizza, sos)
        acikalama = "Ödeme Tutarınız :180 TL"
        print(acikalama)

        print("Ödeme İşlemleri için Bilgiler girmeniz gerekmektedir")

        isim = input("Lütfen İsiminizi Giriniz:")
        kimlikNo = input("Lütfen Kimlik Numaranızı Giriniz")
        krediKartNo = input("Lütfen Kredi Kartı Numaranızı Giriniz")
        krediKartSifre = input("Lütfen Şifrenizi Giriniz")
        zaman = datetime.datetime.now()
        with open("OrderDatabes.csv", "w", newline='', encoding="UTF-8") as database:
            musteriBilgi = csv.writer(database)
            musteriBilgi.writerow(([isim, kimlikNo, krediKartNo, krediKartSifre, acikalama, zaman]))

    # if __name__ == '__main__':
    main()


Mushrooms(",", "", 1)
