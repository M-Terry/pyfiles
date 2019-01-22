from Pyfiles import PyFiles

pyFile = PyFiles()
I = pyFile.trap('2.0*math.pi*x*(1.0-x**2.0)',0,1,5)
print I