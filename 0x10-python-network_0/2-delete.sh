#!/bin/bash
# Script that sends DELETE request to the URL passed as first argument, displays body of the response
curl -sX DELETE $1
