import pytest
from unittest.mock import MagicMock


from language_service.controller.common import (
    check_language,
    get_required_field,
)


def test_check_language(mocker):
    # Make sure we always require the language
    assert (None, "Language is required") == check_language(None)
    assert (None, "Language is required") == check_language("")

    # Check an unsupported language
    assert (None, "Language Klingon is not supported") == check_language("Klingon")

    # Check supported languages
    assert ("CHINESE", None) == check_language("CHINESE")
    assert ("ENGLISH", None) == check_language("ENGLISH")
    assert ("SPANISH", None) == check_language("SPANISH")

    # Check lowercase languages
    assert ("CHINESE", None) == check_language("chinese")
    assert ("ENGLISH", None) == check_language("english")
    assert ("SPANISH", None) == check_language("spanish")


def test_get_required_field_no_json(mocker):
    request = mocker.patch("language_service.controller.common.request")
    request.get_json.return_value = None

    assert (None, "Field my_field is required") == get_required_field(
        request, "my_field"
    )


def test_get_required_field_missing_field(mocker):
    request = mocker.patch("language_service.controller.common.request")
    request.get_json.return_value = {}

    assert (None, "Field my_field is required") == get_required_field(
        request, "my_field"
    )


def test_get_required_field_field_is_present(mocker):
    request = mocker.patch("language_service.controller.common.request")
    request.get_json.return_value = {"my_field": True}

    assert (True, None) == get_required_field(request, "my_field")
