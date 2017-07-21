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

caller_text = transcriptManipulation.stripCallerText(data)

response = natural_language_understanding.analyze(
  text=caller_text,
  features=[
    Features.Entities(
      emotion=True,
      sentiment=True,
      limit=5
    ),
    Features.Keywords(
      emotion=True,
      sentiment=True,
      limit=5
    )
  ]
)

NLUJson = json.dumps(response, indent=2)


print("--------------------")
print("NLU Analysis Output")
print("--------------------\n")
print(NLUJson)

with open("output/NLUJson.txt", 'w') as json_file:
    json.dump(NLUJson, json_file)

print("NLUJson written successfully!")

