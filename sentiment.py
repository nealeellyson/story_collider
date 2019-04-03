# Imports
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

# Fun examples included: raven.txt, hanselgretel.txt, icarus.txt
# Note: It seems that TextBlob does not like parsing through copy-pasted end quotes.
#       If you're getting UnicodeDecodeError, that could the problem.
filename = "transcripts/sc0-inspiration.txt";
transcript = TextBlob(open(filename).read())
polx = []; poly = []
subx = []; suby = []

# For every sentence in the selected source file, use TextBlob to evaluate
# the sentiment (consisting of polarity and subjectivity). Then store those
# values in two different arrays based on that.
for sentence in transcript.sentences:
    poly.append(sentence.sentiment.polarity)
    polx.append(len(poly))
    suby.append(sentence.sentiment.subjectivity)
    subx.append(len(suby))

# Time to graph! set up the plot with axes and labels
plt.title(filename);
plt.ylim(-1, 1)
plt.plot(moving_average(poly,n=10), linewidth = 1, label = "polarity")
#plt.plot(moving_average(suby,n=20), linewidth = 1, label = "subjectivity")
plt.xlabel("sentence #")
plt.legend()
plt.show()

# After you close the plot popup, extreme values of polarity and subjectivity
# will be printed out, along with their respective sentences.
print("Extreme Polarity:")
for index, val in enumerate(poly):
    if val > 0.9 or val < -0.9:
        print("[", index, ",", val ,"]", transcript.sentences[index])
        
print("\nExtreme Subjectivity:")
for index, val in enumerate(suby):
    if val > 0.9 or val < -0.9:
        print("[", index, ",", val ,"]", transcript.sentences[index])
