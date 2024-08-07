from random import randint
import pandas as pd
import os
from pyzbar.pyzbar import decode
from PIL import Image 
def scanBarCode(name_of_bar_code):
    pass
import barcode
from barcode.writer import ImageWriter
currentPath = os.getcwd()
inventoryData = pd.read_csv(f'{currentPath}/inventory/inventory.csv')
supplyData = pd.read_csv(os.path.join(currentPath,'supplier/pending.csv'))
salesData = pd.read_csv(os.path.join(currentPath,'sales/sales.csv'))

# bar code tools 

class BarCodeTools:
    def createBar(name,data,path = currentPath):
        barcode_type = 'code128'
        code = barcode.get_barcode_class(barcode_type)
        barcode_data = data
        barcode_instance = code(barcode_data, writer=ImageWriter())
        barcode_instance.save(f'{path}/barcode/{name}')
        print('saved')
   
    def readingBar(name,path=currentPath):
        for item in decode(Image.open(f'{path}/barcode/{name}.png')):
            return item.data.decode('utf-8')
        
# intializing the system 
def intializing():
    for i in range(0,len(inventoryData['barnumber'])):
        BarCodeTools.createBar(inventoryData['name'][i],str(inventoryData['barnumber'][i]))

# tracking the stocks 
class StockManager:
    def reduceStock(name):
        for index in range(0,len(inventoryData['name'])):
            if inventoryData['name'][index]==name :
                itemIndex = index 
                break
        inventoryData.loc[itemIndex,'available'] = inventoryData['available'][itemIndex] -1
        inventoryData.to_csv(f"{currentPath}/inventory/inventory.csv",index=False)

    def AddToStock(name,number):
        for index in range(0,len(inventoryData['name'])):
            if inventoryData['name'][index] == name:
                itemIndex = index
                break
        inventoryData.loc[itemIndex,'available'] = inventoryData['available'][itemIndex]+int(number)
        inventoryData.to_csv(f"{currentPath}/inventory/inventory.csv",index=False)
# checking if we are not low on stocks 
def checkStock():
    for item in inventoryData['available']:
        try:
            if int(item)<5:
                print("stocks are less")
                return False
            else:
                return True
        except Exception as e:
            print("some empty values are neglected")

# calculating the amount we have to pay to supplier 
def calculatePendingAmount():
    try:
        for index in range(0,len(inventoryData['name'])):
            supplyData.loc[index,'name'] = inventoryData['name'][index]
            supplyData.loc[index,'supplier'] = inventoryData['supply_manager'][index]
            supplyData.loc[index,'amount'] = int(inventoryData['available'][index])*int(inventoryData['price'][index])
            supplyData.to_csv(os.path.join(currentPath,'supplier/pending.csv'),index=False)
        return True
    except Exception as e:
        return False
# if we want to get the real price 
def getPrice(name):
    for i in range(0,len(inventoryData['name'])):
        if inventoryData['name'][i] == name :
            return inventoryData['price'][i]
        else:
            return None
# creating some discounts 
def discount(item):
    for index in range(0,len(inventoryData['name'])):
        if inventoryData['name'][index]==item:
            randomDiscount = float(randint(0,10)/100)
            newPrice = inventoryData['price'][index]-float(inventoryData['price'][index]*randomDiscount)
            return float(f'{newPrice}')
# having a transaction 

from datetime import datetime
def sellItem(name,customer_name,GW):
    StockManager.reduceStock(name)
    initialLength = len(salesData['item'])
    price = getPrice(name)
    for index in range(0,len(inventoryData['name'])):
        if inventoryData['name'][index]==name:
            salesData.loc[initialLength,'s_no'] = initialLength+1
            salesData.loc[initialLength,'item'] = name 
            salesData.loc[initialLength,'sold_at'] = price
            salesData.loc[initialLength,'sold_to'] = customer_name
            salesData.loc[initialLength,'sold_on'] = datetime.now().date()
            salesData.loc[initialLength,'guarranty/warranty'] = GW
            break
    salesData.to_csv(os.path.join(currentPath,'sales/sales.csv'),index=False)
    receipt(name)

def receipt(item):
    for index in range(0,len(salesData['item'])):
        if salesData['item'][index]==item:
            recieptItem = salesData['item'][index]
            price_on_reciept = salesData['sold_at'][index]
            customer_name = salesData['sold_to'][index]
            gw = salesData['guarranty/warranty'][index]
            sold_on = salesData['sold_on'][index]
    print(f'''      SHOP NAME   ''')
    print('''*'''*27)
    print(f'item\t: {recieptItem}')
    print(f'price\t: {price_on_reciept}')
    print(f'customer: {customer_name}')
    print(f'guarrantee/warranty:{gw}')
    print('''*'''*27)
    print(f"{sold_on}\tsignature")

# getting total sales of day 
def getTotalSales():
    total = 0 
    for item in salesData['sold_at']:
        total+=float(item) 
    print(f"your total sale at {datetime.now().date()} is {total}")

# running the main app 

      
