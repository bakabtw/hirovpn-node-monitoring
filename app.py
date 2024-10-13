import time
import os

import psutil
import requests


API_HOST = os.environ.get('API_HOST', None)
PERIOD = os.environ.get('PERIOD', 60)


def check_server_load():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Check RAM usage
    ram = psutil.virtual_memory()
    ram_usage = ram.percent

    # Check Disk usage at /
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    return {
        "cpu": cpu_usage,
        "ram": ram_usage,
        "disk": disk_usage
    }
    

def send_metrics(data):
    try:
        # Sending data to API
        r = requests.post(API_HOST, json=data)
        r.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")

    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")

    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")


if __name__ == "__main__":
    if not API_HOST:
        print("API_HOST is not defined in ENV. Terminating...")
        exit()

    while True:
        data = check_server_load()

        send_metrics(data)
        print(data)

        time.sleep(PERIOD)
