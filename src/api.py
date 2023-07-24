import requests
import json
import os
from abc import ABC, abstractmethod

class APIKey(ABC):
    @abstractmethod
    def api(self):
        pass
#     api_key: str = os.getenv('API_KEY_YT')
#     youtube = build('youtube', 'v3', developerKey=api_key)
class HeadHunterAPI(APIKey):
    pass

class SuperjobAPI(APIKey):
    pass

# Создать абстрактный класс для работы с API сайтов с вакансиями.
# Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами.
# Классы должны уметь подключаться к API и получать вакансии.