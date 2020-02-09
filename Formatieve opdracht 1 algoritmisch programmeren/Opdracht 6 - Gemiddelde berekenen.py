def calc_average(lst):
    return sum(lst) / len(lst)


def calc_list_average(lst):
    number_sum = 0
    list_length = 0
    for i in lst:
        number_sum += sum(i)
        list_length += len(i)
    return number_sum / list_length
