from definitions import Vacancy
from typing import Union

def compare_numbers(vacancy1: Vacancy, vacancy2: Vacancy, column_index) -> bool:
    return vacancy1[column_index] - vacancy2[column_index]

def vacancies_quick_sort(vacancies: list[Vacancy], column_index: Union[0, 1, 2, 3, 4]) -> list[Vacancy]:
    if len(vacancies) <= 1:
        return vacancies

    pivot_vacancy = vacancies[len(vacancies) // 2]

    left = [vacancy for vacancy in vacancies if compare_numbers(vacancy, pivot_vacancy, column_index) < 0]
    middle = [vacancy for vacancy in vacancies if compare_numbers(vacancy, pivot_vacancy, column_index) == 0]
    right = [vacancy for vacancy in vacancies if compare_numbers(vacancy, pivot_vacancy, column_index) > 0]

    return vacancies_quick_sort(left, column_index) + middle + vacancies_quick_sort(right, column_index)
