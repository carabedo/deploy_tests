from flask import Flask, render_template
from flask import request
import pandas as pd
import json
import plotly
import plotly.express as px
import requests as req
import numpy as np

app = Flask(__name__)
@app.route('/',methods=['GET'])
def notdash():
    params=request.args.to_dict()
    paises=json.loads(params['paises'].replace('\'', '"'))
    tipo=json.loads(params['tipo'].replace('\'', '"'))
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
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('notdash.html', graphJSON=graphJSON)
app.run(port=8000,host='0.0.0.0' )# host local puerto el que quieras