import eel
import requests
from bs4 import BeautifulSoup


@eel.expose
def Dollars_Rub(rub):
    """Функция возвращает курс доллара.
       Отправляет запрос в Google, по результатам запроса парсит сайт,
       где находит занчение курса и это значение возвращает.
       Чтобы google не заблокировал запрос при частом запросе, стоит User-Agent.

       Требуется соединение с интернетом.
    """
    #TODO НЕОБХОДИМО ДОБАВИТЬ ОБРАБОТКУ ОШИБКИ СОЕДИНЕНИЯ
    
    DOLLAR_RUB ='https://www.google.ru/search?client=opera&q=доллары+в+рубли&sourceid=opera&ie=UTF-8&oe=UTF-8'
    headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.79'}
    full_page= requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "2"})
    #print ("1$ = "+convert[0].text+" рублей")
    return ("Сейчас 1 бакс это " + convert[0].text + " ,сука, рублей!")
    
# Необходимо указать путь
eel.init("E:\Python\Interface_eel\web")

eel.start("main.html", size=(700, 700))
