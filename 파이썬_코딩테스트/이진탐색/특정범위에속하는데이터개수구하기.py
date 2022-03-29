from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index-left_index


array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(array, 4, 4))
print(count_by_range(array, -1, 3))
