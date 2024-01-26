#!/bin/bash
# Script that sends request,display size of the body of the response
curl -s "$1" | wc -c
