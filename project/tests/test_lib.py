from project.src.fizzbuzz import fizzbuzz

def test_fizz():
    result = fizzbuzz(3)
    assert result == "Fizz"
