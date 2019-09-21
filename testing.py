import numpy as np
import dataret as dr
import pandas as pd
import matplotlib.pyplot as plt

'''
df = dr.get_data('clean_data.xls')
frame = dr.get_all_att(df, 'Item_Visibility', 0, excel=True, datatype="var")
print(frame)
'''

'''
frame = dr.get_data('temp.xls')
mrp = list(frame['Item_MRP'])
sales = list(frame['Item_Outlet_Sales'])
count = []
for itr in range(len(mrp)):
    count.append(sales[itr]/mrp[itr])

frame['count'] = count
dr.generate_excel(frame, 'temp.xls')
'''

'''
frame = dr.get_data('clean_data.xls')
print(frame.loc[0,'Item_Weight'])
print(frame.loc[1,'Item_Weight'])
print(frame.loc[2,'Item_Weight'])
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 2', datatype="var")
print(set(frame['Outlet_Type']))
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 1', datatype="var")
st1 = dr.get_all_att(frame, 'Outlet_Type', 'Supermarket Type1', datatype="var")
dr.generate_excel(st1, 'st1.xls')
gs = dr.get_all_att(frame, 'Outlet_Type', 'Grocery Store', datatype="var")
dr.generate_excel(gs, 'gs.xls')
'''

'''
frame = dr.get_data('st1.xls')
print(dr.get_unqiue_list(frame['Outlet_Id']))
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 3', datatype="var")
frame = dr.get_all_att(frame, 'Outlet_Type', 'Supermarket Type1', datatype="var")
#dr.generate_excel(frame, 'st2.xls')
print(dr.get_unqiue_list(frame['Outlet_Id']))
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 3', datatype="var")
frame = dr.get_all_att(frame, 'Outlet_Type', 'Supermarket Type2', datatype="var")
#dr.generate_excel(frame, 'st2.xls')
print(dr.get_unqiue_list(frame['Outlet_Id']))
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 3', datatype="var")
frame = dr.get_all_att(frame, 'Outlet_Type', 'Supermarket Type3', datatype="var")
#dr.generate_excel(frame, 'st2.xls')
print(dr.get_unqiue_list(frame['Outlet_Id']))
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 3', datatype="var")
frame = dr.get_all_att(frame, 'Outlet_Type', 'Grocery Store', datatype="var")
#dr.generate_excel(frame, 'st2.xls')
print(dr.get_unqiue_list(frame['Outlet_Id']))
'''

'''
frame = dr.get_data('clean_data.xls')
print(dr.get_unqiue_list(frame['Outlet_Id']))
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 2', datatype="var")
frame = dr.get_all_att(frame, 'Outlet_Type', 'Supermarket Type1', datatype="var")
#dr.generate_excel(frame, 'st2.xls')
print(dr.get_unqiue_list(frame['Outlet_Id']))
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, ['Outlet_Loc_Type', 'Outlet_Type', 'Outlet_Id'], ['Tier 1', 'Supermarket Type1', 'OUT049'])
dr.generate_excel(frame, 'result.xls')
'''
'''
frame = dr.get_data('temp.xls')
#frame = dr.get_all_att(frame, ['Item_Type', 'Item_Fat_Content'], ['Dairy', 'Low Fat'], excel=True)
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 1', datatype="var")
dr.generate_excel(frame, 'tier1.xls')
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 2', datatype="var")
dr.generate_excel(frame, 'tier2.xls')
frame = dr.get_all_att(frame, 'Outlet_Loc_Type', 'Tier 3', datatype="var")
dr.generate_excel(frame, 'tier3.xls')
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, ['Item_Type', 'Item_Fat_Content', 'Item_Id'], ['Dairy', 'Low Fat', 'FDA15'])
dr.generate_excel(frame, 'FDA15.xls')
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Item_Id', 'DRC01', datatype="var")
dr.generate_excel(frame, 'DRC01.xls')
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Item_Id', 'FDN15', datatype="var")
dr.generate_excel(frame, 'FDN15.xls')
'''

'''
frame = dr.get_data('clean_data.xls')
frame1 = dr.get_all_att(frame,['Outlet_Id','source'], ['OUT019','train'])
frame2 = dr.get_all_att(frame,['Outlet_Id','source'], ['OUT046','train'])
shape = frame1.shape
count = list(map(lambda x: frame1.loc[x,'Item_Outlet_Sales']/frame1.loc[x,'Item_MRP'], range(shape[0])))
frame1['Item_Count'] = count
#frame1.to_excel('gs.xlsx',index=False)


shape = frame2.shape
count = list(map(lambda x: frame2.loc[x,'Item_Outlet_Sales']/frame2.loc[x,'Item_MRP'], range(shape[0])))
frame2['Item_Count'] = count
#frame2.to_excel('out46.xlsx',index=False)


f1 = frame1[['Item_Id', 'Item_Count', 'Item_MRP', 'Item_Visibility']]
f2 = frame2[['Item_Id', 'Item_Count', 'Item_MRP', 'Item_Visibility']]
#print(f1)
result = f1.merge(f2,on='Item_Id',suffixes=('_Grocery', '_Super46'))
#print(result)
#result.to_excel('result.xlsx',index = False)
#print(result.max())
#print(len(result[result['Item_MRP_Grocery'] >= result['Item_MRP_Super46']]))

print(result[result['Item_Count_Grocery'] >= result['Item_Count_Super46']])
#visual
x_axis =[x for x in range(len(result['Item_Id']))]
plt.plot(x_axis, result['Item_Count_Grocery'])
plt.plot(x_axis, result['Item_Count_Super46'])
plt.show()
'''

'''
frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Item_Id', 'FDU32', datatype="var")
frame.to_excel('FDU32.xlsx', index=False)
'''

frame = dr.get_data('clean_data.xls')
frame = dr.get_all_att(frame, 'Item_Id', 'NCY18', datatype="var")
dr.generate_excel(frame, 'NCY18.xlsx')
