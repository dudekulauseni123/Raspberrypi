''' Statsmodels '''
import numpy
import time
start_time = time.time()
# Our data set 
data = numpy.loadtxt('input_samples_20000k.txt')

# Delay (lag) range that we are interesting in
lags = range(10)



import statsmodels.api as sm

acorr = sm.tsa.acf(data, nlags = len(lags)-1)
#print(acorr)

print("Execution Time: %s" % (time.time() - start_time))
