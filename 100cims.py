from wikidata.client import Client

client = Client()
entity = client.get("Q7838888", load=True)
print(entity.attributes)
