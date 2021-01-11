from marshmallow import Schema, fields


class Word:
    def __init__(self, token="", tag="", lemma="", definitions=None):  # nosec this is not a password
        if definitions is None:
            definitions = []
        self.token = token
        self.tag = tag
        self.lemma = lemma
        self.definitions = definitions

    def __repr__(self):
        return "Word(token: %s, tag: %s, lemma: %s, definitions: %s)" % (
            self.token,
            self.tag,
            self.lemma,
            self.definitions
        )


class WordSchema(Schema):
    token = fields.Str()
    tag = fields.Str()
    lemma = fields.Str()
    definitions = fields.List(fields.Str())
