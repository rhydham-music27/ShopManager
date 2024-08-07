from system.app import *
if __name__=="__main__":
    intializing()
    print(checkStock())
    calculatePendingAmount()
    # change the inside values from inventory/inventory.csv file to print receipt and add to database
    try:
        sellItem('luminousfan','rhydham','G3YRS')
        getTotalSales()
    except Exception:
        print('you have netered wrong value sir')

