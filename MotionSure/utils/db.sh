#!/bin/bash

# Set variables for database parameters
phoneNumber="$1"

dbUsername="team_qa"
dbName="otp"
dbHost="10.10.20.20"
dbPort="5432"
dbPassword="4321lupa"
SQLQuery="select otp from otps s where recipient like '%$phoneNumber' and verified=false order by created_at desc limit 1;"

# Suppress warning message and connect to the PostgreSQL database directly to get the OTP value
otpValue=$(PGPASSWORD="$dbPassword" /opt/homebrew/Cellar/postgresql@14/14.10/bin/psql -U "$dbUsername" -d "$dbName" -h "$dbHost" -p "$dbPort" -t -c "$SQLQuery" | grep -oE '\b[0-9]+\b')

# Extract the last line from otpValue
lastLine=$(echo "$otpValue" | tail -n 1)

# Print the OTP value from the last line
echo "$lastLine" | grep -o '[0-9]\+'

