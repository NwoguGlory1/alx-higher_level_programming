#!/bin/bash
# Sends a JSON POST req to URL passed as Istarg,displays the body of response.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
