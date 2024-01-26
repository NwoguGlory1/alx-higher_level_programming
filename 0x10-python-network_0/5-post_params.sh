#!/bin/bash
# Script that takes in URL, sends POST request to the passed URL, displays body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
