import numpy as np
import numpy
h = [3, 16, 156, 47, 246, 176, 233, 140, 130, 101, 166, 201, 200, 116, 118, 247, 209, 52, 153, 232, 128, 27, 192, 168, 208, 187, 228, 86, 30, 151, 18, 254, 76, 112, 67, 244, 179, 150, 89, 49, 83, 147, 90, 33, 6, 158, 80, 35, 186, 127]
x= [127, 186, 35, 80, 158, 6, 33, 90, 147, 83, 49, 89, 150, 179, 244, 67, 112, 76, 254, 18, 151, 30, 86, 228, 187, 208, 168, 192, 27, 128, 232, 153, 52, 209, 247, 118, 116, 200, 201, 166, 101, 130, 140, 233, 176, 246, 47, 156, 16, 3]
mean = numpy.mean(h)
# Variance
var = numpy.var(h)
# Normalized data
ndata = h - mean
y = np.convolve(h,x) / var / len(ndata)
x=len(y)
print(x)
print(y)
