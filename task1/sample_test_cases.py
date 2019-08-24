# Sample test cases:
from task1.solution import get_matching_meals
from task1.sample_mealdata import MEAL_DATA


def _check(test_name, food_ids, meal_ids):
    if get_matching_meals(MEAL_DATA, food_ids) == meal_ids:
        print('Test %s passed! :)' % test_name)
    else:
        print('Test %s failed! :(' % test_name)


def test_1():
    # Because meal IDs 1, 2 and 3 all have a food with ID 1.
    _check('Test1', food_ids=[1], meal_ids=[1, 2, 3])


def test_2():
    # Because meal IDs 2 and 3 all have a food with ID 11.
    _check('Test2', food_ids=[11], meal_ids=[2, 3])


def test_3():
    # Because meal IDs 1 and 3 have both the given foods with IDs 1 and 10.
    _check('Test3', [1, 10], [1, 3])


def run_all_tests():
    test_1()
    test_2()
    test_3()


run_all_tests()
