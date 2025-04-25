import numpy as np
import pandas as pd
np.random.seed(0)
sales_amounts = np.random.randint(20, size=(5,3))
#print(sales_amounts)

weekly_sales = pd.DataFrame(sales_amounts,
                            index=["Mon", "Tue", "Wed","Thurs", "Fri"],
                            columns=["Almond Butter", "Peanute Butter", "Cashew Butter"])    
#print(weekly_sales) 
prices = np.array([10,8,12])
#print(prices.shape)
butter_prices = pd.DataFrame(prices.reshape(1,3),
                             index=["Price"],
                             columns=["Almond Butter", "Peanute Butter", "Cashew Butter"])
#print(butter_prices)
sales_trans = sales_amounts.T
total_sales =prices.dot(sales_trans)
#print(total_sales)
daily_sales = butter_prices.dot(weekly_sales.T)
#print(daily_sales.reshape(5,3))
print(weekly_sales.shape)
weekly_sales["Total ($)"] = daily_sales.T
print(weekly_sales)

