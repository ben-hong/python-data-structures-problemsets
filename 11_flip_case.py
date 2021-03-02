def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapchar = to_swap.lower()
    list = []
    string = ''

    for char in phrase:
        if char.isupper() and swapchar == char.lower():
            string += char.lower()
        elif char.islower() and swapchar == char:
            string += char.upper()
        else:
            string += char
    
    return string

print(flip_case('AaaaAhh', 'a'))
