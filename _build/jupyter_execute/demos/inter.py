#!/usr/bin/env python
# coding: utf-8

# # Interactive data visualizations

# 

# In[1]:


import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_notebook
from bokeh.sampledata.iris import flowers
output_notebook()


# In[ ]:


flowers.head()


# In[18]:


type(flowers)


# In[19]:


print(flowers['species'].unique())


# In[20]:


print(len(flowers))


# In[ ]:





# In[21]:


plot = figure (x_axis_label = 'patal_length', y_axis_label = 'sepal_length')
plot.circle(flowers['petal_length'],flowers['sepal_length'])
show(plot)


# In[22]:


type(plot)


# In[23]:


plot = figure (x_axis_label = 'patal_length', y_axis_label = 'sepal_length')
plot.circle(flowers['petal_length'],flowers['sepal_length'])


# In[24]:


from bokeh.models import CategoricalColorMapper

mapper = CategoricalColorMapper(
         factors = [ item for item in flowers['species'].unique() ],
         palette = ['red','green','blue'])

plot.circle('petal_length', 'sepal_length', source=flowers, color={'field': 'species', 'transform': mapper},legend_group = 'species')
plot.legend.location = 'top_left'
show(plot)


# In[25]:


from bokeh.models import HoverTool
hover = HoverTool(tooltips=[('species name', '@species'), ('petal length', '@petal_length'), ('sepal length', '@sepal_length') ])
plot.add_tools(hover)
show(plot)


# plot figure

# In[26]:


from bokeh.layouts import gridplot
plot1 = figure (x_axis_label = 'patal_length', y_axis_label = 'sepal_length')
plot1.circle('petal_length', 'sepal_length', source=flowers, color={'field': 'species', 'transform': mapper})
hover = HoverTool(tooltips=[('species name', '@species'), ('petal length', '@petal_length'), ('sepal length', '@sepal_length') ])
plot1.add_tools(hover)

plot2 = figure (x_axis_label = 'patal_length', y_axis_label = 'sepal_width')
plot2.circle('petal_length', 'sepal_width', source=flowers, color={'field': 'species', 'transform': mapper},legend_group = 'species')
plot2.add_tools(hover)

layout = gridplot([[plot1,None],[plot2,None]])


# In[27]:


show(layout)


# In[28]:


from bokeh.layouts import column
from bokeh.models import Slider

from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature

#From https://github.com/bokeh/bokeh/blob/2.2.3/examples/howto/server_embed/notebook_embed.ipynb


# In[29]:



def bkapp(doc):
    df = sea_surface_temperature.copy()
    source = ColumnDataSource(data=df)

    plot = figure(x_axis_type='datetime', y_range=(0, 25),
                  y_axis_label='Temperature (Celsius)',
                  title="Sea Surface Temperature at 43.18, -70.43")
    
    plot.line('time', 'temperature', source=source)

    def callback(attr, old, new):
        if new == 0:
            data = df
        else:
            data = df.rolling('{0}D'.format(new)).mean()
        source.data = ColumnDataSource.from_df(data)

    slider = Slider(start=0, end=30, value=0, step=1, title="Smoothing by N Days")
    
    slider.on_change('value', callback)

    doc.add_root(column(slider, plot))


# In[30]:


show(bkapp)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




