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

strippedText = transcriptManipulation.stripPeople(data)

response = natural_language_understanding.analyze(
  text=strippedText,
  features=[
    Features.Keywords(
      limit=9
    ),
    Features.Entities(
      limit=2
    )
    
  ]
)

NLUJson = json.dumps(response, indent=2)


print("--------------------")
print("NLU Analysis Output")
print("--------------------\n")
print(NLUJson)

with open("output/NLUJson.txt", 'w') as json_file:
    json.dump(response, json_file, indent=2)

print("NLUJson written successfully!")

