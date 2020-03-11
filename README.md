# NIDS1920-WH-data
NIDS full data science example repo for both World Happiness raw data and prediction submission

The two main files are:
* `WH_data_train.csv` to train a model to predict happiness (i.e. "Life Ladder", cf below) from other metrics.
* `WH_data_test.csv` to test the model. This file does not contain the happiness metric.

Each group should:
* copy the files to their analysis repo to create their model
* fork this repo and clone it, so that to submit a pull-request which adds their "Life Ladder" predictions to the `WH_data_test.csv` file

The columns of interest are: 
1. **Life Ladder**: the life evaluation used (to measure happiness) is the Cantril Ladder, which asks survey respondents to place the status of their lives on a “ladder” scale ranging from 0 to 10, where 0 means the worst possible life and 10 the best possible life
2. **GDP per capita** is in terms of Purchasing Power Parity (PPP) adjusted to constant 2011 international dollars, taken from the World Development Indicators (WDI) released by the World Bank on November 14, 2018. See Statistical Appendix 1 for more details. GDP data for 2018 are not yet available, so we extend the GDP time series from 2017 to 2018 using countryspecific forecasts of real GDP growth from the OECD Economic Outlook No. 104 (Edition November 2018) and the World Bank’s Global Economic Prospects (Last Updated: 06/07/2018), after adjustment for population growth. The equation uses the natural log of GDP per capita, as this form fits the data significantly better than GDP per capita.
3. The time series of **healthy life expectancy at birth** are constructed based on data from the World Health Organization (WHO) Global Health Observatory data repository, with data available for 2005, 2010, 2015, and 2016. 
4. **Social support** is the national average of the binary responses (either 0 or 1) to the Gallup World Poll (GWP) question “If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?” 
5. **Freedom to make life choices** is the national average of binary responses to the GWP question “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?” 
6. **Generosity** is the residual of regressing the national average of GWP responses to the question “Have you donated money to a charity in the past month?” on GDP per capita. 
7. **Perceptions of corruption** are the average of binary answers to two GWP questions: “Is corruption widespread throughout the government or not?” and “Is corruption widespread within businesses or not?” Where data for government corruption are missing, the perception of business corruption is used as the overall corruption-perception measure. 
