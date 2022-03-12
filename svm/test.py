#TESTING
import subprocess
test_data=[(1300,44.684),(9400,48.1935),(2000,51.7318),(8600,46.4821),(7300,83.0882),(7300,43.3091)]
for i,j in test_data:
    subprocess.run('sudo python3 classifier_argv.pu',[i,int(j)])
