import bazaar_api
import minion_info

def product_reciever(product_list, fuel_percentage):
    profit = 0; secs_in_day = 86400
    for n in range(len(product_list) - 1):
        action_time = product_list[-1]; product_name = product_list[n][0]
        product_mult = product_list[n][1]; product_compact = product_list[n][2]
        item_count = (secs_in_day/action_time) * product_mult
        profit += bazaar_api.product_calculator([product_name, item_count, product_compact])
        profit += bazaar_api.diamond_spreading([item_count])
    one_percent_profit = profit/100
    return profit + one_percent_profit * fuel_percentage

for i in minion_info.minion_data:
    if product_reciever(minion_info.minion_data[i], 0) > 46_000:
        print(str(i) + " : " + str(int(product_reciever(minion_info.minion_data[i], 0))))
