# %% [markdown]
# # Senior Reviewer's Solution: Business Analytics
# 
# **Goal:** To help marketers reduce costs by eliminating unprofitable traffic sources and reallocating the budget.
# 
# **Data**. There is Yandex.Afisha data from June 2017 to the end of May 2018:
# 
# - server log with data about visits to the Yandex.Afisha website,
# - unloading of all orders for this period,
# - advertising spending statistics.
# 
# **Tasks:**
# 
# how customers use the service,
# 
# when they make their first purchases on the site,
# 
# how much money each client brings to the company,
# 
# when the cost of attracting a client pays off.
# 
# Note. Revenue is measured in conventional units - c.u.

# %% [markdown]
# ## Preprocessing

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np    
import seaborn as sns
pd.set_option('display.max_columns', None)


# %%
visits  = pd.read_csv('https://code.s3.yandex.net/datasets/visits_log.csv')
costs = pd.read_csv('https://code.s3.yandex.net/datasets/costs.csv')
orders = pd.read_csv('https://code.s3.yandex.net/datasets/orders_log.csv')

# %%
def first_look (df):
  print ('------------- first 5 rows ------------')
  (df.head())
  print('')
  print('')
  print ('------------- data types ------------')
  print (df.info())
  print('')
  print('')
  print ('------------- missing values ------------')
  count = 0
  for element in df.columns:
    if df[element].isna().sum() > 0: 
      print(element, ' - ', df[element].isna().sum(), 'missing values')
      count = +1
  if count == 0:
    print('No missing values')
  print('')
  print('')
  print ('------------- Duplicates ------------')
  if df.duplicated().sum() > 0:
    print('Duolicates: ', df.duplicated().sum())
  else:
    print('No duplicates')

# %% [markdown]
# ### Visits

# %%
first_look(visits)

# %% [markdown]
# There are no missing values or duplicates.
# 
# We need to rename the columns.
# 
# We need to change the data types in the date columns.
# 
# It would be good to evaluate how many sources and types of devices we have and how data is distributed across them.
# 
# It would be good to lookat the minimum and maximum dates in the dataset.

# %%
#change types
visits['Start Ts'] = pd.to_datetime(visits['Start Ts'], format="%Y-%m-%d %H:%M:%S")
visits['End Ts'] = pd.to_datetime(visits['End Ts'], format="%Y-%m-%d %H:%M:%S")

#rename columns
visits = visits.rename(columns={"Device": "device", "End Ts": "session_end_ts", "Source Id": "source_id", "Start Ts": "session_start_ts", "Uid": "uid"})

#check
visits.head()

# %% [markdown]
# ##### option

# %%
#check devices
visits.value_counts('device')

# %% [markdown]
# We can change column to the category type, because we only have 2 types of devices.
# 
# More visits come from PC than from mobile devices.

# %%
# check sources
visits.value_counts('source_id')

# %% [markdown]
# There were only 10 sources.
# 
# From the 8th source, users did not come at all (or did they decide to abandon it?)
# 
# From 6 and 7, very few users came. Most likely, they will fall out of further analysis, or we will have to delete them.

# %%
#check date
visits['session_start_ts'].min(), visits['session_start_ts'].max(), visits['session_end_ts'].min(), visits['session_end_ts'].max()


# %% [markdown]
# The minimum start and end dates of sessions correspond to the description of the data. 
# 
# The maximum session start date also matches the conditions. 
# 
# But the last session ended after May 2017. It would be nice to see how many of these sessions we have.

# %%
visits[visits['session_end_ts'] > '2018-06-01']

# %% [markdown]
# 11 sessions began in May 2017 and ended in June 2018. If a purchase was made during these sessions, it can already be attributed to the time interval specified in the assignment. 
# 
# We can delete these sessions - they make up less than 1% of the data. But, since students rarely do this, and we need numbers as close as possible to their correct decisions, we will leave these rows.

# %% [markdown]
# ##### end option

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
# 
# 
# Most likely, students will limit themselves to changing the data type in columns with dates, searching for missing values, and checking for duplicates. If the student doesn't do any of it, it is a serious mistake, a red comment.
# 
# Depending on what else the student did, you can give them a piece of advice:
# 
# - To rename the columns.
# - To check whether the data corresponds to the time interval specified in the task; whether the sessions go beyond its boundaries.
# - To find out what devices the visitors are using and whether it is possible to change the data type in the Device column to Category. More on this data type:https://coderlessons.com/tutorials/python-technologies/vyuchit-python-panda/python-pandas-kategoricheskie-dannye
# - To find out what traffic sources we have and how visitors are distributed among them.
# </div>

