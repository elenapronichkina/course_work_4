import requests
import json
import os
from abc import ABC, abstractmethod
# Создать абстрактный класс для работы с API сайтов с вакансиями.
# Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами.
# Классы должны уметь подключаться к API и получать вакансии.
class APIKEY(ABC):
    def __init__(self, url, params):
        self.url = url
        self.params = params
       #api_key: str = os.getenv('API_KEY_YT')
    @abstractmethod
    def get_vacancies(self):
        response = requests.get(url, params=params)
        data = response.json()
        return data
class HeadHunterAPI(APIKEY):
    url = https://api.hh.ru/vacancies/
    params = {
            'text': 'NAME:word_vacancy', # Текст фильтра. В имени должно быть наименование вакансии
            'area': 1, # Поиск ощуществляется по вакансиям города Москва #113 - по России
            'page': page, # Индекс страницы поиска на HH начинается с 0. Значение по умолчанию 0, т.е. первая страница
            'per_page': 100 # Кол-во вакансий на 1 странице
        }
# headhunter_api = HeadHunterAPI()
# headhunter_api.get_vacancies()

#   def get_page(page = 0):
    #     """
    #     метод для получения страницы со списком вакансий.
    #     """
  #      req = requests.get('https://api.hh.ru/vacancies', params) # запрос к API
 #       data = req.content.decode() # Декодируем его ответ, чтобы Кириллица отображалась корректно
  #      req.close()
   #     return data
#
 #Считываем первые 2000 вакансий
#for page in range(0, 20):

    # Преобразуем текст ответа запроса в справочник Python
#    jsObj = json.loads(get_page(page))
## Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
    # Определяем количество файлов в папке для сохранения документа с ответом запроса
    # Полученное значение используем для формирования имени документа
    #nextFileName = './docs/pagination/{}.json'.format(len(os.listdir('./docs/pagination')))

    # Создаем новый документ, записываем в него ответ запроса, после закрываем
  #  f = open(nextFileName, mode='w', encoding='utf8')
  #  f.write(json.dumps(jsObj, ensure_ascii=False))
  #  f.close()
class SuperjobAPI(APIKEY):
    #access_token = v3.r.137702272.d9fb18907e74e64bafbab0b5f26a5ba34e121367.2e76017ab5def4f4b11596df0f549e0b1cc7a16e
    # https://api.superjob.ru/2.0/vacancies/?access_token
    # https://api.superjob.ru/:version/method_name/:params

    url = https://api.superjob.ru/2.0/vacancies/:params
    params = {
        'keyword': 'NAME:word_vacancy',  # Текст фильтра. В имени должно быть наименование вакансии
        'town': 1,  # Поиск ощуществляется по вакансиям города Москва #113 - по России
        'page': page,  # номер страницы поиска, начинается с 0. Значение по умолчанию 0, т.е. первая страница
        'count': 100  # Кол-во результатов на страницу поиска. Максимальное число результатов - 100
    }