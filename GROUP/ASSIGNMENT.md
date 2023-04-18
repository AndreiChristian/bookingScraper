### I- STEPS TO FOLLOW

- 1- Select a category of hotel and a city
- 2- Make a list of your competitors on booking.com for this city
- 3- Write a scraper using python able to collect your competitors’ room rates 2 to 10 times a day
  and save these information on a csv file.
- 4- Decide which time of the day is the most appropriate to collect your competitors’ rooms rates.
- 5- After a few days, you should have a dataset containing the room rates of your competitors at
  different points in time over the last few days.
- 6- Use linear regression to predict your competitors’ room rates for the next days and set your
  own room rates based on the average room rate of your competitors for the given days.

### II- WHAT SHOULD YOUR PYTHON SMART PRICING SOFTWARE BE ABLE TO DO?

Utimately, at the end of your project, your python script should be able to do following:

- 1- Load the dataset containing the historical room rates of your competitors as dataframe
- 2- Scrape the current room rates of your competitors on booking.com and append these rates to
  your dataframe
- 3- Using this dataframe and linear regression, calculate the predicted room rates of your
  competitors for the next day
- 4- Output the predicted room rate of your hotel for the next day
