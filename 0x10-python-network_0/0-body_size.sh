#!/bin/bash
# This script retrieves response body size from a URL
curl -s -o /dev/null -w "%{size_download}"  "$1"
