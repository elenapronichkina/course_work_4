import requests
import json
import os
from abc import ABC, abstractmethod

class APIKey(ABC):
    def __init__(self, url, params):
        self.url = url
        self.params = params
       #api_key: str = os.getenv('API_KEY_YT')
    @abstractmethod
    def get_vacancies(self):
        response = requests.get(url, params=params)
        data = response.json()

class HeadHunterAPI(APIKey):
       url = https://api.hh.ru/vacancies
    # def get_page(page = 0):
    #     """
    #     метод для получения страницы со списком вакансий.
    #     """
         params = {
        'text': 'NAME:word_vacancy', # Текст фильтра. В имени должно быть наименование вакансии
        'area': 1, # Поиск ощуществляется по вакансиям города Москва
        'page': page, # Индекс страницы поиска на HH начинается с 0. Значение по умолчанию 0, т.е. первая страница
        'per_page': 100 # Кол-во вакансий на 1 странице
        }

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
class SuperjobAPI(APIKey):
    pass

# Создать абстрактный класс для работы с API сайтов с вакансиями.
# Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами.
# Классы должны уметь подключаться к API и получать вакансии.