"""
Where you put definition business logic.
We combine different data sources as available to deliver the best definitions.
"""
import logging

from language_service.service.definition.english import get_english_definitions

logger = logging.getLogger("LanguageService.service.definition")


def get_definitions(language, word):
    """
    Main entry point for getting definitions, letting us dispatch to the correct language.
    Why? Each language has different definition sources, so they'll have their
        own combination logic.
    """
    if language == "ENGLISH":
        return get_english_definitions(word)

    else:
        raise NotImplementedError("Unknown language requested: %s")
