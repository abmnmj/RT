# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:03:37 2022

@author: maria
"""
import numpy as np



    
# parameters to define the conic shapes of the dome (all parameters defined in the paper)
c1 = -0.0021
c2 = -0.0005
k1 = -1.2
k2 = -3.9
h1 = 325
h2 = 345 #345


N = 100 #number of rays
D = 1500.
p = np.linspace(-D, D, 1000000) #number of points, represents the x-axis
er = 2.5 #dielectric constant of the dielectric
n2 = np.sqrt(er) #dielectric refractive index
n1 = 1 #air refractive indeix 
wv = 23. # wavelength in mm (defined in the paper)
k0 = 2*np.pi/wv #propagation constant in free space
L = 3*h1 #length of the Array (hmax = L/3) (defined in the paper)
Array = np.linspace (-L/2, L/2, N) #the starting points of the rays over the array
output_angle = 80 #in degrees
MAX_ITERATIONS = 3

m_max = 1000000000 #max slope possible

