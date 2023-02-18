import json
import requests

def send_discord_notification(webhook_url, payload, username):
    issue_number = payload["pull_request"]["number"]
    author = payload["sender"]["login"]
    url = payload["pull_request"]["html_url"]
    message = f"{username} just merged pull request #{issue_number} on GitHub! {url}"
    
    data = {
        "content": message,
        "username": "GitHub"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    response.raise_for_status()

# Example usage
webhook_url = "https://discord.com/api/webhooks/1234567890/ABCDEFGHIJKL"
payload = {
    "sender": {
        "login": "johndoe"
    },
    "pull_request": {
        "number": 123,
        "html_url": "https://github.com/myorg/myrepo/pull/123"
    }
}
username = "Alice#1234"  # Replace with the Discord username of the user who triggered the webhook
send_discord_notification(webhook_url, payload, username)
