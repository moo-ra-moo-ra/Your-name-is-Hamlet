from konlpy.tag import Okt, Kkma
import hgtk
from collections import Counter

# 파일 불러오기
with open('D:\\test.txt') as f:
    lines = f.readlines()

# 모듈
okt = Okt()
kkm = Kkma()
# print(okt.pos(lines[1]))

# 변수 novel에 전체 문장 저장
novel = []
for line in lines:
    novel.append(line)
f.close()

# 각 문장별로 형태소 구분하기
sentences_tag = []
for sentence in novel:
    morph = okt.pos(sentence, norm=True, stem=True)
    sentences_tag.append(morph)

# print(sentences_tag)

# 형용사인 품사만 선별해서 리스트에 담기

adjs = []
for sentence in sentences_tag:
    for word, tag in sentence:
        if tag in ['Adjective'] and word not in ('있다', '아니다', '이다', '없다'):
            adjs.append(word)

# print(adjs)
adj_stems = []
for adj in adjs:
    a_stem = okt.morphs(adj)
    adj_stems.append(a_stem)

# print(adj_stems)
adj_stem_lists = []
for adj_stem in adj_stems:
    if len(adj_stem) == 1:
        adj_stem_lists += adj_stem

# print(adj_stem_lists)
adjs = []
for adj_stem_list in adj_stem_lists:
    adj_stem_a = adj_stem_list[0:-1]
    adjs.append(adj_stem_a)
# print(adjs)
result_adj = []
for adj in adjs:
    last = hgtk.letter.decompose(adj[-1])
    # print(type(last), last) #모듈 six 설치했음
    if last[2] == '':
        last = list(last)[0:2]
        last.append('ㄴ')
        last = hgtk.letter.compose(last[0], last[1], last[2])
        adj_r = adj[0:-1] + last
        result_adj.append(adj_r)
        # print(adj_r)
    elif last[2] == 'ㅎ':
        last = list(last)[0:2]
        last.append('ㄴ')
        last = hgtk.letter.compose(last[0], last[1], last[2])
        adj_r = adj[0:-1] + last
        result_adj.append(adj_r)

# result_adj = list(set(result_adj))

count_adj = Counter(result_adj).most_common(15)
final_adj = []
for i in count_adj:
    final_adj.append(i[0])
print(final_adj)

# 명사 뽑기
kkm_tag = []

# print(kkm.pos(novel[10]))

for sentence in novel:
    try:
        morph = kkm.pos(sentence)
        kkm_tag += morph
    except:
        pass
#          # print('error', sentence)
# print(kkm_tag)

nouns = []
# print(kkm_tag[4][1])
for i in kkm_tag:
    if i[1] == 'NNG':
        nouns.append(i[0])
    elif i[1] == 'NNP':
        nouns.append(i[0])

# print(Counter(nouns).most_common(60))
count_noun = Counter(nouns).most_common(60)
final_noun = []
for i in count_noun:
    final_noun.append(i[0])
print(final_noun)






