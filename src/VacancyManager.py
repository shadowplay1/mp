'''
  (0)     (1)         (2)      (3)    (4) 
Salary;Work_Type;Company_Size;Role;Company
47200;стажер;26801;менеджер по социальным сетям;Icahn Enterprises
'''

'''
Вы поняли, что хотите сначала проанализировать какие профессии самые востребованные и высокооплачиваемые в
 разных компаниях. Для этого создайте таблицу vacancy_new.csv 
 в которую запишите три столбца company, role, Salary. 
 При этом сама вакансия(Role) должна иметь максимальный размер зарплаты в компании. 
 После этого выведите топ-3 самых высокооплачиваемых профессий в формате: <компания> - <вакансия> - <зарплата>
'''

import csv

from definitions import Vacancy
from quick_sort import quick_sort

class VacancyManager:
    '''
    Инициализация класса:
        - Инициализируем класс VacancyManager;
        - Переводим все числовые значения из типа строки в числовой тип;
        - Сохраняем данные файла внутри класса.

    Аргументы:
        - database_file_path (str): путь к csv-файлу с данными
    '''
    def __init__(self, database_file_path: str) -> None:
        self.database_file_path = database_file_path
        self.vacancies: list[Vacancy] = []

        vacancies = list(csv.reader(open(self.database_file_path, encoding='utf-8'), delimiter=';'))

        for line in range(len(vacancies)):
            for item in range(len(vacancies[line])):
                if vacancies[line][item].isdigit():
                    vacancies[line][item] = int(vacancies[line][item])
        
        self.vacancies = vacancies


    '''
    Запись лучших вакансий по зарплате и вывпод первых 3 в консоль.
        - Сортировка данных по зарплате
        - Получение первых 3 вакансий
        - Создание и открытие нового файла в режиме записи с указанныым названием по указанному пути
        - Запись данных в файл
        - Вывод первых 3 вакансий в консоль
    
    Аргументы:
        - new_database_file_path (str): путь к новому csv-файлу, где будут записаны отсортированные данные
    '''
    def write_best(self, new_database_file_path: str) -> None:
        sorted_vacancies = list(reversed(sorted(self.vacancies[1:], key=lambda i: i[0])))
        first_3 = sorted_vacancies[:3]

        new_file = csv.writer(open(new_database_file_path, encoding='utf-8', mode='w'), delimiter=';')

        new_file.writerow(self.vacancies[0])
        new_file.writerows(sorted_vacancies)

        print('Топ-3 востребованных вакансий:\n')

        for item in first_3:
            company = item[4]
            role = item[3]
            salary = item[0]

            print(f'{company} - {role} - {salary}')


    def print_vacancy_with_least_employees(self) -> None:
        salaries: list[int]



vacancy_manager = VacancyManager('data/vacancy.csv')
vacancy_manager.write_best('data/vacancy_new.csv')