from marshmallow import Schema, fields


class Definition:
    def __init__(
        self, token, source="wiktionary", language="english", subdefinitions=None, tag="", examples=None
    ):
        """
        subdefinitions: The different definitions for this meaning of the word
        tag: The part of speech
        examples: This word definition used in a sentence
        """
        self.subdefinitions = subdefinitions
        self.tag = tag
        self.examples = examples
        self.token = token
        self.source = source
        self.language = language

    def set_subdefinitions(self, subdefinitions):
        self.subdefinitions = subdefinitions

    def __repr__(self):
        return "Definition(subdefinitions: %s, tag: %s, examples: %s)" % (
            self.subdefinitions,
            self.tag,
            self.examples,
        )


def make_definition_object(definition):
    return Definition(**definition)


class DefinitionSchema(Schema):
    token = fields.Str()
    source = fields.Str()
    language = fields.Str()
    subdefinitions = fields.List(fields.Str())
    tag = fields.Str()
    examples = fields.List(fields.Str())
    pinyin = fields.Str()
    simplified = fields.Str()
    traditional = fields.Str()
    hsk = fields.Integer()
