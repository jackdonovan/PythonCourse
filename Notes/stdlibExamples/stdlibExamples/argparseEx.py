import argparse

def main():
    print(args)
    print(args.foo)
    print(args.p)
    print(args.longName)
    print('n' in args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', help='This is a positional argument, it is required')
    parser.add_argument('bar', help='this is nother positional argument')
    parser.add_argument('-p', type=int, help='This is a flag that takes an int, it has no default so it will be none')
    parser.add_argument('--optionalFlag', type=float, default=4.6, help='This is an optional argument that takes a float.  It defaults to 4.6')
    parser.add_argument('-n', '--longName', type=complex, default=4.6j, help='This is an optional with a long and a short name for stuff.  It can only be referenced by the long name')

    parser.add_argument('-t', action='store_true', help='This causes the parser to store True in this, it defaults to False in this case')
    mxg = parser.add_mutually_exclusive_group()
    mxg.add_argument('--opt1', action='store_true')
    mxg.add_argument('--opt2', action='store_true')
    parser.add_argument('foobar', nargs='*', default='this is the default', help='This gathers up any positional arguments and puts them into a list, if nothing is presne tit uses the default.')
    args = parser.parse_args()
    
    main()