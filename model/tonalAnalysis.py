import json
from watson_developer_cloud import ToneAnalyzerV3
import transcriptManipulation
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

toneAnalyzer = ToneAnalyzerV3(
  version='2016-05-19',
  username="c96d2a10-470a-4d75-9b37-9885c8008fbb",
  password="kNNKuFCtV1gW"
)

with open('transcription.txt', 'r') as myfile:
    data = myfile.read().replace('\u2019', '').replace('\u2026', '')

caller_text = transcriptManipulation.stripCallerText(data)
toneJson = json.dumps(toneAnalyzer.tone(text=caller_text), indent=2)

arrayData = json.loads(toneJson)

emotional_range_scores = np.array([sentence.get('tone_categories')[2].get('tones')[4].get('score')  for sentence in arrayData.get('sentences_tone') if sentence.get('tone_categories') != []]) * 100 
anger_scores = np.array([sentence.get('tone_categories')[0].get('tones')[0].get('score')  for sentence in arrayData.get('sentences_tone') if sentence.get('tone_categories') != []]) * 100
fear_scores = np.array([sentence.get('tone_categories')[0].get('tones')[2].get('score')  for sentence in arrayData.get('sentences_tone') if sentence.get('tone_categories') != []]) * 100
sad_scores = np.array([sentence.get('tone_categories')[0].get('tones')[4].get('score')  for sentence in arrayData.get('sentences_tone') if sentence.get('tone_categories') != []]) * 100
s = np.arange(len(emotional_range_scores))

plt.gca().set_color_cycle(['purple', 'red', 'orange', 'blue'])

plt.plot(s, emotional_range_scores)
plt.plot(s, anger_scores)
plt.plot(s, fear_scores)
plt.plot(s, sad_scores)

plt.legend(['Emotion Intensity', 'Anger', 'Fear', 'Sadness'], loc='upper left')

plt.xlabel('Time')
plt.ylabel('Emotion Percentages')
plt.title('911 Caller Emotional Range')
plt.savefig("emotionalrange.png")
plt.show()
