input = list("1113222113")

def split_numbers(numbers: str) -> list:
  full_arr = []
  curr_arr = [numbers[0]]
  b = False
  for num,i in enumerate(numbers):
    if num == 0:
      continue
    else:
      if i == curr_arr[-1]:
        b = False
        curr_arr.append(i)
      else:
        full_arr.append(curr_arr)
        curr_arr = [i]
        b = True
  if not b or len(curr_arr) == 1:
    full_arr.append(curr_arr)
  return full_arr

def join_numbers(numbers_list: list) -> str:
  full_str = ""
  for arr in numbers_list:
    full_str += "".join(map(lambda x: str(x), arr))
  return full_str

def play_game(numbers_list):
  result = []
  for arr in numbers_list:
    # print(arr[0])
    result.append([len(arr)])
    result.append(arr[0])
    # print(arr)
  return result

for i in range(50):
  n_input = join_numbers(play_game(split_numbers(input)))
  input = n_input
  # print(n_input)
  print(len(n_input))