"""
Clients that get word definitions
"""
import logging
from abc import ABC, abstractmethod

from language_service.dto.definition import DefinitionSchema

definition_schema = DefinitionSchema(many=True)
logger = logging.getLogger("LanguageService.client")


class DefinitionClient(ABC):
    """
    Base class to cache definitions in elasticsearch.

    To use:
    Override fetch_definitions(language, word) with your source implementation
    And call super().__init__(name) with the name of your source
    """

    def __init__(self, source):
        self.source = source

    def get_definitions(self, language, word):
        logger.info(
            "Getting definitions in %s for %s using %s" % (language, word, self.source)
        )

        definitions = self.fetch_definitions(language, word)

        return definitions

    @abstractmethod
    def fetch_definitions(self, language, word):
        """
        Implement this to actually get the definition
        """
        raise NotImplementedError("Definition client class didn't implement this")
