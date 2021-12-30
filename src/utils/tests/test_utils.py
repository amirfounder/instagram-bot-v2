from src.utils.utils import deep_copy_dictionary, deep_copy_list


class DummyTestClass:
    pass


def test_deep_copy_dictionary_no_ignore_values():
    original = {
        'dict': {
            'a': 'A',
            'b': 'B',
            'c': 'C'
        },
        'list': [1, 2, 3],
        'string': 'a',
        'int': 1
    }
    copy = deep_copy_dictionary(original)

    copy['dict']['a'] = 'C'
    copy['dict']['b'] = 'D'
    copy['list'][0] = 9
    copy['list'][1] = 8
    copy['list'][2] = 7
    copy['string'] = 'b'
    copy['int'] = 2

    assert original['dict']['a'] == 'A'
    assert original['dict']['b'] == 'B'
    assert original['list'][0] == 1
    assert original['list'][1] == 2
    assert original['list'][2] == 3
    assert original['string'] == 'a'
    assert original['int'] == 1
    
    assert original is not copy
    assert original['dict'] is not copy['dict']
    assert original['list'] is not copy['list']


def test_deep_copy_dictionary_ignore_class():
    original = {
        'copy': 'Copy this!',
        'dict': {
            'no_copy': DummyTestClass(),
            'copy': {
                'key': 'value'
            }
        }
    }

    copy = deep_copy_dictionary(original, [DummyTestClass])

    assert original['dict']['no_copy'] is copy['dict']['no_copy']
    assert original is not copy
    
