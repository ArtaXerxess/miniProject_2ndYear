import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.svm import SVC



#classifier = SVC(kernel = 'linear')

normal_data = np.genfromtxt('normal_data100.csv',delimiter=',')
attack_data = np.genfromtxt('attack_data100.csv',delimiter=',')
#print(normal_data,attack_data)
print(normal_data.size(),attack_data.size())
