import sys
# from typing import Any, List
#
# from src.parser import HH
# from src.json_worker import WorkWithJson
from src.user_interactive import UserInteractive
from src.vacancy import Vacancy

if __name__ == "__main__":

    print("Hello, user")
    user_name = input("Как ваше имя?  ")
    user = UserInteractive(user_name)

    keyword = input("Введите запрос (ключевое слово для поиска вакансий на HH): ")

    user.save_file(user.get_vacancies_list(keyword))

    YesNo = input("\nФайл с вакансиями сформирован.\nУдалить файл с найденными вакансиями? "
                  "\nЕсли удаляем, то выходим из программы!\n"
                  "(Д/д, Y/y - удаляем и выходим, Н/н, N/n - продолжаем работу): ")
    if YesNo == "Y" or YesNo == "y" or YesNo == "Д" or YesNo == "д":
        user.delete_file()
        sys.exit()

    n = int(input("\nСколько вакансий вывести на экран (введите число): "))
    print()

    user.get_vacancies_list_from_file()
    new_vac_list = []
    for vacancy in user.vacancies_list:
        vac = Vacancy.new_vacancy(vacancy)

        new_vac_list.append(vac)

    user.vacancies_list = new_vac_list
    # for vacancy in user.vacancies_list:
    #     print(vacancy)
    user.get_top_n_for_salary(n)
    for vacancy in user.get_top_n_for_salary(n):
        print(vacancy)
        print()

    print("------------------------------------------------------------------")
    for vacancy in user.get_vacancy_from_keywords():
        print(vacancy)
        print()
