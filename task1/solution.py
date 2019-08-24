from task1.sample_mealdata import MEAL_DATA
from pprint import pprint


def get_matching_meals(meal_data=MEAL_DATA, food_ids=[]):
    """Returns all the meal IDs in meal_data that have all of the given food IDs.

    Args:
        meal_data: list of dictionary of meals (check sample_mealdata.py for sample)
        meal_data = [ ...
                    {
                        'meal_id': 1,
                        'foods': [
                            {
                                'food_id': 1,
                                'food_name': 'Idli'
                            },
                            {
                                'food_id': 10,
                                'food_name': 'Sambar'
                            },
                        ]
                    },
                    ....
                ]

        food_ids: list of food IDs.
        food_ids = [10]


    Returns:
        list of int: The matching meal IDs

    """
    typecasted_food_ids = __validate_food_ids(food_ids)

    meals_by_food_id = __transpose_by_food_id(meal_data, typecasted_food_ids)
    """
    - extra all the values (meal_ids) from the dict eg. [[1, 2, 3], [1, 3, 4]]
    - use this 2D array as input for set operations
    - find intersection between multiple food id to find cover meals which have all the food ids
    - convert it back into a list for consumption
    """
    meals_present_in_all_foods = list(set.intersection(*map(set, meals_by_food_id.values())))

    return meals_present_in_all_foods


# helpers
def __validate_food_ids(food_ids):
    """

    :param food_ids:
    :return:
    """
    if not isinstance(food_ids, (list, tuple)):
        raise ValueError("Validation Error: Food ID should be present in a `list` format!")

    try:
        food_ids = list(map(int, food_ids))
    except ValueError:
        raise ValueError("Validation Error: Seems like you pass a non numerical value as a Food ID!")

    return food_ids


def __transpose_by_food_id(meal_data, selective_food_ids=[]):
    """

    :param meal_data:
    :param food_ids:
    :return: {1: [1, 2, 3], 10: [1, 3, 4]}
            key: food_id
            value: list of meal_ids

    """
    transposed_data = dict()

    for enum, current_meal_data in enumerate(meal_data):

        meal_id = current_meal_data.get('meal_id')
        foods_in_a_meal = current_meal_data.get('foods')

        for enum, food in enumerate(foods_in_a_meal):
            current_food_id = food.get('food_id')

            # do not transpose the entire data set if selective food ids are provided to reduce overhead
            if selective_food_ids and current_food_id not in selective_food_ids:
                continue

            meals_attached = transposed_data.get(current_food_id)

            if not meals_attached:
                transposed_data[current_food_id] = [meal_id]
            else:
                transposed_data[current_food_id].append(meal_id)

    return transposed_data
