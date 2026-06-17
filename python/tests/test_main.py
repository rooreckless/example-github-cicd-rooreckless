# from ...python.modules.main import fizz_buzz
from python.modules.main import fizz_buzz
def test_fizz_buzz_fizzbuzz():
    assert fizz_buzz(15) == "fizzbuzz"
def test_fizz_buzz_fizz():
    assert fizz_buzz(2) == "fizz"
def test_fizz_buzz_other():
    assert fizz_buzz("a") == "unknown"