# %% [markdown]
# ### Orders

# %%
first_look(orders)

# %% [markdown]
# The same work here.

# %%
orders['Buy Ts'] = pd.to_datetime(orders['Buy Ts'])

orders = orders.rename(columns={"Buy Ts": "buy_ts", "Revenue": "revenue", "Uid": "uid"})

orders.head()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
# 
# Most likely, students will limit themselves to changing the data type in columns with dates, searching for missing values, and checking for duplicates. If the student doesn't do any of it, it is a serious mistake, a red comment.
#     
# Depending on what else the student did, you can give them a piece of advice:
#     
# - To rename the columns.
# - To check whether the data corresponds to the time interval specified in the task; whether the sessions go beyond its boundaries.
# </div>

# %% [markdown]
# ### Costs

# %%
first_look(costs)

# %% [markdown]
# The same here.

# %%
costs['dt'] = pd.to_datetime(costs['dt'])
costs['dt'].min(), costs['dt'].max()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# Most likely, students will limit themselves to searching for missing values and checking for duplicates. If the student doesn't do any of it, it is a serious mistake, a red comment.
#     
# Depending on what else the student did, you can give them an advice to check whether the data corresponds to the time interval specified in the task; whether the sessions go beyond its boundaries.
# 
# </div>

# %% [markdown]
# # Make reports and calculate metrics

# %% [markdown]
# ## Product

# %% [markdown]
# ### How many people use it every day, week, and month?

# %%
visits['session_month'] = visits['session_start_ts'].dt.month
visits['session_week']  = visits['session_start_ts'].dt.isocalendar().week
visits['session_date']  = visits['session_start_ts'].dt.date

visits.head()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# Very often students try to calculate the number of the week/month of the year instead of calculating the "first day" of the week/month. 
#     
# In this case, it is worth leaving a yellow comment: "In this dataset, the calculation of the week/month number can be misleading, because June 2018 will come immediately after May 2017 (you will see this on the charts below). And if this dataset had data for several years, such an approach would lead to critical errors, because months of different years would be combined into one. It is recommended to use astype('datetime64[M]') / astype('datetime64[W]') methods."
#     
#     
# If the student used the astype('datetime64[W]') method, you can give a piece of advice that this method looks for a Wednesday in each week, not Monday. And that they should think about considering Monday as the first day.
# 

# %%
dau = visits.groupby('session_date').agg({'uid': 'nunique'})
wau = visits.groupby('session_week').agg({'uid': 'nunique'})
mau = visits.groupby('session_month').agg({'uid': 'nunique'})

print('DAU:', int(dau.mean()), 'visitors')
print('WAU:', int(wau.mean()), 'visitors')
print('MAU:', int(mau.mean()), 'visitors')

# %%
fig, ax = plt.subplots(1, 3, figsize=(19, 5))
ax[0].plot(dau)
ax[0].set(title = 'DAU', xlabel = 'date', ylabel = 'visitors')
ax[1].plot(wau)
ax[1].set(title = 'WAU', xlabel = 'date', ylabel = 'visitors')
ax[2].plot(mau)
ax[2].set(title = 'MAU', xlabel = 'date', ylabel = 'visitors')
fig.autofmt_xdate(rotation=30)
plt.show()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# If above the student calculated the number of the week/month in the year, then the graphs will have an anomaly: DAU with a peak in the center, WAU and MAU - with a dip in the center. Draw the student's attention to this contradiction.
#     
# If the student chooses hist as the chart type, check if they have chosen the optimal number of bins: 365, 52, 12. If not, then it is a serious mistake, leave a red comment (it's very easy to fix it and the informativity of the graphs will increase significantly).
#     
# The minimal result: to plot graphs and to specify the DAU, WAU, MAU average values.  If it's not done, then it is a serious mistake, leave a red comment. If the student has done only the necessary minimum, you can offer them in yellow/green:
#     
# - To identify high and low seasons;
# - To identify a day with an abnormally low number of visits - 2018-03-31 - and suggest a possible reason for the lack of visitors on this day;
# - To identify a day with an abnormally big number of visits - 2017-11-24 - and suggest a possible reason for the rush on this day;
# - To add a grid to the graphs - it allows you to better correlate data along the axes.
# </div>

