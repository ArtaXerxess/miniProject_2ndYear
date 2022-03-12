import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC



classifier = SVC(kernel = 'linear')

normal_data = np.genfromtxt('strip_norm.csv',delimiter=',')
attack_data = np.genfromtxt('strip_att.csv',delimiter=',')
#print(normal_data,attack_data)
normal_class = np.zeros(int(normal_data.size/2))
attack_class = np.ones(int(attack_data.size/2))

X = np.append(normal_data,attack_data,axis=0)
Y = np.append(normal_class,attack_class,axis=0)



plt.scatter(X[:,0],X[:,1],c=Y,s=50,cmap='spring') 
nscatter = plt.scatter(normal_data[:,0],normal_data[:,1],c='b',marker='o')
ascatter = plt.scatter(attack_data[:,0],attack_data[:,1],c='r',marker='x')
plt.legend((nscatter,ascatter),('Normal Traffic','Attack Traffic'))

plt.title('Packet Reception Rate at target Machine')
plt.ylabel('Time in Seconds')
plt.xlabel('Number of Packets')

x = np.linspace(0,20000)
# (80,20) (20000,100)
m = 1/200
h = 20
y = m*x+h
d = 0.3
p1 = [70,10500]
p2 = [6,90]
plt.plot(p1,p2,'-k')
plt.show()



classifier.fit(X,Y)
if classifier.predict([[1300,int(44.684)]])==[0.]:
    print("NORMAL TRAFFIC")
else:
    print("ATTACK TRAFFIC")
#print(classifer.predict([[10500,100]]))

