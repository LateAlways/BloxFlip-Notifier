import cloudscraper
from discord_webhooks import DiscordWebhooks
import time
import json

webhook = DiscordWebhooks("https://discord.com/api/webhooks/1021579277482872922/V_MwA71Gl5dljQC_XdDDo35uOb1HW_dkgyHfJ5tgWnvZ6h4ioiRtIUgYBbUHxHbBTo6F")
print("Starting up...")
def notify(amount):
    webhook.set_content(title="NEW RAIN STARTED!",description='Amount: '+str(amount),url="https://bloxflip.com",content="@everyone")
    webhook.send()

while True:
    try:
        scraper = cloudscraper.create_scraper(captcha={'provider': '2captcha','api_key': 'a29e1eaa51c36cb63b6cf263deb01049'},interpreter='nodejs')
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
