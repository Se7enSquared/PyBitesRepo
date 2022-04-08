import pytest

from workouts import print_workout_days, WORKOUTS


@pytest.mark.parametrize(
    "n, expected",
    [("upper body #1", "Mon\n"), ("30", "Wed\n"), ("upper", "Mon, Thu")],
)
def test_print_workout_days(capsys, n, expected):
    print_workout_days(n)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_bad_inputs(capsys):
    print_workout_days("bad input")
    captured = capsys.readouterr()
    assert captured.out == "No matching workout\n"


def test_all_days_in_dict():
    assert ["mon", "tue", "wed", "thu", "fri"] == list(WORKOUTS.keys())


def test_all_workouts_in_dict():
    assert [
        "upper body #1",
        "lower body #1",
        "30 min cardio",
        "upper body #2",
        "lower body #2",
    ] == list(WORKOUTS.values())


def test_comma_sep(capsys):
    print_workout_days("upper")
    captured = capsys.readouterr()
    assert ", " in captured.out
