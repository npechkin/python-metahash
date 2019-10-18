#!/bin/bash

cd /home/user/metahash/examples

LOGS=logs
if [ ! -d "$LOGS" ]; then
    mkdir $LOGS
fi

d=`date -u '+%Y-%m-%d'`
touch logs/$d

#./sending.py >> logs/$d

#sleep 5
#./reinvest.py >> logs/$d

#sleep 5
./balance.py >> logs/$d
