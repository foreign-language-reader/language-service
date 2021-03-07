import es_core_news_sm
from language_service.dto.word import Word

parser = es_core_news_sm.load()


def tag_spanish(text):
    return [
        Word(token=word.text, tag=word.pos_, lemma=word.lemma_) for word in parser(text)
    ]
