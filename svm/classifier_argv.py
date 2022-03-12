import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import sys



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


SOL=[]
classifier.fit(X,Y)
test_data=[(1300,44.684),(9400,48.1935),(2000,51.7318),(8600,46.4821),(7300,83.0882),(7300,43.3091)]
for i,j in test_data:
    if classifier.predict([[i,int(j)]])==[0.]:
        SOL.append([(i,j),"NORMAL TRAFFIC"])
    else:
        SOL.append([(i,j),"ATTACK TRAFFIC"])
print(*SOL)
#[(1300, 44.684), 'NORMAL TRAFFIC'] [(9400, 48.1935), 'ATTACK TRAFFIC'] [(2000, 51.7318), 'NORMAL TRAFFIC'] [(8600, 46.4821), 'ATTACK TRAFFIC'] [(7300, 83.0882), 'NORMAL TRAFFIC'] [(7300, 43.3091), 'ATTACK TRAFFIC']
