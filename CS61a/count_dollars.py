def next_smallest_dollar(bill):
    if bill == 100:
        return 50
    elif bill == 50:
        return 20
    elif bill == 20:
        return 10
    elif bill == 10:
        return 5
    elif bill == 5:
        return 1
    else:
        return 0


def in_denominations(bill):
    denominations = [1, 5, 10, 20, 50, 100]
    return bill in denominations


def count_dollars(total):
    def find_next_deno(bills):
        assert bills > 0, '付款必须大于零'
        denos = [1, 5, 10, 20, 50, 100]
        while True:
            if bills in denos:
                return bills
            else:
                bills -= 1

    def count_partitions(bills, maximum):
        if bills == 1:
            return 1
        elif bills <= 0:
            return 0
        elif maximum == 0:
            return 0

        if bills == maximum:
            return 1 + count_partitions(bills, next_smallest_dollar(maximum))
        else:
            return count_partitions(bills - maximum, maximum) \
                + count_partitions(bills, next_smallest_dollar(maximum))

    maximum = find_next_deno(total)
    return count_partitions(total, maximum)