# %% [markdown]
# ### How many sessions are there per day? (One user might have more than one session.)

# %%
sess_per_user = visits.groupby('session_date').agg({'uid': ['count','nunique']})
sess_per_user.columns = ['n_sessions', 'n_users']
sess_per_user['sess_per_user'] = sess_per_user['n_sessions'] / sess_per_user['n_users']

# %%
plt.figure(figsize= (12,5))
sess_per_user['sess_per_user'].plot().set(title = 'Sessions by user', xlabel = 'date', ylabel = 'sessions');

# %%
print('Average sessions per user is {} by day.'.format(round(sess_per_user['sess_per_user'].mean(),2)))

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
# 
# If the student chooses hist as the chart type, check if they have chosen the optimal number of bins: 365. If not, then it is a serious mistake, leave a red comment.
#     
# The minimal result is to plot a graph and indicate the average value of the metric. If it's not done, then it is a serious mistake, leave a red comment. If the student has done only the necessary minimum, you can offer them:
#     
# - To assess whether the metric changes a lot during the year;
# - To identify days with minimum and maximum values of the metric - whether they coincide with the days of minimum and maximum DAU values.
# - If the student rounded up the value of the metric to an integer (up to 1) - give them a piece of advice to round up such small fractional values to 1-2 decimal places.  A rough rounding of such small values to an integer can introduce a huge error in the value of the metric - up to 50% in some cases.
# </div>

# %% [markdown]
# ### What is the length of each session?

# %%
visits['session_duration_sec'] = (visits['session_end_ts'] - visits['session_start_ts']).dt.seconds
visits['session_duration_sec'].describe()

# %%
plt.figure(figsize= (12,5))
visits['session_duration_sec'].hist(bins=300).set(title = 'Session lenght', xlabel = 'Lenght', ylabel = 'Frequency')
plt.xlim(0,10000)
plt.show()

# %%
print('Mean session lenght is: {:.2f} seconds'.format(visits['session_duration_sec'].mean())) 
print('Median session lenght is: {:.2f} seconds'.format(visits['session_duration_sec'].median()))
print('Mode session lenght is: {} seconds'.format(visits['session_duration_sec'].mode()[0]))

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# The minimal result is to calculate the median and/or mode, plot a histogram of the distribution (or other suitable graph), justify your choice of the average measure in the output.  If it's not done, then it is a serious mistake, leave a red comment. The most common serious mistakes(red comment) are:
#     
# - The median/mode is not calculated, the student only calculates the mean - this metric does not characterize such a skewed distribution well. 
# - The mode/median is given as the average measure, but the histogram is not plotted - students do not justify their choice of the average measure in any way. 
#     
#     
# Frequent minor errors - yellow comment:
# - The student did not specify [0] when calculating the mode and got a less beautiful output. 
# - Student write "model session" instead of "modal session"/"modal session duration".
# 

# %% [markdown]
# ### What's the user retention rate?

# %%
#find first session time
first_visits = visits.groupby('uid').agg({'session_start_ts': 'min'}).reset_index()
first_visits.columns = ['uid', 'first_session_start_ts']
first_visits.head()

# %%
#find first date and month
first_visits['first_session_dt'] = first_visits['first_session_start_ts'].dt.date
first_visits['first_session_month'] = first_visits['first_session_start_ts'].dt.month

#merge
visits_full = pd.merge(first_visits, visits, on = 'uid')

#calculate difference # TODO FIXME error with pandas upgrade 
visits_full['age_months'] = ((visits_full['session_month'] - visits_full['first_session_month']) / (30*np.timedelta64(1,'D'))).round().astype('int')

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# The student doesn't use .round() when rounding - as a result, data is obtained not for periods [0:11], but for periods [0:10].  And "holes" in the heat map. This will be clearly visible on the graph/in the table.
#     
# </div>

# %%
#cohort analysis
cohorts = visits_full.pivot_table(index='first_session_month',
                  columns='age_months',
                  values='uid',
                  aggfunc='nunique')
cohorts.fillna('')

# %%
#Retention Rate
retention = pd.DataFrame()
for col in cohorts.columns:
    retention = pd.concat([retention, cohorts[col]/cohorts[0]], axis=1)
