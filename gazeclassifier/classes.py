
str_to_int = {
    'unknown': 0,
    'saccade': 1,
    'fixation': 2
}

int_to_str = [
    'unknown',
    'saccade',
    'fixation'
]

class ClassError(Exception):
    pass

def convert_to_integers(stringclasses):
    for s in stringclasses:
        if s in str_to_int:
            yield str_to_int[s]
        else:
            raise ClassError('Invalid class string')

def convert_to_strings(intclasses):
    for i in intclasses:
        if i >= 0 and i < len(int_to_str):
            yield int_to_str[i]
        else:
            raise ClassError('Invalid class integer')
