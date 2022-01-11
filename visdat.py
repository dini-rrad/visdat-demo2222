#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from bokeh.io import show
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.models import Panel, Tabs, ColorPicker
from bokeh.models import ColumnDataSource, HoverTool


# In[2]:


#reading dataset
df = pd.read_excel("Canada (1).xlsx",sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)


# In[3]:


# add total column
df['Total'] = df.sum(axis=1)

# years that we will be using in this lesson - useful for plotting later on
years = list(map(str, range(1980, 2014)))
print('data dimensions:', df.shape)


# In[4]:


#making data source
source = ColumnDataSource(data={
    'x' : years,
    'y' : df['Total'].head(34)
})


# In[5]:


#ploting for circle graph
p1 = figure(title='data immigration to canada', x_axis_label='Years', y_axis_label='amount',
           plot_width=700, sizing_mode="stretch_width", plot_height=400)

#maikng circle graph
circle = p1.circle(x='x', y='y', source=source, fill_alpha=0.55, color='black')
tab1 = Panel(child=p1, title="circle")


#ploting for line graph
p2 = figure(title='data immigration to canada', x_axis_label='Years', y_axis_label='amount',
           plot_width=700, sizing_mode="stretch_width", plot_height=400)

#making line graph
line = p2.line(x='x', y='y', source=source, line_width=2, line_color='black')
tab2 = Panel(child=p2, title="line")

#making color picker
picker = ColorPicker(title="Color Picker")
picker.js_link('color', line.glyph, 'line_color')
picker.js_link('color', circle.glyph, 'line_color')

#showing plot
show(column(Tabs(tabs=[tab1, tab2]), picker))

