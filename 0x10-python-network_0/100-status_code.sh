#!/bin/bash
# This script sends a request to the URL passed as the first argument and displays only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
