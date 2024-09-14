def find_zero_sum_subarrays(arr):
    sum_map = {}

    result = []
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == 0:
            result.append((0, i))

        if curr_sum in sum_map:
            for start_index in sum_map[curr_sum]:
                result.append((start_index + 1, i))

        if curr_sum in sum_map:
            sum_map[curr_sum].append(i)
        else:
            sum_map[curr_sum] = [i]

    return result


arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
print(find_zero_sum_subarrays(arr))
