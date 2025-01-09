def romanToInt(s: str) -> int:
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    present_value = 0

    for char in reversed(s):
        if roman_dict[char] < present_value:
            total -= roman_dict[char]
        else:
            total += roman_dict[char]
        present_value = roman_dict[char]

    return total
