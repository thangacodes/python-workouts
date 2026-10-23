import time

print(f"tuple is immutable: you cannot change it after creation.")
#first exmaple for tuple:
print("")
print(f"first example program for tuple")

server_config = ("production", 8080, "nginx")

environment = server_config[0]
port = server_config[1]

print(environment)
print(port)


time.sleep(1)
#second example for tuple
print(f"second example program for tuple")
server_details = ("web1", "web2", "web3")
server1 = server_details[0]
server2 = server_details[1]
server3 = server_details[2]

print(f"server1 name is: {server1}")
print(f"server2 name is: {server2}")
print(f"server3 name is: {server3}")

# third example for tuple
print(f"third example program for tuple")
def get_best_ai():
    return "chatgpt", "gemini"
openai, google = get_best_ai()
print(openai)
print(google)
