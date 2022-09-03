#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:06:47 2022

@author: namnguyen
"""

#%%
import numpy as np
import math
import streamlit as st
from math import pi, cos, sin
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
import pandas as pd
import os



 #%%
def myDict(u,theta):
     g = 9.8
     theta = np.deg2rad(theta)
     t_flight = 2*u*math.sin(theta)/g
     
     T=[]
     X=[]
     Y=[]
     N=101
     for i in range(N):
         t=(t_flight/(N-1))*i 
         T.append(t)
         x = u*math.cos(theta)*t
         X.append(x)
         y = u*math.sin(theta)*t - 0.5*g*t**2
         Y.append(y)
      
     xdict= {'t':T, 'x': X, 'y': Y} 
     return xdict
 

    
#%%  
def nA(u, theta):
    g = 9.8
    theta = np.deg2rad(theta)
    t_flight = 2*u*np.sin(theta)/g
    t = np.linspace(0, t_flight, 100)
    x = u*np.cos(theta)*t
    y = u*np.sin(theta)*t - 0.5*g*t**2
    
    my_array=np.array([t,x,y])
       
    return my_array


#%%  
def dF(u, theta):
    g = 9.8
    theta = np.deg2rad(theta)
    t_flight = 2*u*np.sin(theta)/g
    t = np.linspace(0, t_flight, 100)
    x = u*np.cos(theta)*t
    y = u*np.sin(theta)*t - 0.5*g*t**2
    
    df=pd.DataFrame({'t': t, 'x': x, 'y': y})
    df.set_index('t')
    df.style.highlight_max(color = 'red', axis = 0)
    def highlight_max(s):
        is_max = s == s.max()
        return ['color: red' if cell else '' for cell in is_max]
  
    final_df=df

    return final_df




#%%
 
#def myPlots(var, color='red',path= 'projectile.gif', name='abc'):
def myPlots(var, color='red', name='abc'):    
    ## transform the var ( container) into list for plotting
    if type(var)== np.ndarray:
        #print('To be developed!')
        #pass
        t=var[0]
        x=var[1]
        y=var[2]
    elif type(var)==dict:
        t=var['t']
        x=var['x']
        y=var['y']
    elif type(var)==pd.DataFrame:
        t=var['t']
        x=var['x']
        y=var['y']
    else:
        print('Out of range')        
        
  
 fig, ax = plt.subplots()
   # line, = ax.plot(x, y, color=color)
    #circle = plt.Circle((0.1, 0.1), radius=np.sqrt(0.01))
    #ax.add_patch(circle)
    #time_text=ax.text(0.65,0.95,'',fontsize=15,transform=ax.transAxes, bbox=dict(facecolor='white',edgecolor='black'))

    #def update(time, x, y, line, circle):
    #    line.set_data(x[:time], y[:time])
    #    circle.center = x[time],y[time]
    #    line.axes.axis([0, max(np.append(x,y)), 0, max(np.append(x,y))])
        
    #    return line,circle
   
  #Plotting
    ax.plot(x,y, color=color, label=name) 
    ax.set_xlim(0, 1000)
    ax.set_ylim(0,200)
    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Height [m]')
    ax.legend()
    return fig


 








    
