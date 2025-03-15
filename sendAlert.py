import requests
import json
import argparse
import os

def load_payload_from_file(file_path):
    """Load JSON payload from a specified file."""
    try:
        with open(file_path, 'r') as file:
            payload = json.load(file)
        return payload
    except FileNotFoundError:
        print(f"File {file_path} not found. Using default payload values.")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in file {file_path}. Using default payload values.")
        return None

def main(args):
    # Retrieve the URL from the environment variable
    url = os.getenv('ONCALL_URL')
    if not url:
        raise ValueError("The environment variable 'ONCALL_URL' is not set.")

    # Attempt to load the payload from the file
    payload = load_payload_from_file('splunkcloud.json')

    # If the payload is not loaded from the file, use default values
    if payload is None:
        payload = {
            "ServiceNow_Integration": args.servicenow_integration,
            "monitoring_tool": args.monitoring_tool,
            "vo_annotate.i.Chart Showing Alert": args.chart_url,
            "timestamp": args.timestamp,
            "SFX_aws_instance_id": args.aws_instance_id,
            "entity_display_name": args.entity_display_name,
            "message_type": args.message_type,
            "rule": args.rule,
            "vo_annotate.u.Signal Alert": args.signal_alert,
            "detector": args.detector,
            "vo_annotate.u.Alert Details in SignalFx": args.alert_details_url,
            "entity_id": args.entity_id,
            "state_message": args.state_message,
            "vo_orig.ServiceNowField_victorops_close_notes": args.close_notes,
            "vo_annotate.u.SRE Dashboard": args.sre_dashboard_url
        }

    # Define the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Print the response
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send POST request to OnCall.')

    # Add arguments with default values
    parser.add_argument('--servicenow_integration', default='true', help='ServiceNow Integration flag.')
    parser.add_argument('--monitoring_tool', default='signalfx', help='The monitoring tool used.')
    parser.add_argument('--chart_url', default='https://example.com/chart', help='URL of the chart showing the alert.')
    parser.add_argument('--timestamp', default='2025-02-27T15:25:00Z', help='The timestamp of the alert.')
    parser.add_argument('--aws_instance_id', default='i-0fd21952ef5474ae5', help='The AWS instance ID.')
    parser.add_argument('--entity_display_name', default='AWS EC2: CPU utilization expected to reach the limit CH', help='The display name of the entity.')
    parser.add_argument('--message_type', default='CRITICAL', help='The type of the message.')
    parser.add_argument('--rule', default='AWS EC2: CPU utilization expected to reach the limit', help='The rule related to the alert.')
    parser.add_argument('--signal_alert', default='Critical', help='The signal alert level.')
    parser.add_argument('--detector', default='AWS EC2: CPU utilization expected to reach the limit', help='The detector name.')
    parser.add_argument('--alert_details_url', default='https://example.com/alert-details', help='URL with alert details in SignalFx.')
    parser.add_argument('--entity_id', default='AWS EC2: CPU utilization expected to reach the limit CH', help='The ID of the entity.')
    parser.add_argument('--state_message', default='Critical', help='The state message.')
    parser.add_argument('--close_notes', default='See Incident Activity', help='Notes for closing.')
    parser.add_argument('--sre_dashboard_url', default='https://example.com/sre-dashboard', help='URL to the SRE dashboard.')

    args = parser.parse_args()
    main(args)
