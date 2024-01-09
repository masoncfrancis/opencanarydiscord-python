from flask import Flask, request, jsonify
import os
import json
import argparse
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handler():
    # Get Discord webhook URL from environment variable
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        raise ValueError("Discord webhook URL not found in environment variables.")

    # Get JSON data from the incoming HTTP request
    try:
        input_data = request.get_json()
        json_message = input_data.get("content", "")
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    if not json_message:
        return jsonify({"error": "JSON message not found in the request"}), 400

    # Parse the JSON string to a dictionary
    input_json = json.loads(json_message)

    # Create Discord webhook request body
    discord_request_body = {
        "embeds": [
            {
                "title": "OpenCanary Alert",
                "color": 16777215,  # Color in decimal format (white)
                "fields": [
                    {"name": "Field", "value": "Value", "inline": True},
                    {"name": "dst_host", "value": input_json.get("dst_host", ""), "inline": True},
                    {"name": "dst_port", "value": str(input_json.get("dst_port", -1)), "inline": True},
                    {"name": "local_time", "value": input_json.get("local_time", ""), "inline": True},
                    {"name": "local_time_adjusted", "value": input_json.get("local_time_adjusted", ""), "inline": True},
                    {"name": "logdata", "value": input_json.get("logdata", {}).get("msg", {}).get("logdata", ""), "inline": True},
                    {"name": "logtype", "value": str(input_json.get("logtype", "")), "inline": True},
                    {"name": "node_id", "value": input_json.get("node_id", ""), "inline": True},
                    {"name": "src_host", "value": input_json.get("src_host", ""), "inline": True},
                    {"name": "src_port", "value": str(input_json.get("src_port", -1)), "inline": True},
                    {"name": "utc_time", "value": input_json.get("utc_time", ""), "inline": True}
                ]
            }
        ]
    }

    # Convert the dictionary to a JSON string
    discord_request_body_json = json.dumps(discord_request_body)

    # Make the HTTP POST request to the Discord webhook using the requests library
    response = requests.post(webhook_url, data=discord_request_body_json, headers={"Content-Type": "application/json"})

    # Log the response from the Discord API
    print(response.text)

    return jsonify({"statusCode": response.status_code, "body": response.text})

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 80)))