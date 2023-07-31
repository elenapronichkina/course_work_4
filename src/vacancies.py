class Vacancy:
    """класс для работы с вакансиями"""

    def __init__(self, vacancy_url, title, salary, requirement):
        self.vacancy_url = vacancy_url  # ссылка на вакансию
        self.title = title  # название вакансии
        self.salary = salary  # зарплата
        self.requirement = requirement  # требования

    def to_json(self):
        """сохраняет в файл значения атрибутов экземпляра Vacancy"""
        data = {
            "title": self.title,
            "url": self.vacancy_url,
            "salary": self.salary,
            "requirement": self.requirement,
        }
        return data

    @classmethod
    def vacancy_from_hh(cls, data):
        """получение списка вакансий HH.ru"""
        vacancy_url = data['alternate_url']
        title = data["name"]  # название вакансии
        salary = data["salary"]  # зарплата
        if salary:
            salary = data["salary"]["from"]
            if not salary:
                salary = 0
        else:
            salary = 0

        requirement = data['snippet']['requirement']  # требования
        vacancy = cls(vacancy_url, title, salary, requirement)
        return vacancy

    @classmethod
    def vacancy_from_sj(cls, data):
        """получение списка вакансий SJ.ru"""
        vacancy_url = data['link']
        title = data["profession"]  # название вакансии
        salary = data["payment_from"]  # зарплата
        if not salary:
            salary = 0
        requirement = data['candidat']  # требования
        vacancy = cls(vacancy_url, title, salary, requirement)
        return vacancy

    def __str__(self):
        """возвращает название и ссылку на вакансию"""
        return f"{self.title} ({self.vacancy_url})"

    def __lt__(self, other):
        """сравнение по зарплате: от меньшего к большему"""
        return self.salary < other.salary
