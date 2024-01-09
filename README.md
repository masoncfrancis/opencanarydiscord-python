# OpenCanary Discord Formatter

A server that accepts a message from OpenCanary, formats the data into a table, and sends it to a Discord webhook. 

## OpenCanary Config

Your OpenCanary Config file must contain this JSON key and value pair under the `"handlers"` key:

```json
"Webhook": {
                "class": "opencanary.logger.WebhookHandler",
                "url": "your-discord-webhook-url"
                "method": "POST",
                "data": {
                            "content": "%(message)s"
                        },
                "status_code": 200
            }
```
