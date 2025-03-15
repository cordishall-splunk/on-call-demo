import requests
import json
import argparse
import os

def main(args):
    # Retrieve the URL from the environment variable
    url = os.getenv('VICTOROPS_URL')
    if not url:
        raise ValueError("The environment variable 'VICTOROPS_URL' is not set.")

    # Define the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Define the payload
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

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Print the response
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send POST request to VictorOps.')

    # Add arguments
    parser.add_argument('--servicenow_integration', default='true', help='ServiceNow Integration flag.')
    parser.add_argument('--monitoring_tool', default='signalfx', help='The monitoring tool used.')
    parser.add_argument('--chart_url', required=True, help='URL of the chart showing the alert.')
    parser.add_argument('--timestamp', required=True, help='The timestamp of the alert.')
    parser.add_argument('--aws_instance_id', required=True, help='The AWS instance ID.')
    parser.add_argument('--entity_display_name', required=True, help='The display name of the entity.')
    parser.add_argument('--message_type', default='CRITICAL', help='The type of the message.')
    parser.add_argument('--rule', required=True, help='The rule related to the alert.')
    parser.add_argument('--signal_alert', default='Critical', help='The signal alert level.')
    parser.add_argument('--detector', required=True, help='The detector name.')
    parser.add_argument('--alert_details_url', required=True, help='URL with alert details in SignalFx.')
    parser.add_argument('--entity_id', required=True, help='The ID of the entity.')
    parser.add_argument('--state_message', default='Critical', help='The state message.')
    parser.add_argument('--close_notes', default='See Incident Activity', help='Notes for closing.')
    parser.add_argument('--sre_dashboard_url', required=True, help='URL to the SRE dashboard.')

    args = parser.parse_args()
    main(args)
