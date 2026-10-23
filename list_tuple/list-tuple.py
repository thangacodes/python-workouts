# List
print(f"List: values can be changed")
servers = ["nginx", "apache"]
servers.append("redis")
servers[0] = "mysql"
print(servers)

# Tuple
print(f" Tuple: values cannot be changed")
coordinates = (10, 20)
print(coordinates)
