def search4vowels(word: str) -> set:
    """ Display any vowels found in the input word """
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(pharse: str, letters: str = 'aeiou') -> set:
    """ Return a set of letters found in the pharse """
    return set(letters).intersection(set(pharse))
