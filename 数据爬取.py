import requests
from lxml import etree
import time
import re
url = 'https://movie.douban.com/subject/30166972/comments?start=%d&limit=20&sort=new_score&status=P'
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           #'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Cookie': 'll="118213"; bid=09aB7w6_cpQ; __utmt=1; __utmt_t1=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1573038757%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; ap_v=0,6.0; __yadk_uid=v2AYCFE8ax65kSFDm11aYGGBHtoOAyeh; dbcl2="191195745:3SPt9njVLvA"; ck=8W89; _pk_id.100001.4cf6=799dd73eae98b249.1573038757.1.1573038869.1573038757.; _pk_ses.100001.4cf6=*; __utma=223695111.512686006.1573038757.1573038757.1573038757.1; __utmb=223695111.0.10.1573038757; __utmc=223695111; __utmz=223695111.1573038757.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.2023057902.1573038743.1573038743.1573038743.1; __utmb=30149280.24.8.1573038868913; __utmc=30149280; __utmz=30149280.1573038743.1.1.utmcsr=sogou.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; push_noty_num=0; push_doumail_num=0; RT=s=1573038889805&r=https%3A%2F%2Fmovie.douban.com%2Fsubject%2F30166972%2Fcomments%3Fstart%3D490%26amp%3Blimit%3D20%26amp%3Bsort%3Dnew_score%26amp%3Bstatus%3DP',
           'Host': 'movie.douban.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0', }
if __name__ == '__main__':
    fp=open('./sndn.csv',mode='w',encoding='utf-8')
    fp.write('author\tcomment\tvote\n')
    for i in range(26):
        if i==25:
            url_sndn=url%(490)#最后一页
        else:
            url_sndn=url%(i*20)
        response=requests.get(url_sndn,headers=headers)
        response.encoding='utf-8'
        text=response.text
        html=etree.HTML(text)
        comments=html.xpath('//div[@id="comments"]/div[@class="comment-item"]')
        for comment in comments:
            #作者
            author=comment.xpath('./div[@class="avatar"]/a/@title')[0].strip()
            #评论
            p=comment.xpath('.//span[@class="short"]/text()')[0].strip()
            #数据清理
            p = re.sub('[\s]','',p)
            #点赞
            vote = comment.xpath('.//span[@class="votes"]/text()')[0].strip()
            fp.write('%s\t%s\t%s\n'%(author,p,vote))
        print('成功爬取')
        time.sleep(1)
    fp.close()