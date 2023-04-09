#!/bin/bash
file="genomas_ftp.txt"
while read -r ftp_address; do
wget --recursive -r "$ftp_address" -P .
done < "$file"
