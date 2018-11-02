from django.http import HttpResponse
from django.shortcuts import render

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import(TextMessage, VoiceMessage, ImageMessage, 
       VideoMessage,LinkMessage, LocationMessage, EventMessage, ShortVideoMessage
       )

from . import wechatfun as wf 
from . import member_search as ms
conf = WechatConf(
       token='yinmahezhang',
       appid='wx3756b3cae577363e',
       appsecret='b4d787e3677cf6ee90bc291d89d7e195',
       encrypt_mode='normal'
       )

wechat_instance = WechatBasic(conf=conf) 

@csrf_exempt
def wechat_interface(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
    
        

        if not wechat_instance.check_signature(signature=signature, timestamp=timestamp,nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')

        return HttpResponse(request.GET.get('echostr', ''),content_type="text/plain")

    elif request.method == 'POST':
        try:                     
           
            wechat_instance.parse_data(data=request.body)
        except ParseError:
            return HttpResponseBadRequest('Invalid XML Data')

        message = wechat_instance.get_message()
        if isinstance(message, EventMessage):
            if message.type == 'subscribe':
                reply_text = '欢迎关注饮马河张氏公众号，了解家族历史，共同完善族谱信息。\n\n[友情提醒]\n在底部的信息框中输入问号，即可获取查询自己家谱数据的说明:)'
            elif message.type == 'click':
                reply_text = '自定义菜单点击'        
        elif isinstance(message, TextMessage):
            content = message.content.strip()
            if content == '?' or content == '？':
                reply_text ='''- 我要查询人员信息\n 在公众号底部的信息框中直接输入所需查找的人名即可。\n\n- 我要反馈信息\n 若发现信息有误，则可进行信息反馈。具体方式为，首先在信息框输入冒号(:)，然后在其后面输入需要反馈的内容即可，说清楚哪里有误，如何修正和补充。'''
            elif content[0:1] == ':' or content[0:1] == '：':
                if content[1:] == "":
                    reply_text = '您输入的反馈内容为空，请填写完整。'
                else:
                    reply_text = "您的反馈已收到，最迟24小时内会进行更新，请耐心等待。"
            else:
                keyword = content
                if len(keyword)>4:
                    reply_text = '请输入正确的人名进行查询。若需要反馈或留言，则需要在反馈的内容前输入冒号。'
                else:
                    reply_text = "您关于「"+ keyword + "」的查询结果已计算完毕，详情请点击：<a href='http://www.yinmahezhang.com/s_name?keyword="+keyword+"'>"+"查看"+"</a>"

        elif isinstance(message, ImageMessage):
            reply_text= 'image'
        else:
            reply_text= 'other'
        response = wechat_instance.response_text(content=reply_text)

    return HttpResponse(response, content_type="application/xml")


# Create your views here.
def search_by_keyword(request):
    keyword = request.GET.get('keyword','')
    search_results = ms.search_by_keyword(keyword)
    return HttpResponse(search_results)

# Create your views here.
def search_by_id(request):
    member_id= request.GET.get('mid','')
    print("member_id is ", member_id)
    search_result = ms.get_tree(member_id)
    return HttpResponse(search_result)
