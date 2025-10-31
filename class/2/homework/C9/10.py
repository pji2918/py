import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wiki = wikipedia.page("South Korea", auto_suggest=False)
txt = wiki.content

stopwords = STOPWORDS.union({"south", "north", "korean", "world", "country"})
wc = WordCloud(stopwords=stopwords).generate(txt)
plt.imshow(wc)
plt.axis("off")
plt.show()
