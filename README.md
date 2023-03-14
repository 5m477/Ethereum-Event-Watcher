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
Install the web3.py, colorama, and pyfiglet libraries using pip:
pip install web3 colorama pyfiglet

Clone the repository and run the Event Subscriber script:
python event_subscriber.py


Note:
Make sure you have an Ethereum node running locally or remotely, and that the contract address and ABI are correct.
