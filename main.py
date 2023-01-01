import cloudscraper
from discord_webhooks import DiscordWebhooks
import time
import json

webhook = DiscordWebhooks("WEBHOOK URL")
print("Starting up...")
def notify(amount):
    webhook.set_content(title="NEW RAIN STARTED!",description='Amount: '+str(amount),url="https://bloxflip.com",content="@everyone")
    webhook.send()

while True:
    try:
        scraper = cloudscraper.create_scraper(captcha={'provider': '2captcha','api_key': '2CAPTCHA_KEY'},interpreter='nodejs')
    except:
        print("Failed to get cloudflare tokens. Retrying...")
        continue
    last_created = None
    while True:
        try:
            data = scraper.get("https://api.bloxflip.com/chat/history").json()
        except:
            print("Failed to get cloudflare tokens. Retrying...")
            continue
        if data["rain"]["active"] == True and data["rain"]["created"] != last_created:
            print("[+] RAIN IS ACTIVE. Amount: " + str(data["rain"]["prize"]))
            last_created = data["rain"]["created"]
            notify(data["rain"]["prize"])

        elif not "created" in data["rain"] or data["rain"]["created"] != last_created:
            print("[-] No rain is active.")
        time.sleep(5)
