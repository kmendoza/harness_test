


def foo():
    print('Entry point function foo')


class bar:
    def __call__(self,**kwargs):
        print('Entry point class bar')


if __name__ == '__main__':
    print('Entry point __main__')