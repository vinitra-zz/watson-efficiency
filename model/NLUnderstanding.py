import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features
import transcriptManipulation

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="744c972f-3d84-4b71-8cf3-0eb57fedc072",
  password="3dhfEiyveG8P",
  version="2017-02-27")

with open(transcriptManipulation.script, 'r') as myfile:
    data = myfile.read()

strippedText = transcriptManipulation.stripPeoplePunc(data)

response = natural_language_understanding.analyze(
  text=strippedText,
  features=[
    Features.Keywords(
      limit=10
    ),
    Features.Entities(
      limit=10
    )
    
  ]
)

NLUJson = json.dumps(response, indent=2)
arrayData = json.loads(NLUJson)
keywords = [entry.get('text') for entry in arrayData.get('keywords')]

print("-------------------------------")
print("NLU Analysis Output - Keywords")
print("-------------------------------")
[print(word) for word in keywords]
print()

entityDict = dict([(entry.get('text'), entry.get('type')) for entry in arrayData.get('entities') if len(entry.get('text').split()) < 2])

print("-------------------------------")
print("NLU Analysis Output - Entities")
print("-------------------------------")
[print(entry + ", " + entryType) for entry, entryType in entityDict.items()]
print()

with open("output/NLUJson.txt", 'w') as jsonFile:
    json.dump(response, jsonFile, indent=2)

with open("output/NLUKeywords.txt", 'w') as wordFile:
    for word in keywords:
      wordFile.write(word + "\n")

with open("output/NLUEntities.txt", 'w') as entityFile:
    for entry, entryType in entityDict.items():
      entityFile.write(entry + ", " + entryType + "\n")

print("NLUJson written successfully!")
print("NLUKeywords written successfully!")
print("NLUEntities written successfully!")


