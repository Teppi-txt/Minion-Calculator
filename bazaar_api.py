import json
import urllib.request as urllib

#API Setup
api_key = ("INSERT_API_KEY")
baz_api = "https://api.hypixel.net/skyblock/bazaar?key=" + api_key

#UrlLib Setup
baz_json = urllib.urlopen(baz_api)
data = json.load(baz_json)

#Diamond spreading calculation.
def diamond_spreading(item_count):
    #Gets data of diamond prices.
    diamond_qs = data['products']["ENCHANTED_DIAMOND"]['quick_status']
    e_diamond_conversion_rate = 1_600

    #Gets the sell price.
    sellPrice = diamond_qs['buyPrice']

    #Diamond earning is equal to every 10th minion action, then converted into enchanted diamonds. 
    #Diamond spreadings usually convert into enchanted diamonds.
    diamond_earning = sellPrice * (item_count[0]/e_diamond_conversion_rate)

    #Returns value to where the function was called.
    return diamond_earning

#Product calculation
def product_calculator(product_list):
    #Getting the product sell price with a dictionary containing sell price and amount.
    item_qs = data['products'][product_list[0]]['quick_status']

    #Instantiating those values.
    #productIp = item_qs['productId']
    sellPrice = item_qs['buyPrice']
    #buyPrice = item_qs['buyPrice']

    #Calculating the amount of profit from the variables.
    profit = sellPrice/product_list[2] * product_list[1]
    #Returning profit value.
    return profit