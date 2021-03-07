import zh_core_web_sm
from language_service.dto.word import Word
from language_service.service.tag.common import is_not_punctuation

parser = zh_core_web_sm.load()


def tag_chinese(text):
    return [
        Word(token=word.text, tag=word.pos_, lemma=word.lemma_)
        for word in parser(text)
        if is_not_punctuation(word.text)
    ]
