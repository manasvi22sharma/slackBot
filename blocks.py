Welcome_Message ={
    'ts': "",
    "channel": "",
    "username": "Welcome Robot!",
    "icon_emoji": "",
    "text":"",
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Welcome to Bluelight ",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hello *User*, this is Blubot :robot_face:"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "what would you like to do today ?"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Go to bluelight portal",
						"emoji": True
					},
					"value": "click_portal",
                    "url":"https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "B",
						"emoji": True
					},
					"value": "click_b",
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "A",
						"emoji": True
					},
					"value": "click_a",
				}
			]
		}
	]
}

Welcome_Message_new={
    'ts': "",
    "channel": "",
    "username": "Welcome Robot!",
    "icon_emoji": "",
    "text":"",
    "blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Welcome to Bluelight ",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hello *User*, this is Blubot :robot_face:"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Raise an access request",
							"emoji": True
						},
						"value": "select_access"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Run a query on some data",
							"emoji": True
						},
						"value": "select_query"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Submit an engagemnet request",
							"emoji": True
						},
						"value": "select_engRequest"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Data Definition",
							"emoji": True
						},
						"value": "select_data_definition"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "FAQs",
							"emoji": True
						},
						"value": "select_faq"
					}
				],
				"action_id": "welcomeMessage"
			},
			"label": {
				"type": "plain_text",
				"text": "what would you like to do today ?",
				"emoji": True
			}
		}
	]
}

query= {
	 'ts': "",
    "channel": "",
    "username": "Welcome Robot!",
    "icon_emoji": "",
    "text":"",
	"blocks": [
		{
			"block_id": "heading",
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "You have selected : Query on data",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"block_id": "query_input",
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "select_query_input"
			},
			"label": {
				"type": "plain_text",
				"text": "Enter your query below:",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Submit",
						"emoji": True
					},
					"value": "click_query_submit",
					"action_id": "query_submit"
				}
			]
		}
	]
	
}

access={
 	'ts': "",
    "channel": "",
    "username": "Welcome Robot!",
    "icon_emoji": "",
    "text":"",
	"blocks": [
		{	"block_id": "heading",
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "You have selected : Raise an access request ",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"block_id": "access_album",
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "album 1",
							"emoji": True
						},
						"value": "select_album1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "album 2",
							"emoji": True
						},
						"value": "select_album2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "album 3",
							"emoji": True
						},
						"value": "select_album3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "album 4",
							"emoji": True
						},
						"value": "select_album4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "album 5",
							"emoji": True
						},
						"value": "select_album5"
					}
				],
				"action_id": "access_album_select"
			},
			"label": {
				"type": "plain_text",
				"text": "Pick an album",
				"emoji": True
			}
		},
		{
			"block_id": "access_bj",
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "access_bj"
			},
			"label": {
				"type": "plain_text",
				"text": "Business Justification",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Submit",
						"emoji": True
					},
					"value": "click_acess_submit",
					"action_id": "access_submit"
				}
			]
		}
	]
}

faq={
	'ts': "",
    "channel": "",
    "username": "Welcome Robot!",
    "icon_emoji": "",
    "text":"",	
	"blocks": [
		{
			"block_id": "heading",
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "You have selected : FAQ ",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"block_id": "faq_question",
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "faq_question"
			},
			"label": {
				"type": "plain_text",
				"text": "Please wite your question below",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "submit",
						"emoji": True
					},
					"value": "click_faq",
					"action_id": "faq_submit"
				}
			]
		}
	]
}

data_definition={
	'ts': "",
    "channel": "",
    "username": "Welcome Robot!",
    "icon_emoji": "",
    "text":"",	
	"blocks": [
		{
			"block_id": "heading",
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "You have selected : Data definition ",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"block_id": "mis_selection",
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select a MIS"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "a",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "b",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "c",
							"emoji": True
						},
						"value": "value-2"
					}
				],
				"action_id": "action_mis"
			}
		},
		{
			"block_id": "dimension_selection",
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select metric or dimension"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "select a mis",
							"emoji": True
						},
						"value": "default"
					}
				],
				"action_id": "action_metric_dimension"
			}
		}
	]
}
mis_message={
	'ts': "",
    "channel": "",
    "username": "Welcome Robot!",
    "icon_emoji": "",
    "text":"",	
	"blocks": [
		{
			"block_id": "heading",
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "You have selected : Data definition ",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"block_id": "mis_selection",
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select a MIS"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "a",
							"emoji": True
						},
						"value": "select_a"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "b",
							"emoji": True
						},
						"value": "select_b"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "c",
							"emoji": True
						},
						"value": "select_c"
					}
				],
				"action_id": "select_mis"
			}
		}
	]
}
metric_message={
	'ts': "",
    "channel": "",
    "username": "Welcome Robot!",
    "icon_emoji": "",
    "text":"",	
    "blocks": [
		{
			"block_id": "heading",
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "You have selected : Data definition ",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"block_id": "metric_selection",
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select a Metric/dimension for MIS: NONE"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [],
				"action_id": "select_metric"
			}
		}
	]
}


mis={ # 'mis_name':['metric_ name1','metric_name2']
	'select_a':['1', '2','3'],
	'select_b':['q','w','a'],
	'select_c':['!','@','#']
}