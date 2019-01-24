# pyfiles
A Large Python Class for the University of Cincinnati's Aerodynamic Simulation. 

You must have the pyfiles class in the same folder as your scripts to use. 
### Requirements
- numpy 
- scipy

### Notes
To interpolate run

    from scipy.interpolate import interp1d
    myint =  interp1d(x,y,3)
    myint(xi)
