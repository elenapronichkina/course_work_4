import json
from src.api import HeadHunterAPI
class Vacancy:
    def __init__(self, vacancy_url, title, salary, requirement):
        self.vacancy_url = self.data["items"]['alternate_url']  # ссылка на вакансию
        self.title = self.data["items"]["name"]  # название вакансии
        self.salary = self.data["items"]["salary"] #зарплата
        self.requirement = self.data["items"]['snippet']['requirement'] #требования

    def to_json(self, filename):
        """сохраняет в файл значения атрибутов экземпляра Vacancy"""
        data = {
            "title": self.title,
            "url": self.vacancy_url,
            "salary": self.salary,
            "requirement": self.requirement,
             }
        with open(filename, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def list_vacancies(self):
        """получение списка вакансий"""
        vacancies = []
        vacancy = Vacancy()
        vacancies.append(vacancy)
        return vacancies

    def __str__(self):
        """возвращает название и ссылку на вакансию"""
        return f"{self.title} ({self.vacancy_url})"

    def __lt__(self, other):
        """сравнение по зарплате"""
        return self.salary < other.salary


#Создать класс для работы с вакансиями.
# В этом классе самостоятельно определить атрибуты, такие как
# название вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т.п.
# (не менее четырех)
# Класс должен поддерживать методы сравнения вакансий между собой по зарплате и
# валидировать данные, которыми инициализируются его атрибуты.
#должен быть реализован в соответствии с принципом инкапсуляции и п
# оддерживать методы сравнения вакансий между собой по зарплате

# Создание экземпляра класса для работы с вакансиями
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>",
# "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)