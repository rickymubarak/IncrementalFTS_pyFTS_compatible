'''
Created on Jun 30, 2018

@author: rcpsi
'''
from SilvaIncrementalFTS import SilvaIncrementalFTS as sFTS
from SilvaIncDistributionRestartFTS import SilvaIncDistributionRestartFTS as rFTS
from pyFTS.data import TAIEX
from matplotlib import pyplot as mplt
import numpy as np

def main():
    # Fuzzy set type

    print('Testing  SilvaIncDistributionRestartFTS')
    
    fts = sFTS(do_plots = False)

    data = TAIEX.get_data()
    data = list(data[0:1000])*4 #+ list(np.array(data[0:1000]) * 4) + list(data[0:1000]) 
    
    #data = data - data[0]
    #data = list(data) + list(data*10 - np.mean(data)) + list(data)
    

    print(len(data))
    fts.train(data[0:2])
    forecasts = fts.forecast(data[2:len(data)])
    
    mplt.plot(np.arange(2,len(data))+1,forecasts,'b')            
    mplt.plot(np.arange(2,len(data)),data[2:len(data)],'r')
    mplt.show()
    
    fts.print_rules()
        

if __name__ == '__main__':
    main()