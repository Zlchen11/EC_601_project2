Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

import get_recent_tweet as grt
from google.cloud import language_v1
import os


s = grt.main()


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='ENTER THE PATH OF YOUR JSON FILE'
# Instantiates a client
client = language_v1.LanguageServiceClient()
# The text to analyze


filename = open('data.txt', 'w')

text = []
for i in range(7):
    tmp = []
    for j in range(10):
        tmp.append(s[j])
        s.pop(0)

    text.append(' '.join(tmp))

sentiment_score = []


for i in range(len(text)):
    document = language_v1.Document(
    content=text[i], type_=language_v1.Document.Type.PLAIN_TEXT
)
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    filename.write(text[i])
    filename.write('\n')
    filename.write(str(sentiment.score))
    filename.write(', ')
    filename.write(str(sentiment.magnitude))
    filename.write('\n')
    sentiment_score.append((sentiment.score, sentiment.magnitude))


    #print("Text: {}".format(text[i]))
    #print('\n')
    #print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
    #print('\n')
filename.close()




