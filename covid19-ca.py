#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


df = pd.read_csv(r"C:\Users\nidhi\Downloads\vaccination-coverage-map.csv")


# In[3]:


df


# In[4]:


df.isna().sum()


# In[5]:


cols = ["numweekdelta_atleast1dose","numweekdelta_fully",
        "propweekdelta_atleast1dose",
        "propweekdelta_fully","prfname","numtotal_partially",
        "numeligible_partially",
        "propeligible_partially","proptotal_partially"]
df.drop(cols,axis = 1,inplace=True)


# In[6]:


df


# In[7]:


df.isna().sum()


# In[8]:


df.rename(columns={"prename": "Province","numtotal_atleast1dose":"num_partial",
                   "numtotal_fully":"num_fully",
                   "proptotal_atleast1dose":"prop_partial",
                  "proptotal_fully":"prop_fully",
                   "numeligible_atleast1dose":"eligible_partial",
                   "numeligible_fully":"eligible_fully",
                   "propeligible_atleast1dose":"prop_eligible_partial",
                  "propeligible_fully":"prop_eligible_fully","pruid":"Province_id"},
          errors="raise",inplace=True)


# In[9]:


df.isna().sum()


# In[10]:


df=df.dropna()


# In[11]:


df


# In[12]:


df.isna().sum()


# In[13]:


df.duplicated(subset=['Province']).sum()


# In[14]:


df["Province"].unique()


# In[15]:


df["Province_id"].unique()


# In[16]:


df = df[df.Province != "Canada" ]


# In[17]:


df


# In[18]:


df["Province"].unique()


# In[19]:


df["Province_id"].unique()


# In[20]:


df.head(20)


# In[21]:


df


# In[22]:


print(type(df.week_end))


# In[23]:


df['week_end'] = pd.to_datetime(df['week_end'])


# In[24]:


df = df.sort_values(by="week_end",ascending=False)


# In[25]:


print(type(df.week_end))


# In[26]:


df


# In[27]:


cols = ["Alberta","Manitoba","Ontario","Quebec",
        "Newfoundland and Labrador",
        "British Columbia",
        "Yukon","Northwest Territories"
       ,"Nunavut","Nova Scotia","Prince Edward Island",
        "New Brunswick","Saskatchewan"]
for i in cols:
    df_data = df[df["Province"]== i]
    fig = px.bar(df_data, x='week_end', y="num_fully", 
                 hover_name = "Province", color_discrete_sequence=["green"],
                 title = ("Number of people fully vaccinated in " + i),
                 range_x=['2021-06-01','2021-09-25'])
    fig.show()
    i=+1


# In[28]:


cols = ["Alberta","Manitoba","Ontario","Quebec",
        "Newfoundland and Labrador",
        "British Columbia","Yukon",
        "Northwest Territories"
       ,"Nunavut","Nova Scotia","Prince Edward Island",
        "New Brunswick","Saskatchewan"]
for i in cols:
    df_data = df[df["Province"]== i]
    fig = px.line(df_data, x='week_end', y="num_partial",
                  hover_name = "Province", color_discrete_sequence=["green"],
                 title = ("Number of people partially vaccinated in " + i),
                  range_x=['2021-06-01','2021-09-25'])
    fig.show()
    i=+1


# In[29]:


df_data = df[df["week_end"]=="2021-09-25"]


# In[30]:


fig = px.pie(df_data, values='prop_fully',
             names='Province',
             title='vaccination share by each province')
fig.show()


# In[31]:


fig = go.Figure(data=[go.Table(
    header=dict(values = 
                ("Province",
                 "Percentage of fully vaccinated population by September 2021"),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_data.Province, df_data.prop_fully],
               fill_color='lavender',
               align='left'))
])

fig.show()


# In[ ]:




