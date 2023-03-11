import csv  # csv dosyasını okuyup yazabilmek için import edilmesi gereken kütüphane
import datetime  # python projlerinde zamansal işlemler yapabilmek için kullanacağımz kütüphane



#Öncelikle pizza sınıfımız tanımlıyoruz
class Pizza:
    def __init__(self, description, cost):
        self.description = description #sipariş açıklması
        self.cost = cost #sipariş ücreti
    #Seçilen pizzalara göre açıklama döndürecek metdoumuz
    def get_description(self):
        return self.description
    #Seçilen pizzalara göre ücretini döndürecek fonksiyonumuz
    def get_cost(self):
        return self.cost

#Ana klasımız olan Pizza klasının subclası olan bu classlar çeşitli pizza tabanlarının açıklamlarını ve ücretlerini oluşturmaktadır.
class Margarita(Pizza):
    def __init__(self):
        super().__init__("Özenle Seçilmiş Kaşar peynrleri", 60) #Super fonksiyonu ile subclassımızda Pizza klasımızın özelliklerini kullanmış oluyoruz



class Turkpizza(Pizza):
    def __init__(self):
        super().__init__("Sucuk ve salçalı özel karışım", 80)



class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Acılı karışık pizza",90)


class Salami(Pizza):
    def __init__(self):
        super().__init__("Özenle hazırlnamış salamlı Pizza", 75)



#Sos sınıflarının ana sınıfı olan bu class aynı zamanda Pizza classının özelliklerini kullanrak soslar ve pizza tabanın açıklama ve fiyatlarını kullanmamızı sağlıyor
class Decarator(Pizza):
    def __init__(self, companent, description, cost):
        super().__init__(description, cost) #super fonksiyonu ile pizza sınıfının özelliklerini kullanıyoruz
        self.component =companent

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self) #soslar ve pizza tabanlarının fiyatlarını toplayan fonksiyon

    def get_description(self):
        return self.component.get_description() + " " + Pizza.get_description(self)#soslar ve pizza tabanlarının açıklamlarının birleştiren


class Olives(Decarator):
    def __init__(self,component):
        super().__init__(component, "Özel zeytinlerle pizzanızı tadlandırın", 15) #Decarator ana classımızın özelliklerini kullanrak soslara ait sabit değişkenleri tanımladık



class Mushrooms(Decarator):
    def __init__(self,component):

        super().__init__(component,"Özel mantarlarla pizzanızı tadlandırın",13)


class GoatCheese(Decarator):
    def __init__(self,component):

        super().__init__(component,"Özel keçi peyniri lezzetini pizzada yaşayaın",20)



class Meat(Decarator):
    def __init__(self,component):

        super().__init__(component,"Özel Dana Etlerimizle pizzanızı tadlandırın",25)



class Onions(Decarator):
    def __init__(self,component):

        super().__init__(component,"Soğan severlerele özel ekstra soğan",10)



class Corn(Decarator):
    def __init__(self, component):
        super().__init__(component,"Mısırlarla pizzanıza hem lezzet hemde görsel şölen yaşatın",12)


#Seçilen pizza tabanın menüye uygunluğunu kontrol etmemizi sağlayan fonksiyon
def kontrolPizza(a):
    if a not in ["1", "2", "3", "4"]:
        print("Hatalı Pizza Seçimi Yaptınız")
    else:
        pass
#Sos seçiminde menüye uygun değer girilidiğini kontrol etmemizi sağlayan fonksiyon
def kontrolSos(b):
    if b not in ["11", "12", "13", "14",
                 "15", "16", "17"]:
        print("Hatalı Sos Seçimi Yaptınız")
    else:
        pass

# Ana fonksiyonumuzda menüyü ekran yazdırcak değerleri kontrol edecek ve sonuçları oluştrulan dosyaya yazdırcak aşamlardan oluşmaktadır
def main():


    menu = open("Menu.txt", "r", encoding="UTF-8") #Proje dosyasında yer alan Menumüzü uygulama ile açmamızı ve ekrana yazdıramamızı sağlayan kısım burda tanımlanmıştır.
    print(menu.read())
    #Döngü şeklinde pizza tabanımızının seçimini istenilen uygunulukta yapamızı sağlayacak
    while True:
        pizzaSecim = input("Lütfen Pizza Taban seçinizi giriniz:") #Menüdeki pizza tabanlarından yapacağımızı seçim için programa bizim yazacağımız seçim.
        if pizzaSecim== "1":
            pizza=Margarita()
            break
        elif pizzaSecim== "2":
            pizza=Turkpizza()
            break
        elif pizzaSecim== "3":
            pizza=PlainPizza()
            break
        elif pizzaSecim== "4":
            pizza=Salami()
            break
        else:
            kontrolPizza(pizzaSecim)
    # Menüdeki soslardan yapacağımızı seçim için programa bizim yazacağımız seçim.
    while True:
        sosSecim = input("Lütfen Sos seçiminiz Giriiniz")
        if sosSecim=="11":
            sos=Olives(pizza)
            break
        elif sosSecim=="12":
            sos=Mushrooms(pizza)
            break
        elif sosSecim=="13":
            sos=GoatCheese(pizza)
            break
        elif sosSecim=="14":
            sos=Meat(pizza)
            break
        elif sosSecim=="15":
            sos=Onions(pizza)
            break

        elif sosSecim=="16":
            sos=Corn(pizza)
            break
        else:
            kontrolSos(sosSecim)


    totali=sos.get_cost() # sos ve pizza ücretlerini Topladağımız.
    acikalama =sos.get_description()#sos ve pizza açıklamlarını birleştiren kısım.

    print(acikalama)

    print("Ödeme İşlemleri için Bilgiler girmeniz gerekmektedir")

    isim = input("Lütfen İsiminizi Giriniz:")
    kimlikNo = input("Lütfen Kimlik Numaranızı Giriniz")
    krediKartNo = input("Lütfen Kredi Kartı Numaranızı Giriniz")
    krediKartSifre = input("Lütfen Şifrenizi Giriniz")
    zaman = datetime.datetime.now() #İşlem zamanını veritabanı yazdırmamızı sağlayacak
    with open("OrderDatabes.csv", "w", newline='', encoding="UTF-8") as database:#Veri tabanını programa okutup yazdırmamızı sağlayan metod
        musteriBilgi = csv.writer(database)
        musteriBilgi.writerow(([isim, kimlikNo, krediKartNo, krediKartSifre, acikalama, zaman,totali]))

if __name__ == '__main__': #Programaı çalıştırmamızı sağlayan
    main()



