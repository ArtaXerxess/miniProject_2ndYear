
1. This directory module1 contains four directories.
  - net
  - params
  - pkts
  - svm

2. Start with net directory
3. Run atr_normal.py in one window
   sudo python atr_normal.py
4. Go to pkts directory
5. Run pcap.sh in another window
   sudo pcap.sh normal.pcap
6. Capture for approx. 2 minutes. Then press cntrl - C
7. Do the same thing for attack.

8. Copy normal.pcap and attack.pcap to params directory
9. Go to params directory, use gawk to extract our desired parameters
   gawk -f normal_pkt100.awk normal.pcap
10. Do the same thing for attack
11. Copy the files normal_data100.csv and attack_data100.csv to svm directory.
12. Run svmclassifier.py
    python svmclassifier.py

13. Enjoy.
