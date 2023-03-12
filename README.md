# clickhouse-telegram-bot

A Telegram bot to get data from ClickHouse using plain English questions (based on GPT3)

## Configuration

### Creating a Telegram bot

Use https://t.me/BotFather to create a new bot. It will give you
the bot Telegram API (TELEGRAM_API_KEY).

### Getting Open AI Key

You can get your own Open AI key (OPENAI_API_KEY) at
https://platform.openai.com/account/api-keys

### Zappa configuration

Rename `zappa_settings.template.json` to `zappa_settings.json` and update the parameters like
`arn`, `s3_bucket`, `aws_region`.

### Bot configuration

1. Put Open AI key to OPENAI_API_KEY environment variable
2. Put Telegram API key to TELEGRAM_API_KEY environment variable
3. Put comma-separated list of Telegram usernames for people who's
   allowed to use the bot to ALLOWED_USERNAMES environment variable

## Running locally

0. Create virtualenv `virtualenv venv`, activate it `source venv/bin/activate`
   and install dependencies `pip install -r requirements.txt`
1. Setup ngrok: `ngrok http 5001`
2. Update .env file with the proper keys, urls, etc. (see Bot configuration section)
3. Run the app:

```
flask run --host=0.0.0.0 --port 5001
```

# Roadmap

[✅] Getting database structure

[✅] Generating prompt based on user question and then database structure

[✅] Sending the prompt to GPT3

[✅] Sending generated SQL to the clickhouse server

[ ] Use ChatGPT API instead of GPT3 API

[ ] Store chat history in a persistent storage in order to have a conversation

# Demo video

https://youtu.be/Qeh1RQ1dU2g
