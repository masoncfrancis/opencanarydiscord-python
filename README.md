# OpenCanary Discord Connector

A server that accepts a message from OpenCanary, formats the data into a table, and sends it to a Discord webhook.

The [requirements.txt](requirements.txt) file is set up for it to be fun via gunicorn, but you can use whatever server you want. 

## Configuration

### OpenCanary Config

Your OpenCanary Config file must contain this JSON key-value pair under the `"handlers"` key:

```json
"Webhook": {
    "class": "opencanary.logger.WebhookHandler",
    "url": "your-discord-webhook-url"
    "method": "POST",
    "headers": {
                    "Content-Type": "application/json"
               }
    "data": {
                "content": "%(message)s"
            },
    "status_code": 200
}
```

### Environment Variables

You must set an environment variable `DISCORD_WEBHOOK_URL` as your Discord webhook url.
