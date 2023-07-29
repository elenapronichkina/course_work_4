import json
def read_json(file_path):
    """
    читает файл json и возвращает его содержимое
    return: данные, список словарей
    """
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

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


