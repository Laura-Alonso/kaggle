import pandas as pd   # v - 23.3.1
from tabulate import tabulate
from pandas.api.types import CategoricalDtype # Order cat var


# Packages Time Series
import numpy as np # linear algebraç
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # Plot for ANOVA, statistical data visualization


# Data
data = pd.read_csv("./DB/20231108_rawData_salaries.csv")

# Recode Countries
map_country_name = {
    'AD':'Andorra', 'AR':'Argentina','AU':'Australia'
    ,'BR':'Brazil','CA':'Canada','CF':'Central African Republic'
    ,'CH':'Switzerland','CO':'Colombia','DE':'Germany'
    ,'EC':'Ecuador','EE':'Estonia','ES':'Spain'
    ,'FR':'France','GB':'United Kingdom','GR':'Greece'
    ,'HK':'Hong Kong','HR':'Croatia','IE':'Ireland'
    ,'IN':'India','IT':'Italy','LV':'Latvia'
    ,'MX':'Mexico','NL':'Netherlands','NO':'Norway'
    ,'PH':'Philippines','PL':'Poland','PT':'Portugal'
    ,'RO':'Romania','SE':'Sweden','SI':'Slovenia'
    ,'TH':'Thailand','US':'United States'

}

map_continent_name = {
    'AD':'Europe','AR':'South America','AU':'Asia-Pacific'
    ,'BR':'South America','CA':'North America','CF':'Central Africa'
    ,'CH':'Europe','CO':'South America','DE':'Europe'
    ,'EC':'South America','EE':'Europe','ES':'Europe'
    ,'FR':'Europe','GB':'Europe','GR':'Europe'
    ,'HK':'Shouteast Asia','HR':'Europe','IE':'Europe'
    ,'IN':'Asia-Pacific','IT':'Europe','LV':'Europe'
    ,'MX':'North America','NL':'Europe','NO':'Europe'
    ,'PH':'Asia-Pacific','PL':'Europe','PT':'Europe'
    ,'RO':'Europe','SE':'Europe','SI':'Europe'
    ,'TH':'Asia-Pacific','US':'North America'

}
data = data.assign(company_country_name = data.company_location.map(map_country_name))
data = data.assign(company_continent_name = data.company_location.map(map_continent_name))

# Only 2023
current_year = data['work_year'].max()
data_current = data[data['work_year'] == current_year]

### Remote work along the years
data_years_remote = data.loc[:,("work_year", "remote_ratio")]

# Recode names remote_ratio
data_years_remote["remote_ratio"] = data_years_remote.loc[:,("remote_ratio")].replace({
          0: "No remote work",
          50: "Partial remote work",
          100: "Fully remote work"
})

data_years_remote_count = data_years_remote.groupby(["work_year", "remote_ratio"]).size().reset_index(name='Count')

total_count = data_years_remote_count.groupby('work_year')['Count'].transform('sum')
data_years_remote_count['Percentage'] = (data_years_remote_count['Count'] / total_count) * 100

#Order
cat_type = CategoricalDtype(categories=["No remote work", "Partial remote work", "Fully remote work"], ordered=True)
data_years_remote_count['remote_ratio'] = data_years_remote_count['remote_ratio'].astype(cat_type)

# Data for the text
data_2020_text = data_years_remote_count[data_years_remote_count['work_year'] == 2020]
data_2023_text = data_years_remote_count[data_years_remote_count['work_year'] == 2023]

# Order for year
data_2020_sort_text = data_2020_text.sort_values(by = "Count", ascending=False)

data_2020_max_text = data_2020_sort_text.values[0,1]
data_2020_mid_text = data_2020_sort_text.values[1,1]
data_2020_min_text = data_2020_sort_text.values[2,1]

data_2023_sort_text = data_2023_text.sort_values(by = "Count", ascending=False)

data_2023_max_text = data_2023_sort_text.values[0,1]
data_2023_mid_text = data_2023_sort_text.values[1,1]
data_2023_min_text = data_2023_sort_text.values[2,1]

###########################################################################
# Data for each category with year and count
data_years_remote_count['work_year'] = pd.to_datetime(data_years_remote_count['work_year'], format='%Y') # Make year as dateTime

data_noremote = data_years_remote_count[data_years_remote_count['remote_ratio'] == "No remote work"][["work_year", "Count"]]
data_partial = data_years_remote_count[data_years_remote_count['remote_ratio'] == "Partial remote work"][["work_year", "Count"]]
data_fully = data_years_remote_count[data_years_remote_count['remote_ratio'] == "Fully remote work"][["work_year", "Count"]]

print(data_noremote)

# Visualize the data

def plot_data_remote(data, x, y, title="", xlabel='Date', ylabel='Number of users', dpi=100):
    plt.figure(figsize=(15,4), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

plot_data_noremote = plot_data_remote(data_noremote, 
                   x=data_noremote['work_year'], 
                   y=data_noremote['Count'],
                   title='Number of workers doing no remote work from 2020 to 2023')   



plot_data_partial_remote = plot_data_remote(data_partial, 
                   x=data_partial['work_year'], 
                   y=data_partial['Count'], 
                   title='Number of workers doing no remote work from 2020 to 2023')                      

plot_data_fully_remote = plot_data_remote(data_fully, 
                   x=data_fully['work_year'], 
                   y=data_fully['Count'], 
                   title='Number of workers doing no remote work from 2020 to 2023')  