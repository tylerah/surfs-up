# Analysis of Hawaii Weather Patterns Using SQLite Queries
Click here to view the jupyter notebook containing the SQLite queries: https://github.com/tylerah/surfs-up/blob/main/SurfsUp_Challenge.ipynb

## Overview of the Statistical Analysis
The purpose of this project was to retrieve the weather data in Hawaii during the months of June and December. This data would then be used to evaluate whether opening a hybrid surf/icecream shop is a viable business endeavor year round on teh island of Oahu. A jupyter notebook was used to create a query that could filter out the weather for the months in question. After performing a successful query, this data was placed into a pandas DataFrame in order to complete the analysis. Such analysis included the average temperature during each month, the standard deviation for that temperature, as well as the minimum and maximum temperatures. 


## Results
The following image displays the results of the analysis. 

![Screen Shot 2022-07-11 at 10 42 23 PM](https://user-images.githubusercontent.com/104606662/178410166-5e74fd11-56bb-4cd6-bdc7-c538582d724b.png)

Notable observations from the analysis include:
  1. The sample size for both June and December is sufficiently large
  2. The average temperature for both June and December is comparable
  3. The minimum temperature in December is almost degrees less than the minimum temperature in June
  
One of the largest concerns from the client was whether or not the the sample size was large enough to be sufficiently representative of the true weather patterns. The count of observations for June was 1700 and the count for December was 1517. Both sample sizes are large enough that the data can be assumed to be representative enough to evaluate the weather patterns as a whole. 

A potentially surprising observation is that the average temperature for both the months is relatively similar. The average in June is 75 degrees while the average in December is 71 degrees. This suggests that the weather in Hawaii does not flucuate too wildly throughout the year. Additionally, the average does not appear to drop below 70 degrees throughout the year which is promising in terms of the sustainability for an icecream shop. However, while the average temperatures are very comparable, it is important to note that the minimum temperature in December has dropped as low as 56 degrees (which is 8 degrees lower than the minimum observed in June). This finding should motivate the business owners to gather some additional industry data regarding what temperature the average person considers too cold to eat icecream. 

## Summary
### Conclusion
Based on the results, it is evident that the temperature patterns are mostly consistent throughout the entire year. This bodes well for the year-round sustainability of the surf & icecream shop as the average temperature does not drop below 70 degrees at any point during the year. 70 degrees is sufficiently warm enough weather to expect a steady flow of customers. 

### Additional Queries
While the temperature data is promising, there are a few additional queries that can provide further insight. The sqlite file contains information regarding temperature as well as precipitation. A query regarding average precipitation that takes place during each month would provide useful information in evaluating the year-round sustainability of an icecream shop. It is a safe assumption that while the temperature may be warm enough, not many individuals will visit the beach or a surf / icecream shop if there is significant rain. As such, this information should also be considered in order to better determine the sustainability of such a shop. 

Another worthwhile query would be to filter the data for both temperature and precipitation by year. The original query provided an average for the month of June across several years. However, it is possible that some years have been warmer or cooler overall. It is also possible that some years experienced more precipitation than others. In order to better determine the potential longevity of the shop, it would be useful to know what the weather is like on the coolest years vs the warmest years. It is possible that one of the years dipped significantly in temperature. Knowing the average temperatures and precipitation levels for the coolest year / wettest year would help the business owners understand what a "worst case" scenario would look like. Knowing this information would be helpful in order to tailor the business strategy for such years. 
