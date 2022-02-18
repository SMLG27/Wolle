import requests
from bs4 import BeautifulSoup
import re
import decoo_save_data


class WebRequestSoup:

    def __init__(self, product, produkt_only_n):
        # https://www.wollplatz.de/#sqr:(q[DMC%20Natura%20XL])
        self.url_liferung = "https://www.wollplatz.de/versandkosten-und-lieferung"
        self.url_w = "https://www.wollplatz.de/wolle/" + produkt_only_n.lower() + "/" + product.lower()
        self.web_req = requests.get(self.url_w)
        self.soup = BeautifulSoup(self.web_req.text, "html.parser")
        self.searching = None
        self.prod_name = product
        self.product_first_name = produkt_only_n

    def request_status_code(self):
        return self.web_req.status_code

    def soup_objekt_chceck(self):
        return "Objekt Erstellt" if self.soup else "Objekt nicht erstellt"


class SearchDataInHtml:

    def __init__(self, produkt, soup_objekt, produkt_name):
        self.all_url = None
        self.soupp = soup_objekt
        self.product_speci = None
        self.prod_nam = produkt
        self.prduct_v_name = produkt_name

    def produckt_name_check(self):
        chceckk = re.search(self.prod_nam, self.soupp.text)
        chceckk_two = re.search(self.prod_nam, self.soupp.text)
        return self.prduct_v_name if chceckk or chceckk_two \
            else f"Produkt ist nicht in Html Datei ,{self.prduct_v_name}"  # check if produkt in html

    @decoo_save_data.sav_data # save data in data.txt
    def product_name_print(self):
        return self.prduct_v_name

    @decoo_save_data.sav_data
    def produkt_price(self):
        try:
            produkt_pric = self.soupp.find(class_="product-price").text  # drop the product price
            price = f"Produkt Preis: {produkt_pric}"
            return price
        except AttributeError:
            print(f"{self.prduct_v_name}: price unavailable")

    @decoo_save_data.sav_data
    def produkt_specyfi(self):
        produkt_l = []  # list with produkt specify
        try:
            self.product_speci = self.soupp.find("div", id="pdetailTableSpecs").table  # searching for id with specify
            for e in self.product_speci.find_all("tr", recursive="True"):  # drop the specify if available
                if e.td.text == "Zusammenstellung" or e.td.text == "Nadelstärke":
                    produkt_l.append(e.td.text + ": " + e.td.next_sibling.text + "\n")  # append specify in list
            return "".join(produkt_l)
        except AttributeError:
            print(f"{self.prduct_v_name}: specify unavailable ")

    def versand_kosten(self):
        pass
        # regex_link = r"https?:\/\/.*[\r\n]*liferung"
