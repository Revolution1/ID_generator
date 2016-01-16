def is_tl(data):
    return isinstance(data, tuple) or isinstance(data, list)


def get_depth(data):
    '''
    :type data: list or tuple
    get the depth of nested list
    'x'              is 0
    ['x', 'y']       is 1
    ['x', ['y', 'z'] is 2
    '''
    if is_tl(data):
        depths = []
        for i in data:
            depths.append(1+get_depth(i))
        return max(depths)
    else:
        return 0


def reduce_d2(a, b):
    '''
    generate all combination from a, b
    '''
    if not is_tl(a):
        a = [a]
    if not is_tl(b):
        b = [b]
    result = []
    for i in a:
        for j in b:
            result.append('%s%s' % (i, j))
    return result


def _generate_d2(data):
    return reduce(reduce_d2, data)


def _generate(data):
    '''
    recursively generate the list
    '''
    depth = get_depth(data)
    if depth > 2:
        temp = []
        for i in data:
            temp.append(_generate(i))
        return _generate(temp)
    elif depth == 2:
        return _generate_d2(data)
    elif depth == 1:
        return data
    else:
        return [str(data)]


def generate(data):
    '''
    :rtype: list of str
    :type data: list or tuple
    generate the final result
    '''
    result = _generate(data)
    # fix if initial data's depth == 1
    if result == data:
        result = _generate_d2(data)
    return result


if __name__ == '__main__':
    nested = [range(2), [range(3), range(4)]]
    print(generate(nested))
    print(generate([1, [2, 3]]))
    print(generate([1, 2]))
    print(generate(1))
