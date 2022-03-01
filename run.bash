#!/bin/bash

echo "~~~Running Main.py~~~"
#if no args supplied, it'll just run the code
if [ $# -eq 0 ] 
    then

       echo "Usage for encryption: ./run.bash"
       python3 main.py
       
fi

#if given an output file name, the code will run and create a result file
#if [ $# -eq 1 ] 
#then
#    echo "Running main.py"
#   python3 main.py $1
#fi

echo "~~~Finished running!~~~"

