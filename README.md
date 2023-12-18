# Raspberrypi & Jetson nano
# Time series autocorrelation 
 - We would like to experiment and see Can raspberry pi and/or nano do time series autocorrelation for large data
   sets. Data set usually will contain about 40e6 to 1.5 e8 points and will be sampled uniformly
# Concluison
- Overall, RaspberryPi is faster to execute the autocorrelation than Jetson Nano. However, both have limitaions
  depending on the number of samples taken and the method of implementation. For example, when 20 million
  samples were taken both output produced ”killed”.
