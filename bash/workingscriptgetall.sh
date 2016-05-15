#!/usr/bin/env bash
z=0
i=07
y=2013
while [  $y -lt 2017 ]; do
	wget https://s3.amazonaws.com/tripdata/$y$i-citibike-tripdata.zip
	if [ $i -lt 10 ]; then	
		wget https://s3.amazonaws.com/tripdata/$y$z$i-citibike-tripdata.zip
	fi
	if [ $i = 12 ]; then
		i=1
		((y++))
	else
		((i++))
	fi
done
unzip '*.zip'
rm -r *.zip
mv *.csv ./../bike_data/
