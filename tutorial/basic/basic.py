def num_t():
    x = 3
    print(x, type(x))
    print(x + 1)
    print(x - 1)
    print(x * 2)
    print(x ** 2)  # x^2
    x += 1
    print(x)
    x *= 2
    print(x)


def bool_t():
    t, f = True, False
    print(type(t))
    print(t and f)
    print(t or f)
    print(not t)
    print(t != f)


def string_t():
    hw = 'Hello' + ' ' + 'World'
    print(hw)
    s = 'hello'
    print(s.capitalize())
    print(s.upper())
    print(s.rjust(7))
    print(s.center(7))
    print(s.replace('l', '(ell)'))
    print('    world'.strip())


def list_t():
    xs = [3, 1, 2]
    print(xs, xs[2])
    print(xs[-1])
    xs[2] = 'foo'
    print(xs)
    xs.append('bar')
    print(xs)
    xs.pop()
    print(xs)

    nums = [0, 1, 2, 3, 4]
    squares = []
    for x in nums:
        squares.append(x ** 2)
    print(squares)

    squares_1 = [x ** 2 for x in nums]
    print(squares_1)

    squares_2 = [x ** 2 for x in nums if x % 2 == 0]
    print(squares_2)


def slicing_t():
    nums = list(range(5))
    print(nums)
    print(nums[2:4])  # [2,4)
    print(nums[2:])
    print(nums[:2])  # [0,2)
    print(nums[:])
    print(nums[:-1])
    nums[2:4] = [8, 9]
    print(nums)


def loop_t():
    animals = ['cat', 'dog', 'monkey']
    for animal in animals:
        print(animal)
    for idx, animal in enumerate(animals):
        print('#{}: {}'.format(idx + 1, animal))


def dictionary_t():
    d = {'cat': 'cute', 'dog': 'furry'}
    print(d['cat'])
    print('cat' in d)
    d['fish'] = 'wet'
    print(d['fish'])
    print(d.get('fish', 'N/A'))
    print(d.get('monkey', 'N/A'))

    d_1 = {'person': 2, 'cat': 4, 'spider': 8}
    for animal, legs in d_1.items():
        print('A {} has {} legs'.format(animal, legs))

    nums = [0, 1, 2, 3, 4]
    even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
    print(even_num_to_square)


def set_t():
    animals = {'cat', 'dog'}
    print('cat' in animals)
    print(('fish' in animals))
    animals.add('fish')
    print('fish' in animals)
    print(len(animals))
    animals.add('cat')
    print(len(animals))
    animals.remove('cat')
    print(len(animals))
    animals = {'cat', 'dog', 'fish'}

    for idx, animal in enumerate(animals):
        print('#{}: {}'.format(idx + 1, animal))

    from math import sqrt
    print({int(sqrt(x)) for x in range(30)})


def tuple_t():
    d = {(x, x + 1): x for x in range(10)}
    t = (5, 6)
    print(type(t))
    print(d[t])
    print(d[(1, 2)])


def sign_t(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


def hello_t(name, loud=False):
    if loud:
        print('HELLO, {}'.format(name.upper()))
    else:
        print('Hello, {}'.format(name))


def test_function_t():
    for x in [-1, 0, 1]:
        print(sign_t(x))

    hello_t('Bob')
    hello_t('Fred', True)

    g = Greeter('Fred')
    g.greet()
    g.greet(loud=True)


class Greeter:
    # Constructor
    def __init__(self, name):
        self.name = name  # create instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
            print('HELLO, {}'.format(self.name.upper()))
        else:
            print('Hello, {}'.format(self.name))


test_function_t()
