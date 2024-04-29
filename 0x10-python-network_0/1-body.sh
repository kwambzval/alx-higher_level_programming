#!/bin/bash
# Fetches & displays response body for 200 status code (silent mode)
curl -s -o /dev/null -w "%{http_code}\n"  "$@" | grep 200 && curl -s "$@"
