##04_streamlit_plotly.py
import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import requests as req

paises = st.multiselect(
     'Paises a visualizar:',
     ['AR', 'BR', 'CH', 'UY','BO'])


# texto
option = st.selectbox(
     'Que datos desea visualizar?',
     ('casos_100k','muertes_100k'))

tipo=option
if st.button('plot'):
    fig = px.line(title=tipo)
    for pais in paises:
          r=req.get('http://corona-api.com/countries/' + pais)
          t=[]
          casos=[]
          muertes=[]
          data=r.json()
          for day in data['data']['timeline']:
                    t.append(day['date'])
                    casos.append(day['new_confirmed'])
                    muertes.append(day['new_deaths'])
          df=pd.DataFrame()
          df.index=pd.to_datetime(t)
          df['casos']=casos
          df['muertes']=muertes
          pop=data['data']['population']/100000
          df['casos_100k']=np.array(casos)/pop
          df['muertes_100k']=np.array(muertes)/pop
          fig.add_scatter(x=df.index, y=df[tipo],name=pais,mode='markers+lines') 
    st.plotly_chart(fig)
else:
     pass