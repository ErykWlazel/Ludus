"""ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]"""


def missing_elements(table: list[int], size: int) -> list[int] | None:
    for i in table:
        if type(i) != int:
            return None
    if type(size) == int and size > 0:
        if max(table) <= size and min(table) > 0:
            c = []
            for i in range(1, size + 1):
                if i not in table:
                    c.append(i)
            return c
    return None


def test_size_is_not_int():
    assert missing_elements([1, 3, 4, 1, 2], "12.2c") == None
    assert missing_elements([1, 3, 4, 1, 2], 7.3) == None
    assert missing_elements([1, 3, 4, 1, 2], True) == None
    assert missing_elements([1, 3, 4, 1, 2], [7]) == None
    assert missing_elements([1, 3, 4, 1, 2], (8,)) == None


def test_table_element_or_size_out_of_range():
    assert missing_elements([1, 3, 4, 1, 2], -2) == None
    assert missing_elements([1, 3, 4, 1, 2], 0) == None
    assert missing_elements([1, 3, 4, 1, 2], 2) == None
    assert missing_elements([1, 3, -4, 1, 2], 7) == None


def test_table_element_not_int():
    assert missing_elements([1, 3.2, 4, 1, 2], 9) == None
    assert missing_elements([1, 3, "2d", 1, 2], 9) == None
    assert missing_elements([1, 3, 4, [1], 2], 9) == None


def test_correct_input_and_output():
    assert missing_elements([1, 3, 4, 5, 7], 9) == [2, 6, 8, 9]
    assert missing_elements([1, 2, 4, 5, 7], 12) == [3, 6, 8, 9, 10, 11, 12]
