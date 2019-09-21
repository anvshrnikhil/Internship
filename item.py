#slow speed

import dretrive as dr

import numpy as np

df = dr.get_data('train.xls')

df = dr.get_req_att(df, 'Item_Id')

arr = list(set(df))

print(len(arr))

count = np.zeros(len(arr))

for itr in range(len(arr)):
	print(itr)
	for inner_itr in range(len(df)):

		if arr[itr] == df.loc[inner_itr]:

			#print(arr[itr])

			count[itr] += 1


for itr in range(len(arr)):

	print(arr[itr], ' ', count[itr])
			
			
