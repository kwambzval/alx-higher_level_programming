#!/bin/bash
if [[ $(curl -s -o /dev/null -w "%{http_code}") == "200" ]]; then
  curl -s "$1"
fi