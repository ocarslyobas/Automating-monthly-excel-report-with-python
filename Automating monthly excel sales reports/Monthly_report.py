import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datatime
import calender

#gathering the data
monthly_data = [01_january.xlsl,02_february.xlsl,03_march.xlsl]
combined_data = pd.DataFrame()
for file in monthly_data:
    df = pd.read_excel(file)
    df['Date'] = df['Date'].dt.date
    df['Day'] = pd.datetimeIndex(df['Date']).day
    df['Month'] = pd.datetimeIndex(df['Date']).month
    df['Year'] = pd.datetimeIndex(df['Year']).Year
    df['Month_Name'] = df['Month'].apply(lambda x: calender.month_abbr[int(x)])
    df.dropna(inplace = True)
    combined_data = pd.concat([combined_data, df], ignore_index = True)






