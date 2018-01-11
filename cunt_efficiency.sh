#!/bin/bash

file_count=`ls train | wc -l`
correct=0

for file in ./train/*
do
	if [[ $file == *"M"* ]]; then
		gender_in_file="M"
	else
		gender_in_file="K"
	fi

	gender=`python3 ./inf127241_inf127282.py $file`
	
	if [[ $gender_in_file == $gender ]]; then
		((correct++))
	fi
done

correct=$((correct * 100))
efficiency=$(( correct / file_count ))

echo $efficiency"%"
