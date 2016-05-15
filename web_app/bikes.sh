#!/usr/bin/env bash
z=0
m=`date +%m`
endmon=12
twenty=20
y=`date +%y`
prevYear=y-1
echo $m
if [ $m = 1 ]; then	
	wget https://s3.amazonaws.com/tripdata/$twenty$prevYear$endmon-citibike-tripdata.zip
elif [ $m -lt 11 ]; then
    ((m--))
	wget https://s3.amazonaws.com/tripdata/$twenty$y$z$m-citibike-tripdata.zip
else
	wget https://s3.amazonaws.com/tripdata/$twenty$y$mon-citibike-tripdata.zip
fi
unzip '*.zip'
rm -r *.zip
mv *.csv ./../bike_data/