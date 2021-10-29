from typing import Text
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask,request,Response
from slackeventsapi import SlackEventAdapter
import blocks
import json

env_path=Path('.')/ '.env'
load_dotenv(dotenv_path=env_path)
app=Flask(__name__)
slack_event_adapter =SlackEventAdapter(os.environ['SIGINIG_SECRET'],'/slack/events',app)
client =slack.WebClient(token=os.environ['SLACK_TOKEN'])

User_ID_BOT=client.api_call("auth.test")["user_id"]
users={}
#def actionsOfWelcomeMessage(action_value, user_id,payload):
    #blocks.access["channel"]=user_id
        #client.chat_postMessage(channel=user_id, text='Request Submitted')

#message
@slack_event_adapter.on('message')
def message(payLoad):
    event=payLoad.get('event',{})
    channel_id=event.get('channel')
    user_id=event.get('user')
    text=event.get('text')
    channel_type=event.get('channel_type')
    auth=payLoad.get('authorizations')
    bot_user_id=auth[0]['user_id']
    if user_id!=User_ID_BOT:
        #message on channel
        if channel_type!='im':
            client.chat_postMessage(channel=channel_id,text="let's take this over to DM")
        #message on DM
        blocks.Welcome_Message_new["channel"]=user_id
        #blocks.Welcome_Message_new["channel"]=channel_id
        blocks.Welcome_Message_new["blocks"][1]["text"]["text"]=f"Hello *<@{user_id}>*, this is Blubot :robot_face:"
        client.chat_postMessage(**blocks.Welcome_Message_new)
        
#slash-cmd
#@app.route('/message_count', methods=['POST'])
#def messageCount():
#    data=request.form
#    user_id=data.get('user_id')
#    channel_id=data.get('channel_id')
#    count=message_count.get(user_id,0)
#    client.chat_postMessage(channel=channel_id,text=f"message count is {count}")
#   return Response(), 200

#action on message
@app.route('/actions', methods=['POST'])
def Useraction():
    data = request.form.to_dict()
    payload= data.get('payload')
    payload_data = json.loads(payload)
    action = payload_data['actions']
    channel_id=payload_data['channel']['id']
    user_id=payload_data['user']['id']
    #action_value=action[0]['value']#old
    #print(payload)
    action_type=action[0]['type']
    action_id=action[0]['action_id']
    action_value='none'
    #print(action_value)
    if user_id not in users:
        users[user_id]={'selected_mis': None, 'selected_mis':None}
    #welcome_message
    if action_id=='welcomeMessage':
        action_value=action[0]['selected_option']['value']
        if action_value=='select_access':
                    # abums drop down 
            blocks.access["channel"]=user_id
            client.chat_postMessage(**blocks.access)
                    #message_id=2
        if action_value=='select_faq':
            blocks.faq["channel"]=user_id
            client.chat_postMessage(**blocks.faq)
                    # text box or message input from user and respond back 
                    #files code
                    #remote file
                    #client.files_remote_add(external_id='001',external_url=os.environ['FILE_LINK'],title='test')
                    #client.files_remote_add(external_id='001',external_url=os.environ['FILE_LINK'],title='test')
                    #client.files_remote_share(channels=channel_id,external_id='001')
                    #upload file from local
                    #client.files_upload(channels=user_id,initial_comment="Here's the file you requested",file='test.txt')
        if action_value=='select_query':
            blocks.query["channel"]=user_id
            client.chat_postMessage(**blocks.query)
        if action_value=='select_data_definition':#data definition view like set of drop down 1 mis 2 metrc and dimensions
            blocks.mis_message["channel"]=user_id
            client.chat_postMessage(**blocks.mis_message)
        # if action_vlaue==''select_engRequest:
        #else :
            #def actionsOfWelcomeMessage(action_value, user_id,payload)
            #if action_value=='click_acess_submit':
            #client.chat_postMessage(channel=user_id, text='Request Submitted')
     #access request
    if action_id=='access_submit':
        action_state=payload_data['state']['values']
        selected_album=action_state['access_album']['access_album_select']['selected_option']
        if selected_album==None:
            client.chat_postMessage(channel=user_id, text=f'Please select an album :x:')
        else: 
            selected_album_value=selected_album['value'] 
            selected_album_name=selected_album['text']['text']  
            selected_bj=action_state['access_bj']['access_bj']['value']
            if selected_bj==None:
                client.chat_postMessage(channel=user_id, text=f'Please add Business Justification for {selected_album_name} :x:') 
            else:   
                print(selected_bj)
                client.chat_postMessage(channel=user_id, text=f'Request Submitted for {selected_album_name} :white_check_mark:') 
    #faq request
    if action_id=='faq_submit':
        action_state=payload_data['state']['values']
        faq_question=action_state['faq_question']['faq_question']['value']
        if faq_question==None:
            client.chat_postMessage(channel=user_id, text=f':red_circle: Please add your question')
        else:
         client.chat_postMessage(channel=user_id, text=f':large_green_circle: you will be answered shortly')
    #query request
    if action_id=='query_submit':
        action_state=payload_data['state']['values']
        query_input=action_state['query_input']['select_query_input']['value']
        if query_input==None:
             client.chat_postMessage(channel=user_id, text=f':red_circle:Please add a query')
        else:
            client.chat_postMessage(channel=user_id, text=f':large_green_circle: Running Query....')
    #data definition request
    if action_id=='select_mis':
        selected_mis_value=action[0]['selected_option']['value']
        selected_mis_name=action[0]['selected_option']['text']['text']
        users[user_id]['selected_mis']=selected_mis_name
        #updating metric_message
        metrics=blocks.mis[selected_mis_value]
        for metric in metrics:
            option={"text": {"type": "plain_text","text": "","emoji": True},"value": ""}
            option['text']['text']=metric
            option['value']=metric
            blocks.metric_message['blocks'][2]['accessory']['options'].append(option)
        blocks.metric_message['blocks'][2]['text']['text']=f'Select a Metric/dimension for MIS:{selected_mis_name}'
        blocks.metric_message["channel"]=user_id
        print(blocks.metric_message)
        client.chat_postMessage(**blocks.metric_message)
        blocks.metric_message['blocks'][2]['accessory']['options']=[]
        blocks.metric_message['blocks'][2]['text']['text']=f'Select a Metric/dimension for MIS: NONE'
    if action_id=='select_metric':
        if users[user_id]['selected_mis']==None:
            client.chat_postMessage(channel=user_id, text=f':red_circle: MIS not selected')
            return
        selected_metric=action[0]['selected_option']['value']
        users[user_id]['selected_metric']=selected_metric
        selected_mis=users[user_id]['selected_mis']
        client.chat_postMessage(channel=user_id, text=f':large_green_circle: selected mis is {selected_mis} and selected metric is {selected_metric}')
        selected_mis=None

    return Response(), 200

if __name__=="__main__":
    #print("nere")
    app.run(debug=True)