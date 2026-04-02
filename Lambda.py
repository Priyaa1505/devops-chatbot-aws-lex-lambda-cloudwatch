def lambda_handler(event, context):
    print("Event received:", event)  # log input
    
    intent = event['sessionState']['intent']['name']
    print("Detected Intent:", intent)

    if intent == "CheckServerStatus":
        message = "✅ Server is running smoothly."
    
    elif intent == "DeployApplication":
        message = "🚀 Deployment started."
    
    elif intent == "RestartService":
        message = "🔄 Restarting service..."
    
    else:
        message = "❌ Unknown request"
    
    print("Response:", message)  # log output

    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": intent,
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": message
            }
        ]
    }
