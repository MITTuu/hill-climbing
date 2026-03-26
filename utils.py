import copy

OBJECT_EMPTY = None
OBJECT_HOUSE = "🏠"
OBJECT_HOSPITAL = "🏥"


MOVE_UP = (0, -1)
MOVE_DOWN = (0, 1)
MOVE_LEFT = (-1, 0)
MOVE_RIGHT = (1, 0)


def is_free_to_move(map, move):
    """
    Check whether a target position is empty and can be moved into.

    Args:
        map: Matrix (list of lists) representing the board.
        move: Position as (x, y), where x is horizontal and y is vertical.

    Returns:
        bool: True if the target cell is empty (None), False otherwise.
    """
    x, y = move
    return map[y][x] == None


def is_valid_move(map, move):
    """
    Check whether a position is inside the matrix boundaries.

    Args:
        map: Matrix (list of lists) representing the board.
        move: Position as (x, y), where x is horizontal and y is vertical.

    Returns:
        bool: True if the position is within bounds, False otherwise.
    """
    x, y = move
    x_bound: int = len(map[0]) - 1  
    y_bound: int = len(map) - 1     

    return (0 <= x <= x_bound) and (0 <= y <= y_bound)


def find_objects(map, target_object_symbol):
    """
    Find all coordinates where a given object symbol appears.

    Args:
        map: Matrix (list of lists) representing the board.
        target_object_symbol: Symbol to search for (None, 🏠, or 🏥).

    Returns:
        list[tuple[int, int]]: All matching coordinates as (x, y).
    """
    list_cords = []

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == target_object_symbol:
                list_cords.append((j,i))

    return list_cords


def result(map, hospital_coordinates, target_move):
    """
    Create and return a new map after moving one hospital to a target position.

    Args:
        map: Matrix (list of lists) representing the board.
        hospital_coordinates: Current hospital position as (x, y).
        target_move: Destination position as (x, y).

    Returns:
        list[list]: A deep-copied map with the move applied.
    """
    new_map = copy.deepcopy(map)
    x_hospital, y_hospital = hospital_coordinates
    x_target, y_target = target_move

    new_map[y_target][x_target] = OBJECT_HOSPITAL
    new_map[y_hospital][x_hospital] = None

    return new_map


def manhattan(pos, pos_2):
    """
    Compute the Manhattan distance between two coordinates.

    Args:
        pos: First coordinate as (x, y).
        pos_2: Second coordinate as (x, y).

    Returns:
        int: Distance computed as abs(x2 - x1) + abs(y2 - y1).
    """
    x_1, y_1 = pos
    x_2, y_2 = pos_2

    return abs(x_2 - x_1) + abs(y_2 - y_1)


def cost(map):
    """
    Compute total cost as the sum of distances from each hospital to each house.

    Args:
        map: Matrix (list of lists) representing the board.

    Returns:
        int: Total Manhattan-distance cost.
    """
    hospitals = find_objects(map, OBJECT_HOSPITAL)
    houses = find_objects(map, OBJECT_HOUSE)

    cost = 0
    for hospital in hospitals:
        for house in houses:
            cost += manhattan(hospital, house)
    
    return cost


def move(pos, pos_2):
    """
    Add two coordinates component-wise.

    Args:
        pos: First coordinate as (x, y).
        pos_2: Second coordinate as (x, y).

    Returns:
        tuple[int, int]: New coordinate as (x1 + x2, y1 + y2).
    """
    x_1, y_1 = pos
    x_2, y_2 = pos_2

    return (x_1 + x_2, y_1 + y_2)


def actions(map, hospital_position):
    """
    Return all valid adjacent moves for a hospital in up, down, left, right order.

    Args:
        map: Matrix (list of lists) representing the board.
        hospital_position: Hospital coordinate as (x, y).

    Returns:
        list[tuple[int, int]]: Valid neighboring positions that are in bounds and free.
    """
    actions = []
    x_hospital, y_hospital = hospital_position
    
    moves = [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]

    for dx, dy in moves:
        new_x = x_hospital + dx
        new_y = y_hospital + dy

        if 0 <= new_y < len(map) and 0 <= new_x < len(map[0]):
            if map[new_y][new_x] is None:
                actions.append((new_x, new_y))        

    return actions
