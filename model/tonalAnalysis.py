import json
from watson_developer_cloud import ToneAnalyzerV3
import transcriptManipulation
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
import warnings
warnings.filterwarnings("ignore")

toneAnalyzer = ToneAnalyzerV3(
  version='2016-05-19',
  username="c96d2a10-470a-4d75-9b37-9885c8008fbb",
  password="kNNKuFCtV1gW"
)

with open(transcriptManipulation.script, 'r') as myfile:
    data = myfile.read()

caller_text = transcriptManipulation.stripCallerText(data)
response = toneAnalyzer.tone(text=caller_text)
toneJson = json.dumps(response, indent=2)

with open("output/EmotionJson.txt", 'w') as json_file:
    json.dump(response, json_file, indent=2)


arrayData = json.loads(toneJson)

emotional_range_scores = np.array([sentence.get('tone_categories')[2].get('tones')[4].get('score')  for sentence in arrayData.get('sentences_tone') if sentence.get('tone_categories') != []]) * 100 
anger_scores = np.array([sentence.get('tone_categories')[0].get('tones')[0].get('score')  for sentence in arrayData.get('sentences_tone') if sentence.get('tone_categories') != []]) * 100
fear_scores = np.array([sentence.get('tone_categories')[0].get('tones')[2].get('score')  for sentence in arrayData.get('sentences_tone') if sentence.get('tone_categories') != []]) * 100
sad_scores = np.array([sentence.get('tone_categories')[0].get('tones')[4].get('score')  for sentence in arrayData.get('sentences_tone') if sentence.get('tone_categories') != []]) * 100

emotional_output = "Emotional Range: {" + str(np.percentile(emotional_range_scores, 25)) + ", " + str(np.percentile(emotional_range_scores, 75)) + "}\n" \
					+ "Anger: " + str(max(anger_scores)) + "\n" \
			  		+ "Fear: " + str(max(fear_scores)) + "\n" \
			    	+ "Sadness: " + str(max(sad_scores))+ "\n\n"

print("-------------------------")
print("Emotional Analysis Output")
print("-------------------------\n")
print(emotional_output)


print("Displaying Sentiment Analysis Arcs...\n")

s = np.arange(len(emotional_range_scores))

plt.gca().set_color_cycle(['purple', 'red', 'orange', 'blue'])

plt.plot(s, emotional_range_scores, linewidth=3)
plt.plot(s, anger_scores, linestyle = '--')
plt.plot(s, fear_scores, linestyle = '--')
plt.plot(s, sad_scores, linestyle = '--')

plt.legend(['Emotion Intensity', 'Anger', 'Fear', 'Sadness'], loc='upper left')

plt.xlabel('Time')
plt.ylabel('Emotion Percentages')
plt.title('911 Caller Emotional Range')
plt.savefig("output/EmotionRange.png")
plt.show()

with open("output/EmotionOutput.txt", "w") as text_file:
    text_file.write(emotional_output)

print("EmotionJson written successfully!")
print("EmotionOutput.txt written successfully!")


