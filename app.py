#!/usr/bin/env python
# coding: utf-8



# In[2]:


import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table

# Load RFM + Cluster Data
rfm = pd.read_csv('rfm_data.csv')

app = Dash(__name__)

# Chart: Number of Customers per Cluster
fig_cluster = px.bar(
    rfm['Cluster'].value_counts().sort_index(),
    labels={'value': 'Customer Count', 'index': 'Cluster'},
    title='Customers per Cluster',
    color_discrete_sequence=['teal']
)

# Box plots
fig_recency = px.box(rfm, x='Cluster', y='Recency', title='Recency by Cluster')
fig_frequency = px.box(rfm, x='Cluster', y='Frequency', title='Frequency by Cluster')
fig_monetary = px.box(rfm, x='Cluster', y='Monetary', title='Monetary by Cluster')

# Sample table
sample_table = rfm.groupby('Cluster').head(5)

# Layout
app.layout = html.Div([
    html.H1("Customer Segmentation Dashboard", style={'textAlign': 'center'}),
    
    dcc.Graph(figure=fig_cluster),

    html.Div([
        dcc.Graph(figure=fig_recency),
        dcc.Graph(figure=fig_frequency),
        dcc.Graph(figure=fig_monetary)
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),

    html.H2("Sample Customers by Cluster"),
    dash_table.DataTable(
        data=sample_table.to_dict('records'),
        columns=[{"name": i, "id": i} for i in sample_table.columns],
        style_table={'overflowX': 'auto'},
        page_size=10
    )
])

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host='0.0.0.0', port=port, debug=True)




# In[ ]:




