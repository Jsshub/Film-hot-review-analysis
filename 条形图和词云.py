import pandas as pd
import jieba
from jieba import analyse
import matplotlib.pyplot as plt
import numpy as np
import wordcloud
from PIL import Image

if __name__=='__main__':
    data=pd.read_csv('./sndn.csv',sep='\t')
    comments =';'.join([str(c) for c in data['comment'].tolist()])
    # print(comments)


    gen =jieba.cut(comments)
    words =' '.join(gen)
    #对分好次，进行jieba分析
    tags =analyse.extract_tags(words,topK=500,withWeight=True)
    # print(tags)
    word_result = pd.DataFrame(tags,columns=['词语','重要性'])
    # print(word_result)
    word_result.sort_values(by='重要性',ascending=False,inplace=True)#从大到小

    # 可视化,500个词语，选取其中最重要20个进行分析
    plt.barh(y=np.arange(0, 20), width=word_result[:20]['重要性'][::-1])
    plt.ylabel('Importance')
    plt.yticks(np.arange(0, 20), labels=word_result[:20]['词语'][::-1],fontproperties='KaiTi')
    # 保存条形图
    plt.savefig('./条形图.jpg', dpi=200)
    plt.show()

    # 正向词云图片
    data_pos = pd.read_csv('./sndn_pos.csv', sep='\t')
    comments_pos = ';'.join([str(c) for c in data_pos['comment'].tolist()])

    gen_pos = jieba.cut(comments_pos)
    words_pos = ' '.join(gen_pos)
    # 对分好次，进行jieba分析
    tags_pos = analyse.extract_tags(words_pos, topK=500, withWeight=True)
    SNDN = np.array(Image.open('./少年的你.png'))
    # 讲tags。jieba分词提取出来数据，dict字典

    words_pos = dict(tags_pos)
    cloud_pos = wordcloud.WordCloud(width=1200, height=968, font_path='./simkai.ttf', background_color='white',
                                    mask=SNDN, max_words=500, max_font_size=150)
    # 词云
    word_cloud = cloud_pos.generate_from_frequencies(words_pos)
    plt.figure(figsize=(12, 12))
    plt.imshow(word_cloud)
    # 词云保存
    plt.savefig('.少年的你_正向词云.jpg', dpi=200)
    plt.show()

# 负向词云图片
    data_neg=pd.read_csv('./sndn_neg.csv',sep='\t')
    comments_neg =';'.join([str(c) for c in data_neg['comment'].tolist()])

    gen_neg =jieba.cut(comments_neg)
    words_neg =' '.join(gen_neg)
    #对分好次，进行jieba分析
    tags_neg =analyse.extract_tags(words_neg,topK=500,withWeight=True)
    SNDN = np.array(Image.open('./少年的你.png'))
    # 讲tags。jieba分词提取出来数据，dict字典

    words_neg = dict(tags_neg)
    cloud_neg = wordcloud.WordCloud(width=1200, height=968, font_path='./simkai.ttf', background_color='black',
                                mask=SNDN, max_words=500, max_font_size=150)
    # 词云
    word_cloud = cloud_neg.generate_from_frequencies(words_neg)
    plt.figure(figsize=(12, 12))
    plt.imshow(word_cloud)
    # 词云保存
    plt.savefig('.少年的你_负向词云.jpg', dpi=200)
    plt.show()
