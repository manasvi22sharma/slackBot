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
							"text": "Check out the Bluelight Web Portal",
							"emoji": True
						},
						"value": "select_portal"
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
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "what would you like to do today ?",
				"emoji": True
			}
		}
	]
}