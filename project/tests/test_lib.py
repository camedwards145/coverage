from project.src.fizzbuzz import fizzbuzz

def test_fizz():
    result = fizzbuzz(3)
    assert result == "Fizz"

def test_buzz():
    result = fizzbuzz(5)
    assert result == "Buzz"
