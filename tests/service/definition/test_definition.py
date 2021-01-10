import pytest

from language_service.dto.definition import Definition
from language_service.service.definition import get_definitions


this_definition = Definition(token="This", subdefinitions=["This"])
is_definition = Definition(token="is", subdefinitions=["is"])
a_definition = Definition(token="a", subdefinitions=["a"])
test_definition = Definition(token="test", subdefinitions=["test"])


def get_definitions_successfully_mock(word):
    if word == "This":
        return this_definition
    elif word == "is":
        return is_definition
    elif word == "a":
        return a_definition
    elif word == "test":
        return test_definition


def get_definitions_with_failures_mock(word):
    if word == "This":
        return this_definition
    elif word == "is":
        return None
    elif word == "a":
        return a_definition
    elif word == "test":
        return None


def test_can_pass_through_english_definitions(mocker):
    english = mocker.patch(
        "language_service.service.definition.get_english_definitions"
    )
    english.return_value = "any"

    assert get_definitions("ENGLISH", "any") == "any"

    english.assert_called_once_with("any")


def test_raises_exception_on_unknown_language(mocker):
    with pytest.raises(NotImplementedError):
        get_definitions("LAO", "ສິ່ງໃດກໍ່ຕາມ")
