import datetime
from client import Client
import yaml

access_token = ""

with open("config.yaml", "r") as configuration_file:
    config = yaml.safe_load(configuration_file)

if config == None:
    raise ValueError("config.yaml is empty! Please fill in your credentials")

if "institution" in config and not config["institution"] == None:
    instituion = config["institution"]
else:
    raise ValueError("institution not defined")

current_year = datetime.date.today().year
current_week = datetime.date.today().isocalendar()[1]

client = Client(school=instituion)
usercode = client.get_user(token=access_token)["response"]["data"][0]["code"]
print(usercode)
print (client.get_liveschedule(token=access_token, week=str(current_year)+str(current_week), usercode=int(usercode)))