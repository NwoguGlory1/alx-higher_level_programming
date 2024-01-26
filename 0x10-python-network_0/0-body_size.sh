#!/bin/bash
#Script that takes in URL, sends request to the URL
#and displays  the size of the body of the response

curl -s http://0.0.0.0:5000
curl -s -X POST -d "key1=value1&key2=value2" http://0.0.0.0:5000
curl -s -w "%{size_download}\n" -o /dev/null http://0.0.0.0:5000