retention.columns = cohorts.columns
retention.index = [str(x)[0:10] for x in retention.index]
plt.figure(figsize=(13, 9))
sns.heatmap(retention, annot=True, fmt='.1%', linewidths=1, linecolor='grey',  vmax=0.1, cbar_kws= {'orientation': 'horizontal'} 
            ).set(title = 'Retention Rate')
plt.show()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# For the calculation, not the first day of the month is calculated, but the ordinal number of the month - as a result, RR will be minimal on the 6th month of the cohorts' lifetime, then it will start growing again. 
#     
# Students do a cohort analysis by week, not by month.  In general, the result is almost impossible to understand and evaluate.  In this case, we ask the student to supplement the calculation with the same cohort analysis by months.
#     
#     
# "Holes" in the heatmap - see senior reviewer's comment above.
#     
# Frequent minor errors, yellow comment:
#     
# Heatmap turns out to be black and white and not very informative - recommend the student to use the vmax parameter of the heatmap method;
#     
# Labels on the y-axis look like "2017-06-01 00:00:00" - recommend the student to think about deleting "00:00:00"
# </div>

# %%
print('{:.1%}'.format(retention[1].mean()))

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# The average Retention Rate for the second month of life of the cohorts is 6.5%. Every month it gets smaller.
#     
# </div>

# %% [markdown]
# <div class="alert alert-block alert-info">
# 
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
# 
# The minimal result is to create an RR heat map, calculate the average RR value for the second month of cohorts' lifetime, and make a conclusion on whether RR is growing with time or decreasing. You can also offer the student to choose the most successful and unsuccessful cohorts according to the RR metric.
#     
# </div>

# %% [markdown]
# ## Sales

# %% [markdown]
# ### When do people start buying?

# %%
#add day and month 
orders['buy_dt']  = orders['buy_ts'].dt.date
orders['order_month'] = orders['buy_ts'].astype('datetime64[M]')

# find first prder time
first_orders = orders.groupby('uid').agg({'buy_ts': 'min'}).reset_index()
first_orders.columns = ['uid', 'first_order_ts']
first_orders['first_order_dt'] = first_orders['first_order_ts'].dt.date
first_orders['first_order_month'] = first_orders['first_order_ts'].astype('datetime64[M]')
first_orders.head()

#create dataframe with first orders and first visits
buyers = pd.merge(first_visits, first_orders, on='uid')
buyers.info()

# %%
buyers['first_order_dt'] = pd.to_datetime(buyers['first_order_dt'])
buyers['first_session_dt'] = pd.to_datetime(buyers['first_session_dt'])

buyers['days_to_first_purchase'] = ((buyers['first_order_ts'] - 
                                     buyers['first_session_start_ts']) / np.timedelta64(1,'D')).astype('int')                                     

# %%
(buyers['days_to_first_purchase'].plot(kind='hist',bins=100, figsize=(12,7))
                                 .set(title = 'Time from visit to order', 
                                      xlabel = 'Days', 
                                      ylabel = 'Frequency'))
plt.xlim(0,100)
plt.show()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# According to the principle "done not worse than in the author's solution", you need to comment in green the answers "buy on the first day" and more accurate ones.  Though this interval can be significantly narrowed.  
#     
# Depending on the degree of accuracy of the answer and the level of the student, you can leave a red or yellow comment about the possibility of specifying a narrower time interval.
#     
# Also, students can interpret the question as "in which session the purchase is made". The correct answer "in the first session" is commented in green. This alternative response method can be given as a recommendation.
# </div>

# %% [markdown]
# ### How many orders do they make during a given period of time?

# %%
#find customers number in each cohort
cohort_sizes = buyers.groupby('first_order_month').agg({'uid': 'nunique'}).reset_index()
cohort_sizes.rename(columns={'uid': 'n_buyers'}, inplace=True)

# add first month
cohorts = pd.merge(orders, buyers, how='inner', on='uid')\
.groupby(['first_order_month', 'order_month'])\
.agg({'revenue': 'count'}).reset_index()

cohorts.head()

# %%
#calculate age
cohorts['age_month'] = ((cohorts['order_month'] - cohorts['first_order_month']) / np.timedelta64(1,'M')).round()
cohorts.columns = ['first_order_month', 'order_month', 'n_orders', 'age_month']

#add customers and count orders
cohorts_report = pd.merge(cohort_sizes, cohorts, on = 'first_order_month')
cohorts_report['orders_per_buyer'] = cohorts_report['n_orders'] / cohorts_report['n_buyers']

