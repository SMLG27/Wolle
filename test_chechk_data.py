import unittest
import web
import read_excel


class RequestTest(unittest.TestCase):

    def setUp(self):
        self.ExcelData = read_excel.ExcelData()

    def test_excel_data(self):
        list_ex = ['DMC-Natura-XL', 'Drops-Safran', 'Drops-Baby-Merino-Mix',
                   'Hahn-Alpacca-Speciale', 'Stylcraft-Special-double-knit']
        self.assertEqual(self.ExcelData.produkt_l(), list_ex)


class DataWebTest(unittest.TestCase):

    def setUp(self):
        self.WebReqObject = web.WebRequestSoup("dmc-natura-xl", "dmc")
        self.SearchDataObject = web.SearchDataInHtml("dmc", self.WebReqObject.soup, "DMC-Natura-XL")

    def test_request_code(self):
        self.assertEqual(self.WebReqObject.request_status_code(), 200)

    def test_ob_check(self):
        self.assertEqual(self.WebReqObject.soup_objekt_chceck(), "Objekt Erstellt")

    def test_produkt_name_check(self):
        self.assertEqual(self.SearchDataObject.produckt_name_check(), "DMC-Natura-XL")

    def test_produkt_pric(self):
        self.assertEqual(self.SearchDataObject.produkt_price(), None)

    def test_produkt_speci(self):
        self.assertEqual(self.SearchDataObject.produkt_specyfi(), None)


if __name__ == '__main__':
    unittest.main()
