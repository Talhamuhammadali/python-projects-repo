#!/bin/bash
n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    echo "Retry $n"
    ((n+=1))
done