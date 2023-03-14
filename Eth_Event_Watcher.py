#5m477
#twitter.com/5m477

from web3 import Web3
import asyncio
import json
import colorama
from colorama import Fore, Style
import pyfiglet

# Initialize colorama module
colorama.init()

# Print welcome message
print(pyfiglet.figlet_format("Event Subscriber", font="slant"))

# Prompt for connection URL and create web3 instance
url = input("Enter connection URL for Ethereum node (e.g. http://127.0.0.1:7545): ")
web3 = Web3(Web3.HTTPProvider(url))

# Prompt for contract address and ABI
target_address = input("Enter contract address: ")
target_ABI = input("Enter contract ABI: ")

# Create contract instance
target = web3.eth.contract(address=target_address, abi=target_ABI)

# Prompt for filter options
from_block = input("Enter starting block number for event filter (default is 'latest'): ")
to_block = input("Enter ending block number for event filter (default is 'latest'): ")

# Set default values if user input is blank
if from_block == "":
    from_block = "latest"
if to_block == "":
    to_block = "latest"

# Create event filter for DepositLog
event_filter = target.events.[EVENTNAME].createFilter(fromBlock=from_block, toBlock=to_block)

# Define event handler function
def event_handler(event):
    # Parse event data
    sender = event["args"]["sender"]
    value = event["args"]["value"]
    message = event["args"]["message"]

    # Print event data with colors
    print(f"{Fore.GREEN}New deposit event detected!")
    print(f"Sender: {sender}")
    print(f"Value: {value} wei")
    print(f"Message: {message}{Style.RESET_ALL}\n")

# Define event loop function
async def event_loop(filter, interval):
    while True:
        for event in filter.get_new_entries():
            event_handler(event)
        await asyncio.sleep(interval)

# Prompt for polling interval
interval = int(input("Enter polling interval in seconds: "))

# Run event loop with user-specified options
print(f"{Fore.YELLOW}Starting event loop...")
print(f"Filtering from block {from_block} to {to_block}, polling every {interval} seconds.{Style.RESET_ALL}\n")
asyncio.run(event_loop(event_filter, interval))