# %%
#cohort report
cohorts_ltv = cohorts_report.pivot_table(
    index='first_order_month', 
    columns='age_month', 
    values='orders_per_buyer', 
    aggfunc='sum'
).cumsum(axis=1)

cohorts_ltv.round(2).fillna('')

# %%
print("Mean orders per buyer: ",round(cohorts_ltv[5].mean(), 2))

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# The main criterion for fulfilling this part of the task is that the student receives the number of purchases per customer greater than 1, but less than 1.5. The conclusion is "there are repeated purchases, but they are rare."
#     
# If the student is clearly making mistakes while counting and does not understand at all what exactly needs to be done here, give them advice: "Here you can apply the calculation scheme as in the part about LTV, but instead of the amount of money spent by the customer, count the number of purchases."
# </div>

# %% [markdown]
# ### What is the average purchase size?

# %%
print("Averache purchase is:", round(orders['revenue'].mean(),2))

# %%
orders.pivot_table(index='order_month', values='revenue', aggfunc='mean').plot(legend=None).set(
    title = 'Averache purchasу by month', xlabel = 'month', ylabel = 'у.е.')
plt.show()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
# 
# Students can use a  heatmap for cohort analysis as a graph of metric changes over time. If the calculations are correct, this is a good solution. But in this case, they often make a serious mistake, a red comment: to calculate the average purchase, they take the mean of all values in the cohort analysis matrix. In this case, they get about 3 times the value of the average purchase.
#     
# </div>

# %% [markdown]
# ### OPTION

# %%
order_data = orders.merge(first_orders, how='left', on='uid') 

order_data.head()

# %%
# Calculates median revenue per cohort 
median_purchase=order_data.groupby(['first_order_month','order_month'])['revenue'].median().reset_index()

# Calculates the amount of time between current order and first order 
median_purchase['age_month'] = ((median_purchase['order_month'] - median_purchase['first_order_month']) / np.timedelta64(1,'M')).round()

median_purchase_piv=median_purchase.pivot_table(
    index='first_order_month', 
    columns='age_month', 
    values='revenue', 
    aggfunc='mean'
)

median_purchase_piv.round(2).fillna('')

# %%
median_purchase_piv.index= median_purchase_piv.index.astype(str)
sns.heatmap(median_purchase_piv, annot=True, fmt='.3', linewidths=1, linecolor='grey', vmax=0.1, cbar_kws={'orientation':'horizontal'}).set(title = "Monthly Order Size")
sns.set(rc = {'figure.figsize':(50,30)})
sns.set(font_scale=4)

plt.show()

# %% [markdown]
# ### OPTION END

# %% [markdown]
# ### How much money do they bring? (LTV)

# %%
buyers

# %%
# remember about buyers
cohort_sizes = buyers.groupby('first_order_month').agg({'uid': 'nunique'}).reset_index()
cohort_sizes.rename(columns={'uid': 'n_buyers'}, inplace=True)

#add first month
cohorts = pd.merge(orders, buyers, how='inner', on='uid')\
            .groupby(['first_order_month', 'order_month'])\
            .agg({'revenue': 'sum'}).reset_index()

cohorts.head()

# %%
#calculate age
cohorts['age_month'] = ((cohorts['order_month'] - cohorts['first_order_month']) / np.timedelta64(1,'M')).round()
cohorts.columns = ['first_order_month', 'order_month', 'revenue', 'age_month']

#  add customers and calculate ltv
cohorts_report = pd.merge(cohort_sizes, cohorts, on = 'first_order_month')
cohorts_report['ltv'] = cohorts_report['revenue'] / cohorts_report['n_buyers']

# %%
cohorts_ltv = cohorts_report.pivot_table(
    index='first_order_month', 
    columns='age_month', 
    values='ltv', 
    aggfunc='sum'
).cumsum(axis=1)

cohorts_ltv.round(2).fillna('')

# %%
cohorts_ltv.index=cohorts_ltv.index.astype(str)
sns.heatmap(cohorts_ltv, annot=True, fmt='.2f', linewidths=1, linecolor='grey', cbar_kws= {'orientation': 'horizontal'} 
            ).set(title ='LTV')
plt.show()

# %%
plt.figure(figsize=(13, 9))
sns.heatmap(cohorts_ltv, annot=True, fmt='.2f', linewidths=1, linecolor='grey', cbar_kws= {'orientation': 'horizontal'} 
            ).set(title ='LTV', yticklabels = cohorts_ltv.index.astype('str'))
