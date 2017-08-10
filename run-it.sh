#!/bin/bash

for ((i=1; i<=3; i++)); do
    for ((j=10; j<=16; j++)); do 
        echo NN: "($i,$j)"
        python it.py -l $i -n $j
    done
done
