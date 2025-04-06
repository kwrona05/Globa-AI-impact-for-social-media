import pandas as pd
import numpy as np
from matplotlib import pyplot
import seaborn as sns

df = pd.read_csv('./Global_AI_Content_Impact_Dataset.csv')
columns = df.columns.values
print(columns)

grouped_countries = df.groupby('Country')
#Market share of AI in companies
ai_in_companies = df['Market Share of AI Companies (%)']
avg_market_share = np.average(ai_in_companies)
print(avg_market_share)

market_share_by_countries = df.groupby('Country')['Market Share of AI Companies (%)'].mean()
for country, avg in market_share_by_countries.items():
    print(f'{country}: {avg}')
#Consumer trust to AI
avg_consumer_trust_to_ai = np.average(df['Consumer Trust in AI (%)'])
print(f'Global Consumer Trust: {avg_consumer_trust_to_ai}')

consumer_trust_to_ai_by_countries = df.groupby('Country')['Consumer Trust in AI (%)'].mean()
for country, avg in consumer_trust_to_ai_by_countries.items():
    print(f'{country}: {avg}')
#AI generated content
avg_ai_generated_content = np.average(df['AI-Generated Content Volume (TBs per year)'])
print(f'Global avg AI generated content: {avg_ai_generated_content}')

generated_content_by_countries = df.groupby('Country')['AI-Generated Content Volume (TBs per year)'].mean()
for country, avg in generated_content_by_countries.items():
    print(f'{country}: {avg}')
#Top AI tools
most_popular_ai_tools = df['Top AI Tools Used'].value_counts()
print(most_popular_ai_tools)

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


