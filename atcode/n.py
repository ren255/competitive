def solve():
    L, R, D, U = map(int, input().split())

    def count_even_abs_in_range(lo, hi):
        if lo > hi:
            return 0

        def count_even(a, b):
            if a > b:
                return 0
            return b // 2 - (a - 1) // 2

        return count_even(lo, hi)

    def count_black_in_row(x, D, U):
        abs_x = abs(x)
        count = 0
        if abs_x > 0:
            inner_lo = max(D, -(abs_x - 1))
            inner_hi = min(U, abs_x - 1)
            if inner_lo <= inner_hi and abs_x % 2 == 0:
                count += inner_hi - inner_lo + 1
        outer_left_hi = min(U, -abs_x)
        count += count_even_abs_in_range(D, outer_left_hi)
        outer_right_lo = max(D, abs_x)
        count += count_even_abs_in_range(outer_right_lo, U)
        return count

    total = 0
    for x in range(L, R + 1):
        total += count_black_in_row(x, D, U)

    print(total)


solve()
