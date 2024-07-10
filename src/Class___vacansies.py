class Vacansies:
    """
    Класс для работы с вакансиями полученными в файл.
    """
    def __init__(self, name, area, salary_from, salary_to, salary_currency, requirement, responsibility, url):
        self.name = self.__get_data_validation(name)
        self.area = self.__get_data_validation(area)
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.requirement = self.__get_data_validation(requirement)
        self.responsibility = self.__get_data_validation(responsibility)
        self.url = self.__get_data_validation(url)

    def __str__(self):
        return (f"Название вакансии: {self.name}, Город: {self.area},"
                f"Зарплата: {self.salary_from} - {self.salary_to}{self.salary_currency}, \n"
                f"Требования к соискателю: {self.requirement}, Обязанности соискателя: {self.responsibility},\n"
                f"URl вакансии: {self.url}")

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    @staticmethod
    def __get_data_validation(data):
        if data:
            return data
        else:
            return "Нет данных!"

    @classmethod
    def add_new_vacancy(cls, vacancy_):
        name = vacancy_.get("name")
        area = vacancy_.get("area").get("name")
        if vacancy_.get("salary"):
            if vacancy_.get("salary").get("from"):
                salary_from = vacancy_.get("salary").get("from")
            else:
                salary_from = 0
            if vacancy_.get("salary").get("to"):
                salary_to = vacancy_.get("salary").get("to")
            else:
                salary_to = "Верхний порог не указан."
            salary_currency = vacancy_.get("salary").get("currency")
        else:
            salary_from = 0
            salary_to = "Верхний порог не указан."
            salary_currency = ""
        requirement = vacancy_.get("snippet").get("requirement")
        responsibility = vacancy_.get("snippet").get("responsibility")
        url = vacancy_.get("alternate_url")
        return cls(name, area, salary_from, salary_to, salary_currency, requirement, responsibility, url)




