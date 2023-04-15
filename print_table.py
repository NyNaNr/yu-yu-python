table_date = [['apple', 'orange', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(table_date):
    col_widths = [0] * len(table_date)
    print(table_date[0])


print_table(table_date)
