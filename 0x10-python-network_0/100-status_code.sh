#!/bin/bash
# Script that sends displays only status code of response.
curl -s -o /dev/null -w "%{http_code}" "$1"
