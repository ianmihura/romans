from roman import roman_to_int, int_to_roman

# int_to_roman
assert int_to_roman(9) == "IX"
assert int_to_roman(12) == "XII"
assert int_to_roman(123) == "CXXIII"
assert int_to_roman(567) == "DLXVII"
assert int_to_roman(890) == "DCCCXC"
assert int_to_roman(9999) == "MX̅CMXCIX"

# roman_to_int
assert roman_to_int("IX") == 9
assert roman_to_int("XII") == 12
assert roman_to_int("CXXIII") == 123
assert roman_to_int("DLXVII") == 567
assert roman_to_int("DCCCXC") == 890
assert roman_to_int("CMXCIX") == 999
