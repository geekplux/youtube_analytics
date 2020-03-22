import json
import jieba.analyse
from wordcloud import WordCloud

json_file_path = './watch-history.json'

# with open('./stop_words.txt') as f:
#     stopWords = [line.strip() for line in f.readlines()]


def gen_img(texts, words_number):
  data = ' '.join(text for text in texts)
  wc = WordCloud(
      width=1000,
      height=500,
      background_color='white',
      max_words=words_number,
      font_path='/Library/Fonts/STHeiti Light.ttc'
  )
  wc.generate(data)
  wc.to_file('wordle.png')


def extract_words():
  words = []
  with open(json_file_path) as json_file:
    data = json.load(json_file)
    for history in data:
      if 'subtitles' not in history or 'titleUrl' not in history or not history['title'].startswith('Watched ') or not '2019' in history['time']:
        continue

      title = history['title'].replace('Watched ', '')

      for subtitle in history["subtitles"]:
        jieba.add_word(subtitle["name"])
        jieba.suggest_freq(subtitle["name"], True)

      jieba.add_word('小泽vlog')
      jieba.add_word('钟文泽')
      jieba.add_word('原来这么拍')
      jieba.add_word('原来这么毒')
      jieba.add_word('树根朽木')
      jieba.add_word('金庸')
      jieba.suggest_freq('金庸', True)
      jieba.add_word('评测')
      jieba.suggest_freq('评测', True)
      jieba.add_word('TVB')
      jieba.suggest_freq('TVB', True)
      jieba.add_word('倚天屠龍記')
      jieba.suggest_freq('倚天屠龍記', True)
      jieba.add_word('天龍八部')
      jieba.suggest_freq('天龍八部', True)
      jieba.add_word('射鵰英雄傳')
      jieba.suggest_freq('射鵰英雄傳', True)
      jieba.add_word('射鵰英雄傳')
      jieba.suggest_freq('射鵰英雄傳', True)
      jieba.add_word('神鵰俠侶')
      jieba.suggest_freq('神鵰俠侶', True)
      jieba.add_word('逝世')
      jieba.suggest_freq('逝世', True)
      jieba.add_word('顾俊')
      jieba.add_word('搞机零距离')
      jieba.add_word('笑傲江湖')
      jieba.suggest_freq('笑傲江湖', True)
      jieba.add_word('金婚')
      jieba.suggest_freq('金婚', True)
      jieba.add_word('都挺好')
      jieba.suggest_freq('都挺好', True)
      jieba.add_word('半路夫妻')
      jieba.suggest_freq('半路夫妻', True)
      jieba.add_word('粤语中字')
      jieba.suggest_freq('粤语中字', True)
      jieba.add_word('halfway couple')
      jieba.suggest_freq('halfway couple', True)
      jieba.add_word('主演')
      jieba.add_word('家庭')
      jieba.add_word('婚姻')
      jieba.suggest_freq(('金婚', '金婚'), True)
      jieba.suggest_freq(('家庭', '婚姻'), True)
      jieba.del_word('金庸逝世')
      jieba.analyse.set_stop_words('./stop_words.txt')
      tags = jieba.analyse.extract_tags(title)
      # tags = jieba.cut(title)
      # tags = [t for t in tags if t not in stopWords]
      # print(tags)
      words.extend(tags)
  return words

def analyze():
  words = extract_words()
  print('words count: ', len(words))
  gen_img(words, len(words))

analyze()