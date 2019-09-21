

import dataret as dr
import matplotlib.pyplot as plt

frame = dr.get_data('result.xlsx')

def getsalessum(shop_id):

    return sum(list(frame[frame['Outlet_Id'] == shop_id]['Item_Outlet_Sales']))



#-----------------------------------------------------------------------------------------------------------------------------

def getsalesonitems(shops, item):
    sales = []
    for itr in shops:
        sales.append(sum(list(frame[(frame['Outlet_Id'] == itr) & (frame['Item_Type'] == item)]['Item_Outlet_Sales'])))
    return sales


if __name__ == '__main__' :
    shops = dr.get_unqiue_list(list(frame['Outlet_Id']))
    items = dr.get_unqiue_list(list(frame['Item_Type']))
    for itr in items:
        sales = getsalesonitems(shops,itr)
        plt.bar(shops, sales)
        plt.title(itr)
        plt.show()
    #sales = list(map(getsalessum, shops))


#-------------------------------------------------------------------------------------------------------------------------------

'''
if __name__ == '__main__' :
    pass
    #sales = list(map(getsalessum, shops))
'''
