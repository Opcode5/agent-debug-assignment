import pytest
from agent.agent import call_LLM

@pytest.mark.parametrize("dummy", [0], ids=["dictionary tool type should be calc when % presents in the question"])
def test_dictionary_when_percentage_is_in_the_question(dummy):
    question = "What is 12.5% of 243?"
    out = call_LLM(question)

    expected_output = {'tool': 'calc', 'args': {'expr': f'{question.lower()}'}}
    assert(out==expected_output)
    
@pytest.mark.parametrize("dummy", [0], ids=["dictionary tool type should be calc when add/subtract/multiply/divide presents in the question"])
def test_dictionary_when_operator_is_in__the_question(dummy):
    question = "Add 10 to the average temperature of dhaka."
    out = call_LLM(question)

    expected_output = {'tool': 'calc', 'args': {'expr': f'{question.lower()}'}}
    assert(out==expected_output)

@pytest.mark.parametrize("dummy", [0], ids=["dictionary tool type should be weather when temperature/weather presents in the question"])
def test_dictionary_when_temperature_or_weather_is_in__the_question(dummy):
    question = "temperature of dhaka."
    out = call_LLM(question)

    expected_output = {'tool': 'weather', 'args': {'city': 'dhaka'}}
    assert(out==expected_output)
    
@pytest.mark.parametrize("dummy", [0], ids=["dictionary tool type should be summarized weather when summarized word presents in the question"])
def test_dictionary_when_summarized_is_in__the_question(dummy):
    question = "Summarize today's weather in Paris in 3 words."
    out = call_LLM(question)

    expected_output = {'tool': 'summarized weather', 'args': {'city': 'paris'}}
    assert(out==expected_output)

@pytest.mark.parametrize("dummy", [0], ids=["dictionary tool type should be kb weather when who is presents in the question"])
def test_dictionary_when_who_is_in__the_question(dummy):
    question = "Who is Ada Lovelace?"
    out = call_LLM(question)

    expected_output = {'tool': 'kb', 'args': {'name': ['ada lovelace']}}
    assert(out==expected_output)

@pytest.mark.parametrize("dummy", [0], ids=["dictionary tool type should be kb convert when convert presents in the question"])
def test_dictionary_when_convert_is_in__the_question(dummy):
    question = "convert 300 g to kg"
    out = call_LLM(question)

    expected_output = {'tool': 'convert', 'args': {'expr': f'{question.lower()}'}}
    assert(out==expected_output)
