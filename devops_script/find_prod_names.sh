######################################################################################################
# Write a function that takes a list of server hostnames and returns only those that belong to production (contain "prod" in the name), sorted alphabetically.
####################################################################################################################

#!/bin/bash
echo ""
echo "Script to find the prod given servers list."

servers=(
  "web-prod-01"
  "db-stage-01"
  "api-prod-03"
  "cache-dev-01"
  "api-prod-01"
)

echo "Given or hardcoded variables.."

printf "%s\n" "${servers[@]}"

for server in "${servers[@]}"; do
    if [[ "$server" == *prod* ]]; then
        echo "$server"
    fi
done
