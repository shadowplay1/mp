import csv

from definitions import Vacancy
from quick_sort import vacancies_quick_sort

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


    '''
    Получение вакансии с наименьшим количеством сотрудников.
        - Сортировка всех вакансий от меньшего к большему по количеству сотрудников с помощь алгоритма быстрой сортировки
        - Возвращение первого элеменента отсортированного списка
    '''
    def get_vacancy_with_least_employees(self) -> Vacancy:
        vacancies_with_no_header = self.vacancies[1:]
        sorted_vacancies = vacancies_quick_sort(vacancies_with_no_header, 0, len(vacancies_with_no_header) - 1, 2)

        return sorted_vacancies[0]
    
    '''
    Запуск консольного поиска по всем вакансиям
        - Создание бесконечного цикла, внутри которого:
            - спрашивается название компании
            - все вакансии фильтруются по указанной компании
            - если было введено слово "none" (регистр не важен), то программа закрывается
            - если вакансия не найдена, то выводится соответствующее сообщение
            - в ином случае, вывод всех вакансий указанной компании 
    '''
    def start_console_searching(self) -> None:
        vacancies_with_no_header = self.vacancies[1:]

        while True:
            input_company_name = input('Введите название компании: ')
            filtered_compaines = list(filter(lambda company: company[4] == input_company_name, vacancies_with_no_header))

            if input_company_name.lower() == 'none':
                break

            if not len(filtered_compaines):
                print('К сожалению, ничего не удалось найти')

            for vacancy in filtered_compaines:
                print(f'В {vacancy[4]} найдена вакансия: {vacancy[3]}. З/п составит: {vacancy[0]}')
