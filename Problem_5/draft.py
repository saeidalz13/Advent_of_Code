import pandas as pd

# ls = ['l','','m','g','sf','s','w3r','','']

# print(max([index for index, item in enumerate(ls) if item != '']))
# print(ls[6+1-3:6+1])
n = 2
base = ['4','25','et','y','thds']

# try:
#     last_valid_idx = max([index for index, item in enumerate(base) if item != ''])
# except Exception:
#     pass
# else:
#     print(last_valid_idx)
# idx = max([index for index, item in enumerate(base) if item != ''])
# print(base[:idx+1-n])
print(list(reversed(base)))