import pytest
from unittest.mock import MagicMock


from language_service.controller.common import check_language


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
