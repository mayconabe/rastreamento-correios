from bs4 import BeautifulSoup
from lxml import etree
from urllib.request import urlopen

codigo_rastreamento = input("Código de rastreamento: ")


try:
    # Lib usage
    url = "https://websro.com.br/rastreamento-correios.php?P_COD_UNI=" + codigo_rastreamento
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    dom = etree.HTML(str(soup))
    data = soup.find("td")

    # All data formated
    date = data.get_text()[0:10]
    hour = data.get_text()[10:15]
    object_status = dom.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/table/tbody/tr[1]/td[2]/strong')[0].text
    position = dom.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/table/tbody/tr[1]/td[2]/text()')[0].strip()

    # All data being printed
    print("----------------------------------- Status/Localidade --------------------------------")
    print(f'Data: {date}            {object_status}'.center(24, " "))
    print(f'Hora: {hour}        {position}'.center(30, " "))
    print("--------------------------------------------------------------------------------------")
except:
    print("--------------------------------------------------------------------------------------")
    print("Objeto não encontrado. Talvez você digitado alguma coisa errada :(")
    print("--------------------------------------------------------------------------------------")