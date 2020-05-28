# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:23:03 2020

@author: qtckp
"""

import plotly.graph_objects as go
import numpy as np
from plotly.offline import plot


def plot_function3D(f, xmin=5, xmax=10, ymin=-5, ymax=5,xcount=50,ycount = 50, title = 'function 3D', savepath=None):
    z = np.empty((xcount,ycount))
    x= np.linspace(xmin,xmax,xcount)
    y=np.linspace(ymin,ymax,ycount)
    for row in range(xcount):
        for col in range(ycount):
            z[row,col]=f(x[row],y[col])
            
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
    fig.update_layout(title=title, autosize=True,
                  scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                  #width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90)
                  )

    if savepath != None:
        fig.write_html(savepath)  

    #fig.show()
    plot(fig)
    
  
    






#import plotly.io as pio
#pio.renderers.default = "browser"


