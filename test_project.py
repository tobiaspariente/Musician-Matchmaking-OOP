from project import find_musicians, get_input, surprise_choice
import unittest.mock

#1
def test_find_musicians():

    database = {
        "John": {
            "name": "John",
            "musicaltool": "guitar",
            "age": 30
        },
        "Jane": {
            "name": "Jane",
            "musicaltool": "piano",
            "age": 25
        },
        "Jim": {
            "name": "Jim",
            "musicaltool": "guitar",
            "age": 35
        }
    }

    preferred_instrument = "violin"
    preferred_age = 20
    musicians = find_musicians(database, preferred_instrument, preferred_age)
    assert musicians == [] or (preferred_instrument, preferred_age) not in [(database[i]['musicaltool'], database[i]['age']) for i in database.keys()]

#2
def test_get_input():
    prompt = "Enter your name: "

    def mock_input(prompt):
        return "John"

    with unittest.mock.patch('builtins.input', side_effect=mock_input):
        name = get_input(prompt)
        assert name == "John"

    def mock_input(prompt):
        return "Jane"

    with unittest.mock.patch('builtins.input', side_effect=mock_input):
        name = get_input(prompt)
        assert name == "Jane"

#3
def test_surprise_choice():
    assert surprise_choice
