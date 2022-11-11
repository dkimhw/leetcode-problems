import math

def possible_2n_vals(n):
  num_of_digits = len(list(str(n)))
  curr_cnt = 0
  curr_2n_num = 1
  curr_n = 0
  possible_2n_nums_to_check = []


  while curr_cnt <= num_of_digits:
    curr_2n_num = 2 ** curr_n
    curr_cnt = len(list(str(curr_2n_num)))
    # print(curr_2n_num)
    # print(num_of_digits)
    # print(curr_cnt)
    curr_n += 1
    if (curr_cnt == num_of_digits):
      possible_2n_nums_to_check.append(curr_2n_num)

  return possible_2n_nums_to_check


print(possible_2n_vals(1))
