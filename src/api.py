import requests
import os
from abc import ABC, abstractmethod


class APIKEY(ABC):
    """абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(APIKEY):
    """класс для работы с API сайта с вакансиями HeadHunter:
        подключается к API и получает вакансии"""

    def __init__(self, word_vacancy):
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


class SuperjobAPI(APIKEY):
    """класс для работы с API сайта с вакансиями SuperJob:
            подключается к API и получает вакансии"""

    access_token = os.getenv('API_KEY_SJ')
    url = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self, word_vacancy):
        self.__word_vacancy = word_vacancy

    def get_vacancies(self):
        """
            метод для получения страницы со списком вакансий.
        """
        params = {
            'keyword': self.__word_vacancy,  # Текст фильтра. В имени должно быть наименование вакансии
            'page': 0,  # номер страницы поиска, начинается с 0. Значение по умолчанию 0, т.е. первая страница
            'count': 100  # Кол-во результатов на страницу поиска. Максимальное число результатов - 100
        }

        headers = {
            "X-Api-App-Id": self.access_token
        }
        response = requests.get(self.url, headers=headers, params=params)
        data = response.json()
        return data
