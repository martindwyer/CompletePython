def add_all(*args):
    print(args)
    return sum(args)


print(add_all(1, 2, 3, 4))


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')


pretty_print(**{'username': 'jose123', 'access_level': 'admin'})