plt.show()

# %%
print("Average LTV in 6 months is:", round(cohorts_ltv[5].mean(),2))

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# **Most common serious mistakes (red comment):**
#     
# - Students count the number of unique customers in each month and divide the amount of revenue in each month of each cohort's lifetime by the new number of customers. Students get highly overestimated numbers in all months except 0th.
# - LTV is not considered a cumulative total.
# - They consider LTV per visitor, not per customer. Get a very underestimated result. 
#     
# **Yellow comments:**
#     
# - Heatmap turns out to be black and white and not very informative - recommend the student to use the vmax parameter of the heatmap method;
# - Labels on the y-axis look like "2017-06-01 00:00:00" - recommend the student to think about deleting "00:00:00"
#     
# **Possible discrepancy:** They may form cohorts not from the date of the first purchase, but from the date of the first visit. This method has pros and cons:
#     
# - On the one hand, if we use LTV to calculate payback, and at the same time we link customers to the first traffic source, then the money is spent at the moment of attraction. Then it is also logical to form cohorts according to the time of attraction.
# - On the other hand, although almost everyone buys during the first session, some part still makes purchases much later.  And when calculating the "number of customers in a cohort" you need to use a slightly different approach. And so the results are slightly overestimated.
#     
# **In any case**, since "almost all customers make a purchase at the time of the first session"  the discrepancies are not too large and I accept this solution. You can write to the student about the details of the calculation in green.
# You can also give the advice to study the cohort that started on 06/01/2018 - how is it even possible we have it, how many customers are there, how much do we need it and how useful is it.
# 

# %% [markdown]
# ## Marketing

# %% [markdown]
# ### How much money was spent? Overall/per source/over time

# %%
print('Total costs {}'.format(costs['costs'].sum()))

# %%
#add month
costs['costs_month'] = costs['dt'].astype('datetime64[M]')

# %%
(costs.pivot_table(index='costs_month', values='costs', aggfunc='sum')
      .plot(figsize=(14,5), title='Costs by month', xlabel = 'month', ylabel = 'c.u.'))
plt.show()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# Student can forget to calculate it.  The minimum that the student must do is: calculate the total sum of costs for each source, plot a graph of the expenses' dependence on the source over time, and indicate the months of the greatest and least expenses. 
# 
# You can give advice: to compare the sum of total expenses with the amount of total income and draw a conclusion about how much the project pays off.
#     
# </div>

# %%
print('Costs per source:')    
print(costs.groupby('source_id').agg({'costs': 'sum'}))

# %%
(costs.pivot_table(index='costs_month', columns='source_id', values='costs', aggfunc='sum')
      .plot
      .area(figsize=(14,7), title='Costs per source by month', xlabel = 'month', ylabel = 'c.u.'))
plt.show()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# Students rarely make mistakes here, but they can forget to calculate this. The minimum that the student must do is: calculate the total sum of expenses for each source, plot a graph of the expenses' dependence on the source over time, and indicate the most expensive and cheap sources.
#     
# </div>

# %% [markdown]
# ### How much did customer acquisition from each of the sources cost?

# %%
print("Mean CAC is:", round(costs['costs'].sum() / orders['uid'].nunique(), 2))

# %%
#CAC by month
СAC_by_month = pd.merge(costs.groupby('costs_month').agg({'costs': 'sum'}), 
                        buyers.groupby('first_order_month').agg({'uid': 'nunique'}), 
                        left_index=True, 
                        right_index=True)
СAC_by_month['cac'] = СAC_by_month['costs']  / СAC_by_month['uid'] 

СAC_by_month['cac'].plot(figsize=(14,7), title='Average CAC by month', xlabel = 'Month', ylabel = 'c.u.');

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# **VERY IMPORTANT!**
# </div>

# %%
#find first source per visitor
users = visits_full.sort_values('session_start_ts').groupby('uid').first()
users = users[['source_id']]
buyers = pd.merge(buyers, users, left_on='uid', right_index=True)

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
# The student does not sort the data or does not sort it correctly by the date of the first session. As a result, the first source will be found with an error. If the min method is used instead of the first method, sorting will not be needed.
# The student does not remember that each source appears repeatedly in the users table and, in general, does not try to link the user to any source.
#     
# It is important to understand that the student may choose a different method of linking the customer to the source. Instead of "we link to the source of the first visit."  If the student explained their approach and the approach is logical, we comment such a method in green.
# 
# </div>

