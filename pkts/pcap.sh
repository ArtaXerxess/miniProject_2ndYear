#!/bin/bash

sudo tcpdump ip dst host 10.0.0.1  -n -# -ttttt  -i any -l | tee $1

