def conversion_C_F(temp_c):
    '''UDF to convert temperatures in C to F'''
    temp_f = temp_c * 9/5 + 32
    return temp_f

def line_equation(a, b, x):
    '''UDF to solve the equation of a line given (a, b, x). The output is y = a * x + b'''
    y = a * x + b
    return y

def equations(a, b, x):
    '''UDF to solve two equations of a line given (a, b, x). The output are y1 = a * x + b and y2 = a * x'''
    y1 = a * x + b
    y2 = a * x
    return y1, y2

def histo_par(l, label):
    
    '''UDF that print the histogran of an array or serie with the basic statistical parameters. The label is name of the array just for plotting'''
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    l = l[~np.isnan(l)]
    
    plt.hist(l)
    plt.axvline(x=np.mean(l)-np.std(l), ls="--", color='red', label='mean-std')
    plt.axvline(x=np.percentile(l,33), ls="--", color='green', label='p33')
    plt.axvline(x=np.percentile(l,66), ls="--", color='brown', label='p66')
    plt.axvline(x=np.mean(l), ls="--", color='black', label='mean: '+str(np.mean(l)))
    plt.axvline(x=np.mean(l)+np.std(l), ls="--",color='blue', label='mean+std')        
    plt.xlabel(label)
    plt.ylabel('frequency')
    plt.grid(True)
    plt.legend()

def basic_stat(l):
    
    '''UDF that print basic statistical parameters of an array or serie'''
    
    import numpy as np
    
    l = l[~np.isnan(l)]   
    
    l_range = np.max(l) - np.min(l)

    # Stat of l
    
    print('samples     =', len(l))
    print('range       =', l_range)
    print('min         =', np.min(l))
    print('p33         =', np.percentile(l,33))
    print('mean        =', np.mean(l))    
    print('p66         =', np.percentile(l,66))    
    print('max         =', np.max(l))
    print('std         =', np.std(l))
    print('mean + 3std =', (np.mean(l) + 3*np.std(l)))
    
def log_mlog(l, label, ml):
    
    '''UDF for reporting and plotting histograms with basic statistical parameters of a log and mask or filter log'''
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    l = l[~np.isnan(l)]
    ml = ml[~np.isnan(ml)]

    log_range = np.max(l) - np.min(l)

    # Report of l
    
    file = open('Output/'+label+'_stat.txt', "w")
    
    file.writelines("Statistics of "+label+" \n")
    file.writelines(" \n")
    file.writelines("Minimum value          :"+str(np.min(l))+" \n")   
    file.writelines("P33                    :"+str(np.percentile(l,33))+" \n")      
    file.writelines("Mean                   :"+str(np.mean(l))+" \n")   
    file.writelines("P66                    :"+str(np.percentile(l,66))+" \n")    
    file.writelines("Maximum value          :"+str(np.max(l))+" \n")
    file.writelines("Range                  :"+str(log_range)+" \n")
    file.writelines("Standard deviation     :"+str(np.std(l))+" \n")
    file.writelines("Mean + 3std            :" + str((np.mean(l) + 3*np.std(l)))+" \n")     
    file.writelines(" \n")

    # Report of ml (filter l)
    
    ml_range = np.max(ml) - np.min(ml)

    file.writelines("Statistics of filter "+label+" \n")
    file.writelines(" \n")
    file.writelines("Minimum value          :"+str(np.min(ml))+" \n")
    file.writelines("P33                    :"+str(np.percentile(ml,33))+" \n")      
    file.writelines("Mean                   :"+str(np.mean(ml))+" \n")   
    file.writelines("P66                    :"+str(np.percentile(ml,66))+" \n")   
    file.writelines("Maximum value          :"+str(np.max(ml))+" \n")
    file.writelines("Range                  :"+str(ml_range)+" \n")
    file.writelines("Mean                   :"+str(np.mean(ml))+" \n")
    file.writelines("Standard deviation     :"+str(np.std(ml))+" \n")
    file.writelines("Mean + 3std            :" +str((np.mean(ml) + 3*np.std(ml)))+" \n")             
    file.close()

    # Histogran of l
    
    plt.subplot(1, 2, 1)
    plt.hist(l)
    plt.axvline(x=np.mean(l)-np.std(l), ls="--", color='red', label='mean-std')
    plt.axvline(x=np.mean(l), ls="--", color='black', label='mean: '+str(np.mean(l)))
    plt.axvline(x=np.mean(l)+np.std(l), ls="--",color='blue', label='mean+std')        
    plt.xlabel('Original '+label)
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)

    # Histogran of ml (filter l)
    
    plt.subplot(1, 2, 2)
    plt.hist(ml)
    plt.axvline(x=np.mean(ml)-np.std(ml), ls="--", color='red', label='mean-std')
    plt.axvline(x=np.mean(ml), ls="--", color='black', label='mean: '+str(np.mean(ml)))
    plt.axvline(x=np.mean(ml)+np.std(ml), ls="--", color='blue', label='mean+std')
    plt.xlabel('Filter '+label)
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)