"""
"""

string = 'Hello World'
number = 34564785
pi = 3.14

lst = [1, 7, 'test', True]


def func(arr):
    """
    Print some list
    :param arr: some list
    :return: None
    """
    for line in arr:
        print(line)


print('In module "mod1":', __name__)

if __name__ == '__main__':
    print(string)
    func(lst)
