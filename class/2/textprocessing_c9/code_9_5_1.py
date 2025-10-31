#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.5 워드 클라우드
#

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud()
text = "Hello Hello Hello This is a word cloud example."

with open("class/2/test.txt", encoding="utf-8") as f:
    text = f.read()

wordcloud.generate(text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
