# VictorOps Alert Sender

This Python script sends a POST request to a VictorOps endpoint. It is designed to facilitate integration with monitoring tools like SignalFx and to send alerts for AWS EC2 instances. The script uses command-line arguments for most of its configuration, except for the URL, which is read from an environment variable for enhanced security.

## Features

- Sends POST requests to a specified VictorOps endpoint.
- Integrates with monitoring tools like SignalFx.
- Configurable via command-line arguments.
- Uses environment variables for sensitive information.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository** (if applicable) or download the script directly to your local machine.

2. **Install the required Python package** using pip:

    ```bash
    pip install requests
    ```

## Usage

### Set Environment Variable

Before running the script, set the `VICTOROPS_URL` environment variable with your target URL:

```bash
export VICTOROPS_URL="https://alert.victorops.com/integrations/generic/20131114/alert/YOUR-ENDPOINT"
