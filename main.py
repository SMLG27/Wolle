import web
import read_excel


if __name__ == '__main__':
    ExcelProduktList = read_excel.ExcelData()  # Object Created
    ExcelProduktList.produkt_l()
    produkt_listt = ExcelProduktList.produkt_list
    for counter, prod_it in enumerate(produkt_listt):
        Web = web.WebRequestSoup(prod_it,
                                 ExcelProduktList.produkt_only_name[counter])  # Object Created
        HtmlData = web.SearchDataInHtml(ExcelProduktList.produkt_only_name[counter],
                                        Web.soup, prod_it)  # Object Created

        Web.request_status_code()
        Web.soup_objekt_chceck()
        HtmlData.produckt_name_check()
        HtmlData.product_name_print()
        HtmlData.produkt_price()
        HtmlData.produkt_specyfi()
