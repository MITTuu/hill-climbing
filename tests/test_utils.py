import copy

import pytest

import utils


def test_is_valid_move_uses_xy_order_not_yx():
    board = [[None] * 4 for _ in range(3)]

    assert utils.is_valid_move(board, (3, 2)) is True
    assert utils.is_valid_move(board, (2, 3)) is False


@pytest.mark.parametrize("move", [(-1, 0), (0, -1), (4, 0), (0, 3)])
def test_is_valid_move_rejects_out_of_bounds(move):
    board = [[None] * 4 for _ in range(3)]

    assert utils.is_valid_move(board, move) is False


def test_is_free_to_move_reads_coordinates_as_xy():
    board = [
        [None, None],
        [utils.OBJECT_HOUSE, None],
        [None, None],
    ]

    assert utils.is_free_to_move(board, (0, 1)) is False
    assert utils.is_free_to_move(board, (1, 0)) is True


def test_find_objects_returns_coordinates_in_xy_scan_order():
    board = [
        [utils.OBJECT_HOUSE, None, utils.OBJECT_HOUSE],
        [None, utils.OBJECT_HOSPITAL, None],
        [utils.OBJECT_HOUSE, None, utils.OBJECT_HOSPITAL],
    ]

    assert utils.find_objects(board, utils.OBJECT_HOUSE) == [(0, 0), (2, 0), (0, 2)]
    assert utils.find_objects(board, utils.OBJECT_HOSPITAL) == [(1, 1), (2, 2)]


def test_result_moves_hospital_and_does_not_mutate_original_map():
    board = [
        [utils.OBJECT_HOSPITAL, None],
        [None, utils.OBJECT_HOUSE],
    ]
    before = copy.deepcopy(board)

    moved = utils.result(board, (0, 0), (1, 0))

    assert moved == [[None, utils.OBJECT_HOSPITAL], [None, utils.OBJECT_HOUSE]]
    assert board == before
    assert moved is not board


def test_manhattan_returns_expected_distance():
    assert utils.manhattan((0, 0), (3, 4)) == 7


def test_cost_sums_all_hospital_house_pairs():
    board = [
        [utils.OBJECT_HOSPITAL, None, utils.OBJECT_HOUSE],
        [None, None, None],
        [utils.OBJECT_HOUSE, None, utils.OBJECT_HOSPITAL],
    ]

    assert utils.cost(board) == 8


def test_cost_is_zero_when_no_houses_or_hospitals():
    board_no_houses = [[utils.OBJECT_HOSPITAL, None]]
    board_no_hospitals = [[utils.OBJECT_HOUSE, None]]

    assert utils.cost(board_no_houses) == 0
    assert utils.cost(board_no_hospitals) == 0


def test_move_adds_two_positions_component_wise():
    assert utils.move((2, 3), utils.MOVE_LEFT) == (1, 3)
    assert utils.move((2, 3), utils.MOVE_UP) == (2, 2)


def test_actions_filters_invalid_or_occupied_moves_and_keeps_order():
    board = [
        [None, None, None],
        [utils.OBJECT_HOUSE, utils.OBJECT_HOSPITAL, None],
        [None, utils.OBJECT_HOUSE, None],
    ]

    assert utils.actions(board, (1, 1)) == [(1, 0), (2, 1)]


def test_actions_returns_empty_list_for_far_outside_coordinate_failure_case():
    board = [[utils.OBJECT_HOSPITAL]]

    assert utils.actions(board, (99, 99)) == []
