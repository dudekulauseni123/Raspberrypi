''' numpy.correlate '''
import time
import numpy 
import numpy as np
start_time = time.time()
# Our data set 
data = numpy.loadtxt('input_samples_10000k.txt')
# Delay (lag) range that we are interesting in
lags = range(10)
x = numpy.array(data) 
# Mean
mean = numpy.mean(data)
# Variance
var = numpy.var(data)
# Normalized data
ndata = data - mean
acorr = numpy.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
acorr = acorr / var / len(ndata)
#print(acorr)
print("Execution Time: %s" % (time.time() - start_time))
