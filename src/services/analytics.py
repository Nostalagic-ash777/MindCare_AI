# Create the configuration JSON file
import json

config_content = {
    "botId": "mindcare-ai-bot",
    "botName": "MindCare AI",
    "hostUrl": "https://cdn.botpress.cloud/webchat/v3.2",
    "messagingUrl": "https://messaging.botpress.cloud",
    "clientId": "mindcare-client-id",
    "webhookId": "webhook-id-here",
    "lazySocket": True,
    "themeName": "prism",
    "frontendVersion": "v3.2",
    "showPoweredBy": False,
    "theme": "prism",
    "themeColor": "#2563eb",
    "composerPlaceholder": "Ask me about your mental health...",
    "botConversationDescription": "MindCare AI - Your Personal Mental Health Assistant"
}

# Save configuration to JSON file
with open('config.json', 'w') as f:
    json.dump(config_content, f, indent=2)

print("config.json file created successfully!")
