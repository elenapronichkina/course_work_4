
class Vacancy:
    def __init__(self, vacancy_id):
        self._vacancy_id = vacancy_id
        self.vacancy_url = f'https://hh.ru/vacancy/{self._vacancy_id}'  # ссылка на вакансию
        self.title = self.vacancy["items"]["name"]  # название вакансии
        self.salary = self.vacancy["items"]["salary"] #зарплата
        self.requirement = self.vacancy["items"]['snippet']['requirement'] #требования

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