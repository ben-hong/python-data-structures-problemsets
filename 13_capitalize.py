def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    return list(phrase)[0].upper() + ''.join(list(phrase)[1:])


print(capitalize('python'))
