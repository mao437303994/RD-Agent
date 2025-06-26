# How to read files.
For example, if you want to read `filename.h5`
```Python
import pandas as pd
df = pd.read_hdf("filename.h5", key="data")
```
NOTE: **key is always "data" for all hdf5 files **.

# Here is a short description about the data

| Filename       | Description                                                      |
| -------------- | -----------------------------------------------------------------|
| "daily_pv.h5"  | Adjusted daily price and volume data.                            |


# For different data, We have some basic knowledge for them

## Daily price and volume data
$open: Open price of the stock on that day.
$close: Close price of the stock on that day.
$high: High price of the stock on that day.
$low: Low price of the stock on that day.
$volume: Trading volume of the stock on that day.
$oi: Open interest of the stock or contract on that day (mainly used for futures, represents the number of outstanding contracts).
$month: The month corresponding to the trading date (e.g., 1 for January, 12 for December).
$week: The week number of the year corresponding to the trading date.
$quarter: The quarter of the year corresponding to the trading date (e.g., 1 for Q1, 4 for Q4).