import mock
import pytest
import builtins
from src.pkg.password_generator import *


def test_get_user_input():
    with mock.patch.object(builtins, "input", lambda _: "3"):
        character_count = get_user_input("Enter character count: ")
        assert character_count == 3
        assert type(character_count) == int


@pytest.fixture
def get_character_counts():
    return {
        "letters_count": 3,
        "symbols_count": 4,
        "numbers_count": 5,
    }


def test_append_characters_to_password(get_character_counts):
    letters_count = get_character_counts["letters_count"]
    password = append_characters_to_password(letters_count, letters, [])
    assert len(password) == letters_count
    assert all([character in letters for character in password])


def test_shuffle_characters():
    characters = list("afa2!#$%jl78")
    shuffled = shuffle_characters(characters)
    assert len(shuffled) == len(characters)
    assert type(shuffled) == list
    for character in shuffled:
        assert character in characters


def test_join_characters():
    original_string = "jl2lj42!&*)"
    characters = list(original_string)
    joined_string = join_characters(characters)
    assert joined_string == original_string

