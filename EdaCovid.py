import pandas as pd
import matplotlib.pyplot as plt

# Load the COVID-19 data into a pandas dataframe
covid_data = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv", parse_dates=['Date'])

# Filter the data for a specific country
country = 'India'
country_data = covid_data[covid_data['Country'] == country]

# Plot the daily confirmed cases
plt.plot(country_data['Date'], country_data['Confirmed'], label='Confirmed Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title(f'{country} COVID-19 Confirmed Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()

# Plot the daily recovered cases
plt.plot(country_data['Date'], country_data['Recovered'], label='Recovered Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title(f'{country} COVID-19 Recovered Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()

# Plot the daily deaths
plt.plot(
