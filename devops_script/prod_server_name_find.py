"""
Write a function that takes a list of server hostnames and returns only those that belong to production (contain "prod" in the name), sorted alphabetically.
"""
servers = [
    "web-prod-01",
    "db-stage-01",
    "api-prod-03",
    "cache-dev-01",
    "api-prod-01"
]

def find_prod_machine():
    print(servers)
    print("Only print the given variables containing prod in their names")
    print ("")
    prod_exists = False
    for server in servers:
        if "prod" in server.lower():
            print(f"Prod server found: {server}")
            prod_exists = True
    if not prod_exists:
        print("No prod servers exist")

find_prod_machine()
