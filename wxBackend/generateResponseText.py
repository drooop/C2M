#!/usr/bin/env python3
#!coding='utf-8'
# from tornado.ioloop import IOLoop
# from tornado.httpclient import HTTPClient
import json
import requests
import time

query_url = "http://c2m.tq.yhlcps.com/api/query"
video_url = "http://c2m.tq.yhlcps.com/statics/video/"


'''
@Description 与用户进行文本交互，用户输入【订单】返回订单列表，
             输入取件码返回订单详情，
             输入【通群】返回通群官网，
             输入其他内容返回提示字符串。

@param      {str}openid 用户的openid
            {str}msg    用户的发的字符串
            
@return     {str} res       :本次回复的字符串
'''


def producer(openid, msg):
    print(f"{openid}发送了{msg}\n\n返回：")
    response = query_his_order(openid)
    order_list = response['data']
    order_count = len(order_list)
    pickup_code_list = []
    goods_type_list = []
    status_list = []
    for each_order in order_list:
        pickup_code_list.append(each_order['pickup_code'])
        goods_type_list.append(each_order['goods_type'])
        status_list.append(each_order['status'])
   #print (pickup_code_list,goods_type_list,status_list)

    if msg == '订单':
        if order_count > 0:  # 查询到了
            res_2 = ''
            for i in range(order_count):
                try:
                    if goods_type_list[i] == "名片":
                        res_2 += (pickup_code_list[i]+'  |' +
                                  goods_type_list[i]+'  |'+status_list[i]+'|'+'\n')
                    else:
                        res_2 += (pickup_code_list[i]+'  |' +
                                  goods_type_list[i]+'|'+status_list[i]+'|'+'\n')
                except Exception as ex:
                    print(ex)
            res_1 = f"您一共有{order_count}个订单,回复取件码查看订单详情：\n取件码|类型  |状态\n"
            res = res_1+res_2
        else:
            res = '未查询到您的订单，请先下单吧^-^'

    elif msg in pickup_code_list:
        data = query_order(msg)['data']
        res_3 = "取件码："+msg+'\n'
        res_4 = '订单ID：'+data['order']['id']+'\n'
        res_5 = "商品类型："+data['order']['goods_type']+'\n'
        res_6 = '生产状态：'+data['order']['status']+'\n'
        res_7 = '创建时间：'+data['order']['create_time']+'\n'

        video_name= data['order']['video']
        if video_name == "null":
            res_8 = "视频链接：暂无生产视频\n"
        else :
            res_8 = "视频链接："+video_url+video_name+'\n'

        if data['order']['status'] == '待生产':
            wait_time = (int(msg)-int(data['last_pickup_code']))*1  # 大约1分钟一件
            res_9 = "预计等待："+str(wait_time)+'分钟'
        else :
            res_9=''

        res = res_3+res_4+res_5+res_6+res_7+res_8+res_9

    elif msg == '通群':
        res = '上海通群科技有限公司http://www.tongquntech.com/'

    elif msg == "tqcps神秘代码查询所有":
        all_pickup_code = query_all_pickup_code()["data"]
        unfinshed_str=""
        producting_str=""
        finshed_str=""
        for i in all_pickup_code["unfinshed_pickup_code"]:
            unfinshed_str+=i+"\n"
        for i in all_pickup_code["producting_pickup_code"]:
            producting_str+=i+"\n"
        for i in all_pickup_code["finshed_pickup_code"]:
            finshed_str+=i+"\n"
        res = "待生产:\n"+unfinshed_str+"生产中:\n"+producting_str+"已完成:\n"+finshed_str
    
    elif msg=="tqcps神秘代码删除所有":
        delete_all()
        res = "删除所有"
    else:
        res = "哈喽，我是云海流智能助手，很高兴为您服务！\n1.回复【订单】，查询您的所有订单\n2.回复【通群】，了解通群科技"

    return res

# 根据用户openid查询他的所有订单，返回json


def query_his_order(openid):
    # client = HTTPClient()
    url = query_url+"?user_openid="+openid
    # response = client.fetch(url, method='GET', request_timeout=10)
    res = requests.get(url)
    print('response all_order', res.text)
    # res = str(response.body, 'utf-8')
    res = json.loads(res.text)
    # client.close()
    return res

# 根据用户取件码查询订单详情，返回json


def query_order(pickup_code):
    # client = HTTPClient()
    url = query_url+"?pickup_code="+pickup_code
    # response = client.fetch(url, method='GET', request_timeout=10)
    res = requests.get(url)
    print('response order', res.text)
    # res = str(response.body, 'utf-8')
    res = json.loads(res.text)
    # client.close()
    return res

def qurey_video_url(pickup_code):
    url = query_url+"?video="+pickup_code
    res = requests.get(url)
    res = json.loads(res.text)
    print('response video_filename', res,type(res))
    return res 

def query_all_pickup_code():
    url= query_url+"?cmd=query_all"
    res = requests.get(url)
    res = json.loads(res.text)
    print('response all_pickup_code', res,type(res))
    return res 

def delete_all ():
    url=query_url+"?cmd=delete_all"
    res = requests.get(url)
    res = json.loads(res.text)
    print('response delete_all', res,type(res))
    return res
if __name__ == "__main__":
    a = producer("张杨", '订单')
    print(a)
