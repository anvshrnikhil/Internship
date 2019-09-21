
import dretrive as dr
import pandas as pd

def generate_excel(df):
    writer = pd.ExcelWriter('text.xls')
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()

if __name__ == '__main__' :

    df = dr.get_data('ctrain.xls')
    std_shop_list = dr.get_unqiue_list(list(df['Outlet_Id']))
    shop_list = list(df['Outlet_Id'])
    item_visible = list(df['Item_Visibility'])
    outlet_size = list(df['Outlet_Size'])
    item_weight = list(df['Item_Weight'])
    loc_type = list(df['Outlet_Loc_Type'])
    outing = list(df['Outlet_Type'])
    tot_visi_list = []
    type_list = []
    count_list = []
    weight_list = []
    final_list = []
    loc_list = []
    out_type = []
    for itr in std_shop_list:
        tot = 0
        count = 0
        weight = 0
        final = 0
        out = outing[0]
        for inner_itr in range(len(shop_list)):
            if itr == shop_list[inner_itr]:
                tot += item_visible[inner_itr]
                type_ =  outlet_size[inner_itr]
                if(pd.isna(item_weight[inner_itr]) == False):
                    weight += item_weight[inner_itr]
                    #final +=  item_weight[inner_itr] * item_visible[inner_itr]
                count += 1
                loc = loc_type[inner_itr]
                out = outing[inner_itr]
        tot_visi_list.append(tot)
        type_list.append(type_)
        count_list.append(count)
        weight_list.append(weight)
        #final_list.append(final)
        loc_list.append(loc)
        out_type.append(out)

    frame = pd.DataFrame(columns=["shop_id","item_weight","size","item_count","visible"])
    frame['shop_id'] = std_shop_list
    frame['item_weight'] = weight_list
    frame['size'] = type_list
    frame['item_count'] = count_list
    frame['visible'] = tot_visi_list
    frame['Loc'] = loc_list
    #frame['final'] = weight_list * tot_visi_list

    for itr in range(len(std_shop_list)):
        tot = weight_list[itr] * tot_visi_list[itr]
        final_list.append(tot)

    frame['final'] = final_list
    frame['Outlet_size'] = out_type
    print(frame)

    print()
    print("final = item_weight * visible")

    #generate_excel(frame)
