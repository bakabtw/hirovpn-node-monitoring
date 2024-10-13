# VPN Node Monitoring Script
This Python script monitors the server's resource usage (CPU, RAM, and disk space) and sends the metrics to a specified API endpoint at regular intervals. It utilizes the psutil library to retrieve system resource data and the requests library to send the data to an external API.

# Features
## Monitors:
- CPU usage (percentage)
- RAM usage (percentage)
- Disk usage at the root directory / (percentage)
- Sends the collected data as JSON to a specified API endpoint.
- Periodically checks and sends the metrics at an interval defined by the user (default is 60 seconds).
- Graceful error handling for API connectivity issues (e.g., HTTP errors, connection errors, timeouts).

# Requirements
- Python 3.x
- `psutil` and `requests` Python libraries
You can install the required libraries using pip:

```bash
pip install psutil requests
```

# Environment Variables
The script uses the following environment variables:

- `API_HOST`: The URL of the API endpoint to which the server metrics are sent.
- `PERIOD`: The time interval (in seconds) between sending the metrics (default is 60 seconds).
