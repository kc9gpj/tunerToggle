import pyhid_usb_relay
import time
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <sleep_duration>")
    sys.exit(1)

try:
    sleep_duration = float(sys.argv[1])
except ValueError:
    print("Error: Invalid sleep duration. Please provide a valid numeric value.")
    sys.exit(1)

relay = pyhid_usb_relay.find()
if relay is None:
    print("No USB relay found.")
    sys.exit(1)

print(relay)
print(relay.state)
print("Toggling relay")

relay.toggle_state(1)
time.sleep(sleep_duration)
relay.toggle_state(1)
print(relay.state)
