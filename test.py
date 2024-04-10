# test to find temperature at a given geophysical condition

import os,sys
import numpy as np

path_dir = '~/MCD6.1/mcd-python/'
sys.path.append(path_dir)

# This python program illustrates how the Mars Climate Database
# fortran routines can be called interactively from python

from fmcd import mcd

# 1. Inputs:
dset = '~/MCD6.1/MCD6.1/data/' # default to 'MCD_DATA'
dust = 1  
'''
# 1.4 Dust and solar scenario
print("Dust scenario?")
print("1= Climatology       typical Mars year dust scenario")
print("                     average solar EUV conditions")
print("2= Climatology       typical Mars year dust scenario")
print("                     minimum solar EUV conditions")
print("3= Climatology       typical Mars year dust scenario")
print("                     maximum solar EUV conditions")
print("4= dust storm        constant dust opacity = 5 (dark dust)")
print("                     minimum solar EUV conditions")
print("5= dust storm        constant dust opacity = 5 (dark dust)")
print("                     average solar EUV conditions")
print("6= dust storm        constant dust opacity = 5 (dark dust)")
print("                     maximum solar EUV conditions")
print("7= warm scenario     dustier than Climatology scenario")
print("                     maximum solar EUV conditions")
print("8= cold scenario     clearer than Climatology scenario")
print("                     minimum solar EUV conditions")
'''
datekey   = 1        # 1 = "Mars date" ; 0 = "Earth date"
xdate = float(71)    # the value of Ls
loct = float(4.6)    # LT only if datekey =1

zkey      = 2  # xz is the altitude above the Martian zero datum (Mars geoid or “areoid”)
#1: distance to center of planet, 2: height above areoid, 3: height above surface, 4: Pressure
xz = float(120000)   # in meters, depends on zkey

lon = float(160.9)   # east longitude
lat = float(23.6)    # latitude

hrkey     = 1  #set high resolution mode on (hrkey=0 to set high resolution off)
perturkey = 0  #integer perturkey ! perturbation type (0: none)
seedin    = 1  #random number generator seed (unused if perturkey=0)
gwlength  = 0. #gravity Wave wavelength (unused if perturkey=0)

extvarkey = 0  #output extra variables
if (extvarkey == 0) :
    extvarkeys = np.zeros(100)
else :
    extvarkeys = np.ones(100)   #extvar index 0 to 99

(pres, dens, temp, zonwind, merwind, \
 meanvar, extvar, seedout, ierr) \
 = mcd.call_mcd(zkey,xz,lon,lat,hrkey, \
 datekey,xdate,loct,dset,dust, \
 perturkey,seedin,gwlength,extvarkeys )

print(temp)
