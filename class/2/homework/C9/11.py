import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

txt = (
    wikipedia.page("South Korea", auto_suggest=False).content
    + wikipedia.page("Japan", auto_suggest=False).content
)

stopwords = STOPWORDS.union({"south", "north", "korean", "world", "country"})
wc = WordCloud(stopwords=stopwords).generate(txt)
# wc.to_file("/Users/pji2918/Downloads/cloud.png")
plt.imshow(wc)
plt.axis("off")
plt.show()
