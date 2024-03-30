from definitions import Vacancy
from typing import Union

def partition(vacancies: list[Vacancy], low: int, high: int, column_index: Union[0, 1, 2, 3, 4]) -> int:
    pivot = vacancies[high][column_index]
 
    i = low - 1
 
    for j in range(low, high):
        if vacancies[j][column_index] <= pivot:
 
            i = i + 1
 
            (vacancies[i][column_index], vacancies[j][column_index]) = (vacancies[j][column_index], vacancies[i][column_index])
 
    (vacancies[i + 1][column_index], vacancies[high][column_index]) = (vacancies[high][column_index], vacancies[i + 1][column_index])
    return i + 1


def vacancies_quick_sort(vacancies: list[Vacancy], low: int, high: int, column_index: Union[0, 1, 2, 3, 4]):
    if low < high:
        pi = partition(vacancies, low, high, column_index)

        vacancies = vacancies_quick_sort(vacancies, pi + 1, high, column_index)
    
    return vacancies
