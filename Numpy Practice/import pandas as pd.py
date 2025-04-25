import pandas as pd
import numpy as np
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr)

df = pd.DataFrame(arr)
print(df)

df.to_csv(r"C:\Users\bharg\Desktop\Numpy Practice.csv", index=False)
random_array = np.random.randint(0,100,size=(4,7))
print(random_array)
dff = pd.DataFrame(random_array)
print(dff)

##dff.to_csv(r"C:\Users\bharg\Desktop\Numpy_Practice.csv", index=False)
dff.columns= ["Column_1", "Column_2","Column_3", "Column_4", "Column_5", "Column_6","Column_7"]
print(dff)
dff.to_csv(r"C:\Users\bharg\Desktop\Numpy_Practice.csv", index=False)
total = dff.sum().sum()
print(total)


