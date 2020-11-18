"""

    *  *  *  *  *  *  *
    *  *  *  *  *  *  *
    *  *  *  *  *  *  *
    *  *  *  *  *  *  *
    *  *  *  *  *  *  *
    *  *  *  *  *  *  *
    *  *  *  *  *  *  *

"""

cols = 7
rows = 7
#
# for i in range(cols):
#     for j in range(rows):
#         print('*  ', end='')
#     print()

"""
        0               cols-1
      0 *  *  *  *  *  *  *
        *                 *
        *                 *
        *                 *
        *                 *
        *                 *
 rows-1 *  *  *  *  *  *  * 

"""

for i in range(cols):
    for j in range(rows):
        if (i == 0
                or i == cols - 1
                or j == 0
                or j == cols - 1
                or i == j):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