# %%
buyers_daily = buyers.groupby(['source_id', 'first_order_dt']).agg({'uid': 'count'}).reset_index()
buyers_daily.rename(columns={'uid': 'n_buyers'}, inplace=True)
buyers_daily['first_order_dt'] = pd.to_datetime(buyers_daily['first_order_dt'])

costs_ = pd.merge(buyers_daily, costs, left_on=['source_id', 'first_order_dt'], right_on=['source_id', 'dt'])
costs_['cac'] = costs_['costs']/costs_['n_buyers']

costs_.pivot_table(index=['costs_month'], columns='source_id', values='cac', aggfunc='mean').plot(
    figsize=(16,9), title='CAC by buyer from each source из каждого источника', xlabel = 'month', ylabel = 'c.u.')
plt.show()

# %%
#average CAC by source
costs_.groupby('source_id').agg({'cac': 'mean'}).round(2)

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
# 
# The student must plot a graph and calculate the average CAC values by sources. In the output, you can write which sources have a higher and lower CAC.
#     
# Possible serious mistakes, red comments:
#     
# - the student calculates CAC not by the customer, but by the visitor;
# - the student incorrectly counts the number of customer.
#     
# In any of these cases, CAS is underestimated.
#     
# Small discrepancies are acceptable - usually, they appear due to preliminary grouping.
#     
# In the author's solution, only the last few months are used to calculate the CAC.
# </div>

# %% [markdown]
# ### How worthwhile where the investments? (ROI)

# %%
orders

# %%
#create вацшер order by month and merge with buyers
month_revenue = orders.groupby(['uid', 'order_month']).agg({'revenue': 'sum'}).reset_index()
buyers = buyers.merge(month_revenue,on = 'uid')

# %%
for source, df in buyers.groupby('source_id'):
    if source !=7:

        cohort_sizes_t = (
            df.groupby(['source_id', 'first_order_month'])
            .agg({'uid': 'nunique'})
            .reset_index()
        )
        cohort_sizes_t.columns = ['source_id', 'first_order_month', 'n_buyers']

        cohorts_revenue_t = (
            df.groupby(['source_id', 'first_order_month', 'order_month'])
            .agg({'revenue': 'sum'})
            .reset_index()
        )
        cohorts_revenue_t.columns = ['source_id', 'first_order_month', 'order_month', 'gp']

        report_romi = pd.merge(cohort_sizes_t, cohorts_revenue_t, on=['source_id', 'first_order_month'])
        report_romi['age'] = (
            report_romi['order_month'] - report_romi['first_order_month']
        ) / np.timedelta64(1, 'M')
        report_romi['age'] = report_romi['age'].round().astype('int')
        report_romi['ltv'] = report_romi['gp'] / report_romi['n_buyers']

        report_romi = pd.merge(report_romi,costs.groupby(['source_id', 'costs_month']).agg({'costs': 'sum'}).reset_index(),
                       left_on=['source_id', 'first_order_month'], right_on=['source_id', 'costs_month'])
        report_romi = report_romi.drop(['costs_month'], axis = 1) 
        report_romi['cac'] = report_romi['costs'] / report_romi['n_buyers']
        report_romi['romi'] = report_romi['ltv'] / report_romi['cac']


        romi = report_romi\
                .pivot_table(index='first_order_month', columns='age', values='romi', aggfunc='mean')\
                .cumsum(axis=1)
        romi.round(2).fillna('')

        
        romi.index=romi.index.astype(str)
        sns.heatmap(romi, annot=True, fmt='.2f', linewidths=1, linecolor='grey', cbar_kws= {'orientation': 'horizontal'} 
            ).set(title ='ROMI by source {}'.format(source))
        plt.show()
        
        


# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's Comment </b> <a class="tocSkip"></a>
#     
#     
# Possible serious mistake, red comment: the student does not understand that different sources can have different LTV and takes the average LTV for all sources to calculate the payback.
# 
# We can give advice to fix vmax at 1 for all graphs, it will show which sources pay off and which do not.
# 
# Depending on the calculation, and for how many months the student studies, the roi can be different. But they should not be higher than 200% and, in any case, the 3 and the 10 sources will not pay off.
# 
# In the final conclusion, the student must indicate the sources on which it is no longer worth spending money, and the sources with which it is necessary to continue working.
#     
#     
# </div>


