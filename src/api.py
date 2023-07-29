from pprint import pprint
import requests
import json
import os
from abc import ABC, abstractmethod
# Создать абстрактный класс для работы с API сайтов с вакансиями.
# Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами.
# Классы должны уметь подключаться к API и получать вакансии.
class APIKEY(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass

class HeadHunterAPI(APIKEY):
    def __init__ (self, word_vacancy):
        self.__word_vacancy = word_vacancy
    url = "https://api.hh.ru/vacancies/"
    def get_vacancies(self):
        """
           метод для получения страницы со списком вакансий.
        """
        params = {
            'text': self.__word_vacancy,  # Текст фильтра. В имени должно быть наименование вакансии
            'area': 113,  # Поиск ощуществляется по вакансиям города Москва #113 - по России
            'page': 0,  # Индекс страницы поиска на HH начинается с 0. Значение по умолчанию 0, т.е. первая страница
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        response = requests.get(self.url, params=params)
        data = response.json()
        return data

# hh_1 = HeadHunterAPI("Python")
# pprint(hh_1.get_vacancies())

class SuperjobAPI(APIKEY):
    access_token = "v3.r.137702272.d9fb18907e74e64bafbab0b5f26a5ba34e121367.2e76017ab5def4f4b11596df0f549e0b1cc7a16e"
    # api_key: str = os.getenv('API_KEY_YT')
    url = "https://api.superjob.ru/2.0/vacancies/:params"

    def __init__(self, word_vacancy):
        self.__word_vacancy = word_vacancy
    def get_vacancies(self):
        """
            метод для получения страницы со списком вакансий.
        """
        params = {
        'keyword': self.__word_vacancy,  # Текст фильтра. В имени должно быть наименование вакансии
        'town': 1,  # Поиск ощуществляется по вакансиям города Москва #1 - по России
        'page': 0,  # номер страницы поиска, начинается с 0. Значение по умолчанию 0, т.е. первая страница
        'count': 100  # Кол-во результатов на страницу поиска. Максимальное число результатов - 100
        }

        headers = {
            "X-Api-App-Id": access_token
        }
        response = requests.get(self.url, headers=headers, params=params)
        data = response.json()
        return data

    # sj_1 = SuperjobAPI("Python")
    # pprint(sj_1.get_vacancies())