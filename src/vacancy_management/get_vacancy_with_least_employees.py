from ..definitions import Vacancy
from ...src import VacancyManager

vacancy_manager = VacancyManager('data/vacancy.csv')

sorted_vacancies = vacancy_manager.get_vacancies_with_least_employees()
required_vacancy_name = 'классный руководитель'

vacancy_with_least_employees: Vacancy = list(filter(lambda vacancy: vacancy[3].lower() == required_vacancy_name, sorted_vacancies))[0]
print(f'В компании {vacancy_with_least_employees[4]} есть заданная профессия: {vacancy_with_least_employees[3]}, з/п в такой компании составит: {vacancy_with_least_employees[0]}')
