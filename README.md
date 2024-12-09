# OpenCanary Discord Connector
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmasoncfrancis%2Fopencanary-discord-connector.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmasoncfrancis%2Fopencanary-discord-connector?ref=badge_shield)


A simple Flask server that accepts a message from OpenCanary, formats the data into a table, and sends it to a Discord webhook.

The [requirements.txt](requirements.txt) file is set up for it to be run via gunicorn, but you can use whatever server you want. 

## Configuration

### OpenCanary Config

Your OpenCanary config file must contain this JSON key-value pair under the `"handlers"` key:

```json
"Webhook": {
    "class": "opencanary.logger.WebhookHandler",
    "url": "url-to-this-connector"
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


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmasoncfrancis%2Fopencanary-discord-connector.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmasoncfrancis%2Fopencanary-discord-connector?ref=badge_large)