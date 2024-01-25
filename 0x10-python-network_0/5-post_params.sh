#!/bin/bash

url=$1
user_id=98

response=$(curl -s -H "X-School-User-Id: $user_id" "$url")

echo "$response"
