import asyncio
from bleak import BleakScanner

async def scan_devices():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Found: {device.name} - {device.address}")
    print("Scan complete.\n")

async def main(scan_interval):
    while True:
        await scan_devices()
        print(f"Waiting for {scan_interval} seconds before the next scan...\n")
        await asyncio.sleep(scan_interval)

if __name__ == "__main__":
    # Set the scan interval (in seconds)
    import os
    scan_interval = int(os.getenv("BLE_SCAN_INTERVAL", 60))  # Default to 60 seconds
    asyncio.run(main(scan_interval))