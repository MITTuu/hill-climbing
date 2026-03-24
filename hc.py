import utils
import math


# def get_move_weight(map, hospital):
#     houses = utils.find_object(map, utils.OBJECT_HOUSE)
#     cost, coordinate = (math.inf, ())
#
#     for house in houses:
#         temp_cost = utils.manhattan(
#             hospital,
#             house,
#         )
#
#         if temp_cost < cost:
#             cost = temp_cost
#             coordinate =
#
#     return cost, coordinate


def hill_climbing(map):
    current_map = map
    current_cost = utils.cost(map)
    last_cost = math.inf

    while current_cost != last_cost:
        last_cost = current_cost

        for hospital in utils.find_objects(current_map, utils.OBJECT_HOSPITAL):
            neighbors = utils.actions(current_map, hospital)

            for temp_hospital_move in neighbors:
                temp_map = utils.result(current_map, hospital, temp_hospital_move)
                temp_cost = utils.cost(temp_map)

                if current_cost > temp_cost:
                    current_cost = temp_cost
                    current_map = temp_map

                    neighbors = utils.actions(current_map, hospital)

    return current_map
