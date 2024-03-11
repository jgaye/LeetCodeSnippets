import csv
import src


def test_successful_pairs():
    with open("spells.csv", newline="") as csvfile:
        spells = [list(map(int, rec)) for rec in csv.reader(csvfile, delimiter=",")][0]
    with open("potions.csv", newline="") as csvfile:
        potions = [list(map(int, rec)) for rec in csv.reader(csvfile, delimiter=",")][0]
    with open("expected.csv", newline="") as csvfile:
        expected = [list(map(int, rec)) for rec in csv.reader(csvfile, delimiter=",")][
            0
        ]

    assert (
        src.Solution().successful_pairs(
            spells=spells, potions=potions, success=5433930978
        )
        == expected
    )
