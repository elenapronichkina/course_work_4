from src.api import HeadHunterAPI, SuperJobAPI
def user_interaction():
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    hh_vacancies = hh_api.get_vacancies()
    sj_vacancies = superjob_api.get_vacancies()
    user_platform = input("Введите название сайта:")
        if user_platform not in ["HeadHunter", "SuperJob"]:
            print("Сайт недоступен")
        else:
            word_vacancy = input("Введите наименование вакансии:")










#Создать функцию для взаимодействия с пользователем.
# Функция должна взаимодействовать с пользователем через консоль.
# Самостоятельно придумать сценарии и возможности взаимодействия с пользователем.
# Например, позволять пользователю указать, с каких платформ он хочет получить вакансии,
# ввести поисковый запрос, получить топ N вакансий по зарплате, получить вакансии в отсортированном виде,
# получить вакансии, в описании которых есть определенные ключевые слова, например "postgres" и т. п

## Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter", "SuperJob"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
#
#     if not filtered_vacancies:
#         print("Нет вакансий, соответствующих заданным критериям.")
#         return
#
#     sorted_vacancies = sort_vacancies(filtered_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)