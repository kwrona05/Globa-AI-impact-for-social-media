import pandas as pd
import numpy as np
from matplotlib import pyplot
import seaborn as sns

df = pd.read_csv('./Global_AI_Content_Impact_Dataset.csv')

#Number of countries from which data was collected
countries_number = df['Country'].count()
print(f'Number of countries: {countries_number}')

#Posegregować na lata i wyciągnąć dane:
#Industries which used AI
# AVG global AI adoption rate in each industry in each year




