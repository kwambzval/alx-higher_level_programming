#!/bin/bash
# This script displays response body for successful GET requests
[[ $(curl -s -o /dev/null -w "%{http_code}") == "200" ]] && curl -s "$1"
