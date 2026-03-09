import matplotlib.pyplot as plt
import numpy as np

def global_stat(l):
    
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
    return

def global_histo(l, label):
    
    # Histogram of l
    
    plt.hist(l)
    plt.axvline(x=np.mean(l)-np.std(l), ls="--", color='red', label='mean-std')
    plt.axvline(x=np.mean(l), ls="--", color='black', label='mean: '+str(np.mean(l)))
    plt.axvline(x=np.mean(l)+np.std(l), ls="--",color='blue', label='mean+std')        
    plt.xlabel(label.lower())
    plt.ylabel('frequency')
    plt.grid(True)
    plt.legend()
    return
    
def global_mask_stat(l, label, ml):
    
    # l is an array, ml is a subset of l (mask or filter l), label is an string

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
    
#      %matplotlib inline
    
    plt.subplot(1, 2, 1)
    plt.hist(l)
    plt.axvline(x=np.mean(l)-np.std(l), ls="--", color='red', label='mean-std')
    plt.axvline(x=np.mean(l), ls="--", color='black', label='mean: '+str(np.mean(l)))
    plt.axvline(x=np.mean(l)+np.std(l), ls="--",color='blue', label='mean+std')        
    plt.xlabel('original '+label.lower())
    plt.ylabel('frequency')
    plt.legend()
    plt.grid(True)

    # Histogran of ml (filter l)
    
    plt.subplot(1, 2, 2)
    plt.hist(ml)
    plt.axvline(x=np.mean(ml)-np.std(ml), ls="--", color='red', label='mean-std')
    plt.axvline(x=np.mean(ml), ls="--", color='black', label='mean: '+str(np.mean(ml)))
    plt.axvline(x=np.mean(ml)+np.std(ml), ls="--", color='blue', label='mean+std')
    plt.xlabel('filter '+label.lower())
    plt.ylabel('frequency')
    plt.legend()
    plt.grid(True)
    
    plt.show()

    return