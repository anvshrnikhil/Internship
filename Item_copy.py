#fast

import dretrive as dr

import numpy as np

df = dr.get_data('train.xls')

df = dr.get_req_att(df, 'Item_Id')

arr = list(set(df))

item = list(df)

count = np.zeros(len(arr), dtype = int)

for itr in range(len(arr)):

	for inner_itr in range(len(item)):

		if arr[itr] == item[inner_itr]:

			#print(arr[itr])

			count[itr] += 1


for itr in range(len(arr)):

	print(arr[itr], ' ', count[itr])
