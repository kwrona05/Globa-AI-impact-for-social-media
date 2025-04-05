import pandas as pd
import numpy as np
from matplotlib import pyplot
import seaborn as sns

df = pd.read_csv('./Global_AI_Content_Impact_Dataset.csv')
columns = df.columns.values
print(columns)

india_df = df[df['Country'] == 'India']
france_df = df[df['Country'] == 'France']
japan_df = df[df['Country'] == 'Japan']
china_df = df[df['Country'] == 'China']
usa_df = df[df['Country'] == 'USA']
skorea_df = df[df['Country'] == 'South Korea']
uk_df = df[df['Country'] == 'UK']
germany_df = df[df['Country'] == 'Germany']
canada_df = df[df['Country'] == 'Canada']
australia = df[df['Country'] == 'Australia']

#Market share of AI in companies
ai_in_companies = df['Market Share of AI Companies (%)']
avg_market_share = np.average(ai_in_companies)



#Consumer trust to AI

#AI generated content

#Top AI tools



#Number of countries from which data was collected
countries_number = df.value_counts('Country')
print(countries_number)

#Industries which used AI

#Revenue increase due to AI

#Human-AI colaboration rate

#Job loss due to AI in industries

#AVG global AI adoption rate in each industry in each year

#AI adoption rate in each industry and compare in each years


#Visualise data


#Predictive model


