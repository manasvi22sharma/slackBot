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


#client.chat_postMessage(channel='slack-bot',text="Hello world 2!")
User_ID_BOT=client.api_call("auth.test")["user_id"]
message_count={}
# to message user directly use user id in channel
#client.chat_postMessage(channel='U02HASA6Z0C',text="hello")

#message
@slack_event_adapter.on('message')
def message(payLoad):
    event=payLoad.get('event',{})
    channel_id=event.get('channel')
    user_id=event.get('user')
    text=event.get('text')
    channel_type=event.get('channel_type')
    #print(channel_type)
    #message= text + "<@%s>! :tada:"%user_id
    #if user_id!=BOT_ID and channel_id=="D02H8M5P8CB":
        #client.chat_postMessage(**blocks.StartMessage)
    if user_id!=User_ID_BOT:
        #message on channel
        if channel_type!='im':
            client.chat_postMessage(channel=channel_id,text="let's take this over to DM")
        #message on DM
        #blocks.Welcome_Message_new["channel"]=user_id
        blocks.Welcome_Message_new["channel"]=channel_id
        blocks.Welcome_Message_new["blocks"][1]["text"]["text"]=f"Hello *<@{user_id}>*, this is Blubot :robot_face:"
        client.chat_postMessage(**blocks.Welcome_Message_new)
        #if user_id in message_count:
        #    message_count[user_id]+=1
        #else:
         #   message_count[user_id]=1 
            #block[channel]= channel_id   
        
#slash-cmd
@app.route('/message_count', methods=['POST'])
def messageCount():
    data=request.form
    user_id=data.get('user_id')
    channel_id=data.get('channel_id')
    count=message_count.get(user_id,0)
    client.chat_postMessage(channel=channel_id,text=f"message count is {count}")
    return Response(), 200

#action on message
@app.route('/actions', methods=['POST'])
def Useraction():
    print("here")
    data = request.form.to_dict()
    #print(data)
    payload= data.get('payload')
    payload_data = json.loads(payload)
    #print(type(payload_data))
    action = payload_data['actions']
    #print(action)
    channel_id=payload_data['channel']['id']
    print("channel"+ channel_id)
    #action_value=action[0]['value']#old
    action_value=action[0]['selected_option']['value']
    print(action_value)
    if action_value=='select_access':
        user_id=payload_data['user']['id']
        #print(user_id)
        blocks.Welcome_Message["channel"]=user_id
        #client.chat_postMessage(channel=user_id,text="clicked on A")
        client.chat_postMessage(**blocks.Welcome_Message)
    if action_value=='select_faq':
        user_id=payload_data['user']['id']
        #print(user_id)
        print("here")
        #remote file
        client.files_remote_add(external_id='001',external_url=os.environ['FILE_LINK'],title='test')
        client.files_remote_add(external_id='001',external_url=os.environ['FILE_LINK'],title='test')
        client.files_remote_share(channels=channel_id,external_id='001')
        #upload file from local
        #client.files_upload(channels=user_id,initial_comment="Here's the file you requested",file='test.txt')
    return Response(), 200

if __name__=="__main__":
    app.run(debug=True)