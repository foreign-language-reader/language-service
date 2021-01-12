import pytest
from testfixtures import compare
from language_service.service.tag import tag
from language_service.dto.word import Word


def test_can_tag_chinese():
    words = tag("CHINESE", "测试已通过，因为返回了这些单词。")
    compare(
        words,
        [
            Word(token="测试", tag="NOUN", lemma="测试"),
            Word(token="已", tag="ADV", lemma="已"),
            Word(token="通过", tag="VERB", lemma="通过"),
            Word(token="因为", tag="ADP", lemma="因为"),
            Word(token="返回", tag="VERB", lemma="返回"),
            Word(token="了", tag="PART", lemma="了"),
            Word(token="这些", tag="DET", lemma="这些"),
            Word(token="单词", tag="NOUN", lemma="单词"),
        ],
    )


def test_chinese_tagging_no_duplicates():
    words = tag(
        "CHINESE",
        "石室诗士施氏，嗜狮，誓食十狮。氏时时适市视狮。十时，适十狮适市。 是时，适施氏适市。氏视是十狮，恃矢势，使是十狮逝世。氏拾是十狮尸，适石室。石室湿，氏使侍拭石室。石室拭，氏始试食是十狮尸。食时，始识是十狮，实十石狮尸。试释是事。",
    )
    compare(
        words,
        [
            Word(token="石室", tag="PROPN", lemma="石室"),
            Word(token="诗士", tag="NOUN", lemma="诗士"),
            Word(token="施氏", tag="VERB", lemma="施氏"),
            Word(token="嗜狮", tag="NOUN", lemma="嗜狮"),
            Word(token="誓食", tag="VERB", lemma="誓食"),
            Word(token="十狮", tag="NUM", lemma="十狮"),
            Word(token="氏时", tag="NOUN", lemma="氏时"),
            Word(token="时适市", tag="NOUN", lemma="时适市"),
            Word(token="视狮", tag="VERB", lemma="视狮"),
            Word(token="十时", tag="NUM", lemma="十时"),
            Word(token="适", tag="VERB", lemma="适"),
            Word(token="十", tag="NUM", lemma="十"),
            Word(token="狮", tag="NUM", lemma="狮"),
            Word(token="适市", tag="VERB", lemma="适市"),
            Word(token="是时", tag="VERB", lemma="是时"),
            Word(token="适施", tag="VERB", lemma="适施"),
            Word(token="氏", tag="NOUN", lemma="氏"),
            Word(token="氏视", tag="PROPN", lemma="氏视"),
            Word(token="是", tag="VERB", lemma="是"),
            Word(token="恃", tag="NOUN", lemma="恃"),
            Word(token="矢势", tag="VERB", lemma="矢势"),
            Word(token="使", tag="VERB", lemma="使"),
            Word(token="逝世", tag="NOUN", lemma="逝世"),
            Word(token="氏拾", tag="ADV", lemma="氏拾"),
            Word(token="狮尸", tag="VERB", lemma="狮尸"),
            Word(token="适石室", tag="VERB", lemma="适石室"),
            Word(token="湿", tag="NOUN", lemma="湿"),
            Word(token="氏使", tag="NOUN", lemma="氏使"),
            Word(token="侍拭", tag="NOUN", lemma="侍拭"),
            Word(token="拭", tag="VERB", lemma="拭"),
            Word(token="氏始", tag="ADV", lemma="氏始"),
            Word(token="试食", tag="VERB", lemma="试食"),
            Word(token="食时", tag="NOUN", lemma="食时"),
            Word(token="始识", tag="NOUN", lemma="始识"),
            Word(token="实十", tag="ADJ", lemma="实十"),
            Word(token="石", tag="ADV", lemma="石"),
            Word(token="试释", tag="NOUN", lemma="试释"),
            Word(token="事", tag="NOUN", lemma="事"),
        ],
    )


def test_can_tag_english():
    words = tag("ENGLISH", "The test has passed because these words were returned.")
    compare(
        words,
        [
            Word(token="The", tag="DET", lemma="the"),
            Word(token="test", tag="NOUN", lemma="test"),
            Word(token="has", tag="AUX", lemma="have"),
            Word(token="passed", tag="VERB", lemma="pass"),
            Word(token="because", tag="SCONJ", lemma="because"),
            Word(token="these", tag="DET", lemma="these"),
            Word(token="words", tag="NOUN", lemma="word"),
            Word(token="were", tag="AUX", lemma="be"),
            Word(token="returned", tag="VERB", lemma="return"),
        ],
    )


def test_english_tagging_no_duplicates():
    words = tag(
        "ENGLISH", "This is the song that never ends, it goes on and on my friends"
    )
    compare(
        words,
        [
            Word(token="This", tag="DET", lemma="this"),
            Word(token="is", tag="AUX", lemma="be"),
            Word(token="the", tag="DET", lemma="the"),
            Word(token="song", tag="NOUN", lemma="song"),
            Word(token="that", tag="DET", lemma="that"),
            Word(token="never", tag="ADV", lemma="never"),
            Word(token="ends", tag="VERB", lemma="end"),
            Word(token="it", tag="PRON", lemma="-PRON-"),
            Word(token="goes", tag="VERB", lemma="go"),
            Word(token="on", tag="ADP", lemma="on"),
            Word(token="and", tag="CCONJ", lemma="and"),
            Word(token="my", tag="DET", lemma="-PRON-"),
            Word(token="friends", tag="NOUN", lemma="friend"),
        ],
    )


def test_can_tag_spanish():
    words = tag(
        "SPANISH", "La prueba ha pasado porque estas palabras fueron devueltas."
    )
    compare(
        words,
        [
            Word(token="La", tag="DET", lemma="La"),
            Word(token="prueba", tag="NOUN", lemma="probar"),
            Word(token="ha", tag="AUX", lemma="haber"),
            Word(token="pasado", tag="VERB", lemma="pasar"),
            Word(token="porque", tag="SCONJ", lemma="porque"),
            Word(token="estas", tag="DET", lemma="este"),
            Word(token="palabras", tag="NOUN", lemma="palabra"),
            Word(token="fueron", tag="VERB", lemma="ser"),
            Word(token="devueltas", tag="VERB", lemma="devolver"),
        ],
    )


def test_spanish_tagging_no_duplicates():
    words = tag("SPANISH", "Hola, mi llamo Lucas. Hola Lucas")
    compare(
        words,
        [
            Word(token="Hola", tag="PROPN", lemma="Hola"),
            Word(token="mi", tag="DET", lemma="mi"),
            Word(token="llamo", tag="NOUN", lemma="llamar"),
            Word(token="Lucas", tag="PROPN", lemma="Lucas"),
        ],
    )


def test_raises_exception_on_unknown_language():
    with pytest.raises(NotImplementedError):
        tag("KLINGON", "We can't handle this sentence")
