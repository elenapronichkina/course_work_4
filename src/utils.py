from file_json import write_json
from src.api import HeadHunterAPI, SuperjobAPI
from src.vacancies import Vacancy


def user_interaction():
    """функция для взаимодействия с пользователем"""
    word_vacancy = input("Введите наименование вакансии:")
    hh_api = HeadHunterAPI(word_vacancy)
    superjob_api = SuperjobAPI(word_vacancy)

    hh_vacancies = hh_api.get_vacancies()
    sj_vacancies = superjob_api.get_vacancies()
    vacancies = []
    for vacancy in hh_vacancies["items"]:
        item = Vacancy.vacancy_from_hh(vacancy)
        vacancies.append(item)

    for vacancy in sj_vacancies["objects"]:
        item = Vacancy.vacancy_from_sj(vacancy)
        vacancies.append(item)

    vacancies_to_json = []
    for vacancy in vacancies:
        vacancy_in_json = vacancy.to_json()
        vacancies_to_json.append(vacancy_in_json)

    write_json("vacancies.json", vacancies_to_json)

    print("Введите 1, чтобы отсортировать вакансии по зарплате\n"
          "Введите 2, чтобы вывести топ вакансий")
    user_input = input()
    if user_input == "1":
        sorted_vacancies = sorted(vacancies)
        for vacancy in sorted_vacancies:
            print(vacancy)

    if user_input == "2":
        print("Введите количество вакансий для списка топ")
        user_input_top = input()
        sorted_vacancies = sorted(vacancies, reverse=True)
        for vacancy in sorted_vacancies[0:int(user_input_top)]:
            print(vacancy)
