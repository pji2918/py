#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 9-6 위키피디아 워드 클라우드
#

import requests
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Komoran

komoran = Komoran()

wikipedia.set_lang("ko")
# 위키백과 사전의 컨텐츠 제목을 명시해 준다
wiki = wikipedia.page("트릭컬 리바이브")
# 이 페이지의 텍스트 컨텐츠를 추출하도록 한다
text = wiki.content

tokenized_txt = komoran.nouns(text)

stopword = str(
    requests.get(
        "https://gist.github.com/spikeekips/40eea22ef4a89f629abd87eed535ac6a/raw/4f7a635040442a995568270ac8156448f2d1f0cb/stopwords-ko.txt"
    ).content
).split()

clean_txt = ""

for idx, text in enumerate(tokenized_txt):
    if text == "트릭" and tokenized_txt[idx + 1] == "컬":
        clean_txt += "트릭컬 "
    elif text not in stopword and text.isalnum() and text != "컬":  # type: ignore
        clean_txt += f"{text} "  # type: ignore

wordcloud = WordCloud(
    width=2000, height=1500, font_path="PretendardJPVariable.ttf"
).generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
