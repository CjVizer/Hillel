string = 'Hello World'
number = 34564785
pi = 3.14

lst = [1, 'hi', 2.544, True]


def func(arr):
    """
    Print some list

    :param arr: some list
    :return: None
    """
    for i in arr:
        print(i)


print('In module "mod1":', __name__)

if __name__ == '__main__':
    print(string)
    func(lst)
