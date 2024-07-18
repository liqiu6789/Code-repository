import timeit

# 创建一个包含一百万个元素的列表和集合
num_elements = 1000000
elements = list(range(num_elements))
element_set = set(elements)

# 要查找的元素
search_element = num_elements - 1

# 测量列表查询的时间
list_time = timeit.timeit(stmt=f'{search_element} in elements', globals=globals(), number=1000)

# 测量集合查询的时间
set_time = timeit.timeit(stmt=f'{search_element} in element_set', globals=globals(), number=1000)

print(f'List lookup time: {list_time} seconds')
print(f'Set lookup time: {set_time} seconds')
print(f'Set lookup is {list_time / set_time:.2f} times faster than list lookup')
