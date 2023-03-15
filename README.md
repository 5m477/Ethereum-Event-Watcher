# Ethereum-Event-Watcher

Description:
Event Subscriber is a tool that allows you to subscribe to Ethereum smart contract events and receive real-time notifications. It uses the web3.py library to connect to an Ethereum node and creates an event filter for a specified contract and event. The tool will then continuously poll the blockchain for new events and notify you when a new event is detected.

Usage:

Enter the connection URL for your Ethereum node.
Enter the contract address and ABI for the contract you want to monitor.
Specify the starting and ending block numbers for the event filter (default is 'latest').
Enter the polling interval in seconds.
Start the event loop and wait for new events to be detected.


Requirements:
Python 3.6+
web3.py library
colorama library
pyfiglet library


Installation:
Install Python 3.6 or higher.

this script requires the web3, asyncio, and pyfiglet Python packages. You can install them using pip:
pip install web3 asyncio pyfiglet

Usage
Run the script using the following command:

python eth_event_watcher.py
Enter the connection URL for your Ethereum node when prompted. For example:

Enter connection URL for Ethereum node (e.g. http://127.0.0.1:8545):

Enter the contract address and ABI when prompted. For example:
Enter contract address:
Enter contract ABI:

Enter the starting and ending block numbers for the event filter when prompted. If left blank, the default value is 'latest'. For example:
Enter starting block number for event filter (default is 'latest'):
Enter ending block number for event filter (default is 'latest'):


Enter the name of the event to filter for when prompted. For example:
Enter event name to filter for:

Enter the polling interval in seconds when prompted. For example:
Enter polling interval in seconds:

The script will then start the event loop and begin listening for new events. When a new event is detected, the script will log the event data to the console.

Note:
Make sure you have an Ethereum node running locally or remotely or use infura node API, and that the contract address and ABI are correct.
