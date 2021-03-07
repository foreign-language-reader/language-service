import zh_core_web_sm
from language_service.dto.word import Word

parser = zh_core_web_sm.load()


def tag_chinese(text):
    # Lemmatization is not meaningful for Chinese because there are no conjugations.
    return [
        Word(token=word.text, tag=word.pos_, lemma=word.text) for word in parser(text)
    ]
