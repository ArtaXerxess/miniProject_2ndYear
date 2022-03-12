#!/usr/bin/gawk -f

BEGIN	{
	record=1;
	}

	{
	pkts=100*record;
	if($1==pkts){
	 split($2,tt,":");
	 secs = tt[2]*60+tt[3];
	 printf(pkts "," secs "\n") >> "attack_data100.csv";
	 record++;
 	 }
	}
		


