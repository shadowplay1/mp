import VacancyManager

vacancy_manager = VacancyManager('data/vacancy.csv')
vacancy_with_least_employees = vacancy_manager.get_vacancy_with_least_employees()

print(f'В компании {vacancy_with_least_employees[4]} есть заданная профессия: {vacancy_with_least_employees[3]}, з/п в такой компании составит: {vacancy_with_least_employees[0]}')
