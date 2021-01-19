from problem_solving import _20210118_med_dp__coin_change_03 as f

timeout_01_arr = [1, 2, 5, 7, 8, 10, 11, 12, 13, 17, 19, 22, 28, 32, 33, 35, 37, 39, 40, 41, 43, 46, 49]
timeout_01_amt = 166

# result = f.getWaysInteral(10, [2,3,5,6])
result = f.getWays(timeout_01_amt, timeout_01_arr)
print(f"num ways: {result}")