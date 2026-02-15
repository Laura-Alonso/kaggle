#! C:\Users\laura.alonso\Desktop\job-salaries-main\job-salaries-main\venv\Scripts\python.exe

import pandas as pd   # v - 23.3.1
from tabulate import tabulate
from IPython.display import Markdown, display, HTML
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns

# Packages Statistics
from statsmodels.graphics.factorplots import interaction_plot
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

### Functions created. Eta and omega where created for ALEKS MASHANSKI  for Two ways ANOVA because Stats model 
# doesnt have it. https://www.kaggle.com/code/alexmaszanski/two-way-anova-with-python#kln-55
def eta_squared(aov):
    aov['eta_sq'] = 'NaN'
    aov['eta_sq'] = aov[:-1]['sum_sq']/sum(aov['sum_sq'])
    return aov
def omega_squared(aov):
    mse = aov['sum_sq'][-1]/aov['df'][-1]
    aov['omega_sq'] = 'NaN'
    aov['omega_sq'] = (aov[:-1]['sum_sq']-(aov[:-1]['df']*mse))/(sum(aov['sum_sq'])+mse)
    return aov


# Import data
data = pd.read_csv("../../2_DB/20231108_rawData_salaries.csv")

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

current_year = data['work_year'].max()
data_current = data[data['work_year'] == current_year]

job_count = data_current['job_title'].value_counts().head(10).reset_index()

job_count.set_index("job_title", inplace=True)
job_count.index.name = None
job_count.columns.name = None

first_job = job_count.index[0]
second_job = job_count.index[1]
third_job = job_count.index[2]

data_top = data_current[(data_current["job_title"] == first_job) | (data_current["job_title"] == second_job) | (data_current["job_title"] == third_job)]
# 

#

# Prepare data
data_salary_job_continents = data_top.loc[(data_top['company_continent_name']== 'Europe') | (data_top['company_continent_name']== 'North America')]
data_salary_job_continents_mean = data_top.groupby(['company_continent_name', 'job_title'])['salary_in_usd'].agg(['mean', 'std'])
data_salary_job_continents_mean = pd.DataFrame(data_salary_job_continents_mean).reset_index(drop = False)
data_salary_job_2continents_mean = data_salary_job_continents_mean.loc[(data_salary_job_continents_mean['company_continent_name']== 'Europe') | (data_salary_job_continents_mean['company_continent_name']== 'North America')]



# PLOT 

plt.figure(figsize=(8, 6))
sns.pointplot(
    x='company_continent_name',
    y='mean',
    hue='job_title',
    data=data_salary_job_2continents_mean,
    dodge=True,  # Separate the points for better visibility
)
plt.xlabel('Continent')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary for Job Titles in Europe and North America')
plt.legend(bbox_to_anchor=(0, 1), loc='upper left')  # Adjust legend position

# Thousand separator
def format_thousands(x, pos):
    return '{:,.0f}K'.format(x / 1000)

formatter = FuncFormatter(format_thousands)
plt.gca().yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.show()


# Verifica la presencia de NaNs o infinitos en tu DataFrame
print(data_salary_job_2continents_mean)  # Para identificar valores faltantes

# ANOVA TWO WAYS

# Statsmodels: doesnt calculate Effect Size by him self
formula = 'salary_in_usd ~ C(job_title) + C(company_continent_name) + C(job_title):C(company_continent_name)'
model = ols(formula, data_salary_job_continents).fit()
res_anova_two = anova_lm(model, typ = 2)

# We add to the table the effect sizes (eta and omega)
eta_squared(res_anova_two)
omega_squared(res_anova_two)

print(res_anova_two.round(3))

# Now we see the fit of the residual
res = model.resid 
fig = sm.qqplot(res, stats.t, fit=True, line="45")
plt.show()

# Post hoc test. We need to do one by one
jobs = pairwise_tukeyhsd(data_salary_job_continents['salary_in_usd'], data_salary_job_continents['job_title'], alpha=0.05)
continents = pairwise_tukeyhsd(data_salary_job_continents['salary_in_usd'], data_salary_job_continents['company_continent_name'], alpha=0.05)

print(jobs.summary())
print(continents.summary())

