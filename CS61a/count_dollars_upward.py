def next_largest_dollar(bill):
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100
    else:
        return None


def count_dollars_upward(total):
    def count_partitions(remaining, minimum):
        """
        以最小值minimum分割remaining
        :param remaining:
        :param maximum:
        :return:
        """
        if minimum == None:
            return 0
        if minimum > remaining:
            return 0
        elif minimum == remaining:
            return 1

        return count_partitions(remaining - minimum, minimum) +\
            count_partitions(remaining, next_largest_dollar(minimum))
    return count_partitions(total, 1)