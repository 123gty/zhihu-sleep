#coding: utf-8
import re
import os
import time
import urllib.request
import threading
import json
import math
headers ={
	"cookie":'_zap=b41c9fd8-f245-4ee6-ac29-76cd12cdb05e; d_c0="AeBcPDAA_RKPTrAc99UbXgjo7YitT2Ht9Sc=|1618996237"; _ga=GA1.2.1890805944.1620293508; _xsrf=O99btZ65j89gZnBJxpHybRnZw7tmtGD0; __snaker__id=gZvCqNHqKjfgHq4p; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=LK31XfyEDXBABEABAEY%2F094B9Sy6oHTs; q_c1=b16cb556f93e458ea57b60e73177bce2|1640162195000|1640162195000; ariaDefaultTheme=undefined; YD00517437729195%3AWM_NI=mhC%2BRi25pYI5PvF2lsC38%2BeeN8FH%2FEsezMTsO2hpCAKGn5LLvE262thp9pgCLIxNsmgEC9U%2BEPeJiKYjy7DohDbtANcIxrPuNQl5oelDtE%2BFU91m5ZN3mgJHwz%2BX5U8gN1c%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea8c534bbacf9b3b37387928fb6d45f879b9faab57ba3b48687eb3a8e8ae1b8c82af0fea7c3b92aafb88dccd163f2ebc0bacc3f94aa8ad3ef7981edf8cce86f8ee88aa9ae4fb1bbb6aed7798deea891c24b8999a2d6cf48b69bfed7b180acb0f791e6499097b8aff267a59b8ddad8218790ababec419bb6b7d8c765ac9cae95c446a197b893d37f8e8fa4d6ee6fb09cbca6aa4e97e7ff8eb8528eeda388c944b5a6e5b9b85ffcb982d2e237e2a3; tst=r; gdxidpyhxdE=UeMhWHmVMit%5CCdf1g3e5r51xgkmz4wkXhptf0f%2FqcCKML%5ChibTl4ylNiVx3UNz6NxzKMIY%2F%2B4q%5CUaS5MvJTRxN5qKygy7Zrm%2F1LXZpbnz%2FvRzRsC0tvn5AQ1C3jAdBEXpMJmSUxY%5CWcsgU%2BeU4K%2Fq5%2BBQgq5Nep4M5DeMPOwfV49iV6T%3A1644479260517; captcha_session_v2="2|1:0|10:1644478577|18:captcha_session_v2|88:c2cxQTRtVVVwa0VjVzRzR2JSNFlUZkV4TG5NVjhmUXZZbUxOeGJId3VlYy9CSjI0dUlObXFtMmRQRmVJZHJERw==|2a6caf146bce063a5bbd6b1bb5b2d92e45bab63973ffeaa65f5b9c89b5e2f7bf"; captcha_ticket_v2="2|1:0|10:1644478614|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfNmxWUUtDWTdidzl5R1lGcGZYVUZ2X0dJUVVuZG5CSzBCQW5jc0IwSGdmLkxDNy5uaExreUJlUjFjNmlIZGU5cS5xbHZqZGFxakZNSk93R1FtTC1OLW1KSzQ3cm5MREt0NDdQWTkwRVE2ZzZ5N0RWREVMSExYOGdONk02eHQ1U0gyUGo4U01YdmtZcWNnTk9iZ2FaY0dlR0ZwUHFmd2F1NXpRRi1IZ1NoZHotTFNUdkVTRUhCTlROeFAwNjB5QnZ2SEZKbkw2OS5QR3B3SC5VSjgwY0tXcUQwRXdwazZmUkZ1U3JsaGc2cUU2dDVuVGJxVzAtcUE2eTlRWi1NTHNINHVManRKeVRNVGxldTVmcHQxUE1ZOXBYV3l5QW45djBKVDUyRWsxTVNYY0NQWXVzZHNDdDRTMUNGLkJ1WW1QN2xOU1BZUm5WbnI3VEtQc2x2akhYME1iNF9TMGNiazBvQV9mZmYwUV9RVUR1RERhSDJtRTgtT1UyRXo3b2RrVXVVSV9sT0JZa3Q4YlZpRVFkbk1Wa3hBNTFYZVpTemlvWnVPVC1UZVJjNTlDYS5CV2NwWWZXZ1FuNWx6V3JZc1lrcDFMVWtRcTJCSFMtNnRLR1RPU3ctd0tzVDdPVVpwVXdCcEZYemxBTGZQRHZCeU1VMmZYRUNVR1RFUU9pMyJ9|5bf3807433c211eea390a4dcc1dbbd1319b921ca9f536957c7e20b5ad8bdedab"; z_c0="2|1:0|10:1644478619|4:z_c0|92:Mi4xRXFCeENBQUFBQUFCNEZ3OE1BRDlFaVlBQUFCZ0FsVk5tZzd5WWdCem9qOVk3a3hVMUJTMXBic3RGYnBiZ2JqbWlB|a93aa35c74e4a55cd03cf4e3b44d74f5e50d5f89353c41ee74e795ebfb149883"; SESSIONID=VkTXw8l35OAGjWHUWUEilC7qWLmI6YbZbCQTHOmu5yP; JOID=W14UA0pwK0ePNfoZTHn8EboG8-NWKUcS1krNcn5NawHJXqVeHk7uQ-Qy8h9MKxnYw62Nqa3ECVnwAWD4cHk_cOA=; osd=V10WBU98KEWJMPYaTn_5HbkE9eZaKkUU00bOcHhIZwLLWKBSHUzoRugx8BlJJxraxaiBqq_CDFXzA2b9fHo9duU=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1643092081,1644459372,1644469967,1644479311; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1644479783; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1644480607|1644475546',
    "method":"Get"
	# "Referer": "https://www.doutula.com/photo/list/",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
url_list = []  #储存所有url
contentList = [] #存储所有出现的书籍
tongjicishu = {} #统计所有书籍出现的频率
totals = 0 #回答数量
glock = threading.Lock()

#生产者：请求url，获取所有书籍list
def get_pic_url():
    while True:
        glock.acquire()
        if len(url_list) == 0:
            glock.release()
            break
        else:
            page_url = url_list.pop()
            glock.release()
            res = urllib.request.Request(page_url,headers=headers)#请求
            res2 = urllib.request.urlopen(res).read().decode("utf-8")#获取html
            objContent = json.loads(res2)['data']#获取数据data
            ddd = re.compile(r'《.*?.》')#正则
            glock.acquire()
            for rel in objContent:
                result = ddd.findall(str(rel['content']))
                for gtygty in result:
                    if len(gtygty)<30:
                        contentList.append(gtygty) 
                    else:
                        zz = re.compile(r'>.*?.<')#正则
                        hrefcontent = zz.findall(gtygty)
                        data = str(hrefcontent).replace(">","《",1).replace("<","》",1)
                        contentList.append(data[2:-2]) 
            glock.release()
# 统计书籍出现的频率
def download_picture():
    ifStop=0
    submit = []
    while True:
        glock.acquire()
        if len(contentList) ==0:
            glock.release()
            ifStop +=1 
            if ifStop == 2:
                y2 = {k: v for k, v in sorted(tongjicishu.items(), key=lambda item: item[1], reverse=True)}
                for key in y2.keys():
                    submit.append("<p>"+ key+ ":推荐人数"+str(y2[key])+"人</p>")
                return ''.join(submit)	
                break
            else:
                continue
        else:
            url = contentList.pop()
            glock.release()
            #修改文件名
            if tongjicishu.__contains__(url) :
                tongjicishu[url]=tongjicishu[url]+1
            else :
                tongjicishu[url]=1
# 
def main():
    for idx in range(0,math.ceil(totals/5)):
        url = f"https://www.zhihu.com/api/v4/questions/29114634/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset={idx*5}&platform=desktop&sort_by=default"
        url_list.append(url)
    #创建十个线程作为生产者，请求
    for x in range(10):
        product = threading.Thread(target=get_pic_url)
        product.start()
    #创建一个线程作为消费者，统计
    for x in range(1):
        time.sleep(2)
        consumer = threading.Thread(target=download_picture)
        consumer.start()
def submitPut(putcontent):
    putUrl = "https://www.zhihu.com/api/v4/answers/2342429808?include=is_visible%2Cpaid_info%2Cpaid_info_content%2Cadmin_closed_comment%2Creward_info%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cattachment%2Crelationship.is_authorized%2Cvoting%2Cis_thanked%2Cis_author%2Cis_nothelp%2Cis_recognized%2Cis_labeled%3Bmark_infos%5B*%5D.url%3Bauthor.vip_info%2Cbadge%5B*%5D.topics%3Bsettings.table_of_content.enabled"
    data = {
           "content":putcontent,
           "reshipment_settings":"disallowed",
           "comment_permission":"all",
           "reward_setting":{"can_reward":False,"tagline":""},
           "disclaimer_status":"close",
           "disclaimer_type":"none",
           "commercial_report_info":{"is_report":False},
           "is_report":False,
           "push_activity":True,
           "table_of_contents_enabled":False,
           "thank_inviter_status":"close"
           }
    datascontent=json.dumps(data).encode('utf8')
    # data = urllib.parse.urlencode(formData).encode("utf-8")
    putres = urllib.request.Request(putUrl,data=datascontent,headers=headers,method='PUT')#请求
    putres2 = urllib.request.urlopen(putres).read().decode("utf-8")#获取html
if __name__ == '__main__':
    while True:
        totalsUrl = "https://www.zhihu.com/api/v4/questions/29114634/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=3&limit=5&sort_by=default&platform=desktop"
        res = urllib.request.Request(totalsUrl,headers=headers)#请求
        res2 = urllib.request.urlopen(res).read().decode("utf-8")#获取html
        totals = json.loads(res2)['paging']['totals']#获取数据data
        submitPut("<p>正在获取。。。</p>")#//提交空内容，防止重复
        print(totals,"__________")
        url_list = []
        contentList = []
        tongjicishu = {}
        main()
        putcontent = download_picture()
        submitPut("<p>本话题汇总,目前"+str(totals)+"回答</p>"+"<p>每天"+time.strftime('%H:%M:%S')+"更新</p>"+json.dumps(putcontent,ensure_ascii=False))
        
        time.sleep(10) #睡眠半个小时
