import logging

from flask_restful import Resource

from language_service.controller.common import check_language
from language_service.dto.definition import DefinitionSchema
from language_service.service.definition import get_definitions

definition_schema = DefinitionSchema(many=True)
logger = logging.getLogger("LanguageService")


class DefinitionController(Resource):
    def get(self, language=None, word=None):
        language, error = check_language(language)
        if error:
            return {"error": error}, 400

        if word is None or word == "":
            return {"error": "Word is required"}, 400

        logger.info("Getting definition in %s for %s" % (language, word))

        definitions = get_definitions(language, word)
        return definition_schema.dump(definitions), 200
