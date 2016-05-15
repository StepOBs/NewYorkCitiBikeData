#!/usr/bin/env bash
z=0
m=`date +%m`
mon=m-1
endmon=12
y=`date +%y`
prevYear=y-1
if [ $m = 1 ]; then	
	wget https://s3.amazonaws.com/tripdata/$prevYear$endmon-citibike-tripdata.zip
else if [ $mon -lt 10 ]; then	
	wget https://s3.amazonaws.com/tripdata/$y$z$mon-citibike-tripdata.zip
else
	wget https://s3.amazonaws.com/tripdata/$y$mon-citibike-tripdata.zip
fi
unzip '*.zip'
rm -r *.zip
mv *.csv ./../bike_data/
