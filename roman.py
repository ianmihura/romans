
def int_to_roman(num: int) -> str:
    """Input range: 1 to 9999"""

    def mapping(decimal_place: str) -> dict:
        """
        Mapping of basic digits that make up the decimal place.
        For example, first decimal place is made up of (I, V, X)
        """
        (uni, mid, max) = [
            ("I", "V", "X"),  # 1 - 9
            ("X", "L", "C"),  # 10 - 99
            ("C", "D", "M"),  # 100 - 999
            ("M", "V̅", "X̅"),  # 1000 - 9999
        ][decimal_place]

        return {
            "0": "",
            "1": uni,
            "2": uni * 2,
            "3": uni * 3,
            "4": uni + mid,  # or uni * 4
            "5": mid,
            "6": mid + uni,
            "7": mid + uni * 2,
            "8": mid + uni * 3,
            "9": uni + max,
            "10": max,
        }

    roman = ""
    for decimal_place, decimal in enumerate(str(num)[::-1]):
        roman = mapping(decimal_place)[decimal] + roman

    return roman


def roman_to_int(roman: str) -> int:
    """Input range: I to MX̅CMXCIX"""

    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "V̅": 5000,
        "X̅": 10000,
    }

    num = 0
    prev = ""
    for r in roman[::-1]:
        if prev and mapping[r] < mapping[prev]:
            num = num - mapping[r]
        else:
            num = num + mapping[r]
        prev = r

    return num
