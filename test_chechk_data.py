import unittest
import web
import read_excel


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.ExcelData = read_excel.ExcelData
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
