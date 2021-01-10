from testfixtures import compare

from language_service.controller.definition import DefinitionController
from language_service.dto.definition import Definition

test_first_subdefinitions = ["test (plural tests)", "A challenge, trial."]
test_second_subdefinitions = [
    "test (third-person singular simple present tests, present participle testing, simple past and past participle tested)",
    "To challenge.",
]
noun_tag = "noun"
test_first_examples = ["This is a test", "This is a second test"]
test_second_examples = ["This is a third test", "This is a fourth test"]

test_definitions_input = [
    Definition(
        token="test",
        subdefinitions=test_first_subdefinitions,
        tag=noun_tag,
        examples=test_first_examples,
    ),
    Definition(
        token="test",
        subdefinitions=test_second_subdefinitions,
        tag=noun_tag,
        examples=test_second_examples,
    ),
]
test_definitions_output = [{'examples': ['This is a test', 'This is a second test'],
                            'language': 'ENGLISH',
                            'source': 'WIKTIONARY',
                            'subdefinitions': ['test (plural tests)', 'A challenge, trial.'],
                            'tag': 'noun',
                            'token': 'test'},
                           {'examples': ['This is a third test', 'This is a fourth test'],
                            'language': 'ENGLISH',
                            'source': 'WIKTIONARY',
                            'subdefinitions': ['test (third-person singular simple present tests, '
                                               'present participle testing, simple past and past '
                                               'participle tested)',
                                               'To challenge.'],
                            'tag': 'noun',
                            'token': 'test'}]

experiment_subdefinitions = [
    "experiment (plural experiments)",
    "A test under controlled conditions made to either demonstrate a known truth, examine the validity of a hypothesis, or determine the efficacy of something previously untried.",
    "(obsolete) Experience, practical familiarity with something.",
]
experiment_examples = [
    "South Korean officials announced last month that an experiment to create artificial rain did not provide the desired results.\nAudio ",
    "Audio ",
    "Pilot [...] Vpon his card and compas firmes his eye, / The maisters of his long experiment, / And to them does the steddy helme apply [...].",
]

experiment_definitions_input = [
    Definition(
        token="experiment",
        subdefinitions=experiment_subdefinitions,
        tag=noun_tag,
        examples=experiment_examples,
    )
]
experiment_definitions_output = [
    {
        "subdefinitions": experiment_subdefinitions,
        "tag": noun_tag,
        "examples": experiment_examples,
    },
]


def test_single_definition_controller(mocker):
    controller = DefinitionController()

    get_definition = mocker.patch(
        "language_service.controller.definition.get_definitions"
    )
    get_definition.return_value = test_definitions_input

    result, status = controller.get(language="ENGLISH", word="test")

    assert status == 200
    compare(result, test_definitions_output)