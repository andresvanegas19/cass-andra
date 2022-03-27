# Data processing

all the data processing and make one data

## Source of data
For data collection it is necessary to first form a robust database with hourly interval data for 6 years, an average of 52560 data to 3155760 data.

For this data it is necessary to obtain these 3 platforms.

 - Yahoo
 - Blockchain (API)
 - Coin market cap (API)

# Data format
It is necessary to train the model that the data has the format of MONTH/DAY/YEAR HOUR:MINUTES:SECONDS and for the cryptocurrency prices in dollars it is rounded and for the cryptocurrency value it is in decimals.



## Features in the data
The most important and basic feature that we can extract is the date that is in months and hours, and another data that we will take into account is the volume of purchase.

## Hypothesis
Drastic changes that would be outliers should be taken into account first. In the exploratory analysis of the data set, the study variable will be the price and two categorical independent variables will be selected as possible factors influencing the price. To test this hypothesis, we expect to calculate the volume of purchases and movements compared to the value at that time.

## Splitting data
Sparse data, as there may be gaps of some dates that were not recorded and that made the data missing. For outliers, wavelet transforms could be implemented for the missing data. This would leave 80% for model training, and 10% and 10% for validation and testing.

## Model training
For the training we first validate the hypothesis, and place it as features date, price, volume of purchase. It is expected to make 5 models testing the different features and the impact that each one has on the prediction decision.

---
## Storing data
For the storage of the data we will use a postgres database with the timescaledb plugin since this will facilitate the indexing of dates which is the most important thing in this. Similarly, after the model already deployed is expected to see that it gives better performance if implemented with mongoDb.
