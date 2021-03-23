# Film-hot-review-analysis
This is a film review analysis system
Python数据分析与挖掘
Python数据分析技术：numpy、pandas、matploylib、nltk、jieba、gensim等；
数据来源：可在网上阿里天池、kaggle自行收集或者自行通过爬虫或取；
运行环境：win7，win8，win10、linux等；
编译环境：Pycharm、Anaconda等

数据集的来源
来源于豆瓣网内网友们对《少年的你》电影的评论，通过python爬取得到，保存在文件sndn.csv，爬取网址如下：
https://movie.douban.com/subject/30166972/comments?start=0 &limit=20&sort=new_score&status=P

数据的介绍
由于这个电影最近热映，争议比较大，有人喜欢，也有人说它抄袭，然后我们根据爬取的数据，对它进行情感分析。

数据分析的目的
通过爬取的数据，然后对它进行分析，得出看完电影后的人对它的喜爱程度，主要是喜欢它是因为什么，不喜欢它又是因为什么，有哪些方面，去分析后，我们可以更直观看出原因。

实验的详细过程介绍-结合主要代码以及可视化结果进行说明
由于爬取到数据有部分没有意义和部分评论存在有回车，导致爬取出来形成多行，对此我们进行了数据的清理、数据的拼接、停用词的去除，再进行（0~1）情感分析，最后生产可视化最重要20个进行分析生成条形图，再绘制正向和负向词云。
