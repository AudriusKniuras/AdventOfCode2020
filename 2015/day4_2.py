from hashlib import md5
from timeit import default_timer as timer

start = timer()

num = 0
while True:
  i = 'ckczppom' + str(num)
  if md5(i.encode()).hexdigest()[0:6] == '000000':
    print(num)
    break
  num += 1

stop = timer()
print('Time: ', stop-start)

