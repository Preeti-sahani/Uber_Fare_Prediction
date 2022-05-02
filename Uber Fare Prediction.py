#!/usr/bin/env python
# coding: utf-8

# In[1]:

# In[2]:


data = pd.read_csv(r'uber data.csv')
testdata = pd.read_csv(r'test.csv')


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


data.describe()


# In[6]:


data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'])


# In[7]:


data['date'] = data['pickup_datetime'].apply(lambda d: d.day)
data['month'] = data['pickup_datetime'].apply(lambda d: d.month)
data['year'] = data['pickup_datetime'].apply(lambda d: d.year)
data['day'] = data['pickup_datetime'].apply(lambda d: d.weekday)
data['hour'] = data['pickup_datetime'].apply(lambda d: d.hour)


# In[8]:


data.drop(['key','pickup_datetime'], axis=1, inplace=True)


# In[9]:


data.dropna(how='any',inplace=True)


# In[10]:


min_lat = -90
max_lat = 90
min_long = -180
max_long = 180


# In[11]:


data.drop(data[(data['pickup_longitude'] < min_long) | (data['pickup_longitude'] > max_long)].index, inplace=True)
data.drop(data[(data['dropoff_longitude'] < min_long) | (data['dropoff_longitude'] > max_long)].index, inplace=True)
data.drop(data[(data['pickup_latitude'] < min_lat) | (data['pickup_latitude'] > max_lat)].index, inplace=True)
data.drop(data[(data['dropoff_latitude'] < min_lat) | (data['dropoff_latitude'] > max_lat)].index, inplace=True)


# In[12]:


fig, axs = plt.subplots(4, figsize=(6,20))
sns.distplot(data['pickup_longitude'], ax=axs[0])
sns.distplot(data['dropoff_longitude'], ax=axs[1])
sns.distplot(data['pickup_latitude'], ax=axs[2])
sns.distplot(data['dropoff_latitude'], ax=axs[3])


# In[13]:


data.drop(data[data['fare_amount']<=0].index,inplace=True)
data.drop(data[data['passenger_count']==0].index,inplace=True)


# In[14]:


data.describe()


# In[15]:


data.info()


# In[16]:


plt.figure(figsize=(15,10))
sns.heatmap(data.corr(), annot=True,cmap='RdYlGn')


# In[17]:


x = data.drop('fare_amount',axis=1)
y = data['fare_amount']


# In[18]:


x.info()


# In[19]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state= 42)


# In[23]:


from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(bootstrap=True, ccp_alpha=0.0,
                                             criterion='mse', max_depth=None,
                                             max_features='auto',
                                             max_leaf_nodes=None,
                                             max_samples=None,
                                             min_impurity_decrease=0.0,
                                             min_impurity_split=None,
                                             min_samples_leaf=1,
                                             min_samples_split=2,
                                             min_weight_fraction_leaf=0.0,
                                             n_estimators=100, n_jobs=None,
                                             oob_score=False, random_state=42,
                                             verbose=0, warm_start=False)


# In[24]:


regressor.fit(x_train,y_train)


# In[25]:


regressor.score(x_train,y_train)


# In[26]:


predict = regressor.predict(x_test)


# In[27]:


from sklearn.metrics import r2_score, mean_squared_error


# In[28]:


print("RMSE is: ", np.sqrt(mean_squared_error(y_test,predict)))


# In[29]:


import pickle

filename = "Uberfile"
outfile = open(filename, "wb")
pickle.dump(regressor, outfile)
outfile.close()


# In[30]:


data.head()


# In[ ]:




