#!/usr/bin/bash


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange, dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.cli import CLI


import re

class myTopo(Topo):
    def __init__(self,ns=5,nps=5,**opts):
        super(myTopo,self).__init__(**opts)
        self.numswitch = ns
        self.nodesperswitch = nps


        rootswitch = self.addSwitch('s0')

        victim = self.addHost('h1')
        vicswitch = self.addSwitch('s1')
        self.addLink(victim,vicswitch)

        self.addLink(rootswitch,vicswitch)


        k = 2

        for i in irange(2,self.numswitch):
            switch = self.addSwitch('s%s' % i)
            self.addLink(switch,rootswitch)

            for j in irange(1,self.nodesperswitch):
                host = self.addHost('h%s' % k)
                self.addLink(host,switch)
                k += 1


def atr():

    topo = myTopo(ns=13,nps=7)

    net = Mininet(topo=topo)

    net.start()

#    print "Dumping host connections......"
    print "Generating traffics..."
    hosts = net.hosts
#    CLI(net)
    for host in hosts:
        if str(host)!='h1':
            host.cmd('bash ./normal_packgen.sh &')
    print "Dropping into CLI..."
    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')

    atr()
