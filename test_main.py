import main

#python -m pytest test_main.py


def test_kulka():
    result = main.charivna_kulka('can i fly?')
    expected_answers = ['yes', 'no', 'maybe']
    assert result in  expected_answers
    assert type(result) == str
    assert result is not 'You didnt ask question'
    result_invalid = main.charivna_kulka(42)
    assert result_invalid == 'invalid input'



