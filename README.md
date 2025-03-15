# VictorOps Alert Sender

This Python script sends a POST request to a Splunk On-Call endpoint. It is designed to simulate the integration with Splunk Observability and to send alerts for AWS EC2 instances. The script may be modified to customzie the content, monitoring tool, alert details, api key, routing key, etc to suit the needs of the demo.

## Features

- Sends POST requests to a specified VictorOps endpoint.
- Configurable via command-line arguments.
- Uses environment variables for sensitive information.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository** or download the script directly to your local machine.

2. **Install the required Python package** using pip:

    ```bash
    pip install requests
    ```

## Usage

### Set Environment Variables of required fields

Before running the script, set the `ONCALL_URL` environment variable with your target URL. This can be found in Splunk On-Call under Integrations then selecting an integration point -- the integration may need to be enabled by admin or alert admin if not enabled already. Routing keys are found under Settings > Routing Keys. In the command below, `API_KEY` and `ROUTING_KEY` must be replaced with your values (there is no default value)

```bash
export ONCALL_URL="https://alert.victorops.com/integrations/generic/20131114/alert/<API_KEY>/<ROUTING_KEY>"
```
Optionally, other fields may be set for consistent usage when running the script repeatedly. These fields _do_ have default values, and the script will work without assigning them yourself.

```bash
export ONCALL_TOOL="MY_MONITORING TOOL"
export ONCALL_ENTITY_ID="MY_ENTITY_ID"
```
