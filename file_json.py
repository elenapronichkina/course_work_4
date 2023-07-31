import json
def read_json(file_path):
    """
    читает файл json и возвращает его содержимое
    return: данные, список словарей
    """
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_json(file_path, data):
    """Запись данных в файл в формате JSON"""
    with open(file_path, 'w') as f:
        json.dump(data, f, ensure_ascii=True, indent=2)
