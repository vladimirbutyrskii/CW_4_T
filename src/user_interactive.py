from src.json_worker import WorkWithJson
from src.parser import HH


class UserInteractive(WorkWithJson):

    def __init__(self, user_name):
        super().__init__()
        self.user_name = user_name
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword):
        hh = HH(keyword)
        return hh.load_vacancies()

    def get_vacancies_list_from_file(self):
        work_file = WorkWithJson()
        self.vacancies_list = []
        for vac in work_file.read_file():
            self.vacancies_list.append(vac)
        return self.vacancies_list

    def get_top_n_for_salary(self, n):

        vac_filter = []
        for vac in self.vacancies_list:
            vac_filter.append(vac)

        sort_by_salary = sorted(vac_filter, key=lambda x: x.salary, reverse=True)
        return sort_by_salary[:n]

    def get_vacancy_from_keywords(self):
        keywords = input("Введите ключевые слова:  ")  # .split() сделано для одного
        res = []
        for vacancy in self.vacancies_list:
            if vacancy.name.find(keywords) != -1:
                res.append(vacancy)

        return res
