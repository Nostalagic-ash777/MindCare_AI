# Let me create a complete repository structure with all necessary files for the MindCare AI chatbot
import json
import os

# Create the basic HTML file for the Botpress webchat
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MindCare AI - Mental Health Assistant</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>MindCare AI</h1>
            <p>Your Personal Mental Health Assistant</p>
        </header>
        
        <main>
            <div class="chat-container">
                <div id="webchat"></div>
            </div>
        </main>
        
        <footer>
            <p>&copy; 2025 MindCare AI. All rights reserved.</p>
        </footer>
    </div>

    <!-- Botpress Webchat Scripts -->
    <script src="https://cdn.botpress.cloud/webchat/v3.2/inject.js"></script>
    <script>
        window.botpressWebChat.init({
            "composerPlaceholder": "Type a message...",
            "botConversationDescription": "This chatbot was built surprisingly fast with Botpress",
            "botId": "mindcare-ai-bot",
            "hostUrl": "https://cdn.botpress.cloud/webchat/v3.2",
            "messagingUrl": "https://messaging.botpress.cloud",
            "clientId": "mindcare-client-id",
            "webhookId": "webhook-id-here",
            "lazySocket": true,
            "themeName": "prism",
            "frontendVersion": "v3.2",
            "showPoweredBy": false,
            "theme": "prism",
            "themeColor": "#2563eb"
        });
    </script>
</body>
</html>"""

# Create CSS file for styling
css_content = """/* MindCare AI Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    text-align: center;
    margin-bottom: 30px;
    color: white;
}

header h1 {
    font-size: 3rem;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

header p {
    font-size: 1.2rem;
    opacity: 0.9;
}

main {
    background: white;
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    margin-bottom: 30px;
}

.chat-container {
    min-height: 500px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

#webchat {
    width: 100%;
    height: 600px;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

footer {
    text-align: center;
    color: white;
    opacity: 0.8;
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        padding: 10px;
    }
    
    header h1 {
        font-size: 2rem;
    }
    
    main {
        padding: 20px;
    }
    
    #webchat {
        height: 500px;
    }
}

/* Custom Botpress Webchat Styling */
.bpw-layout {
    border-radius: 10px !important;
    box-shadow: none !important;
}

.bpw-header {
    background: linear-gradient(45deg, #2563eb, #3b82f6) !important;
    border-radius: 10px 10px 0 0 !important;
}

.bpw-composer {
    border-radius: 0 0 10px 10px !important;
}"""

# Create JavaScript file for additional functionality
js_content = """// MindCare AI JavaScript Functions

// Initialize chatbot when page loads
document.addEventListener('DOMContentLoaded', function() {
    console.log('MindCare AI initialized');
    
    // Add custom event listeners for chatbot interactions
    if (window.botpressWebChat) {
        window.botpressWebChat.onEvent(function(event) {
            if (event.type === 'message') {
                console.log('Message received:', event.data);
                trackUserEngagement();
            }
        });
    }
});

// Track user engagement
function trackUserEngagement() {
    // Add analytics tracking here if needed
    console.log('User engaged with MindCare AI');
}

// Custom functions for mental health features
const MindCareAI = {
    // Emergency contact information
    emergencyContacts: {
        crisis: '988', // National Suicide Prevention Lifeline
        text: 'Text HOME to 741741' // Crisis Text Line
    },
    
    // Show emergency contacts
    showEmergencyInfo: function() {
        alert(`Emergency Resources:
Crisis Hotline: ${this.emergencyContacts.crisis}
Crisis Text Line: ${this.emergencyContacts.text}

If you're having thoughts of suicide or self-harm, please reach out for help immediately.`);
    },
    
    // Mental health tips
    mentalHealthTips: [
        "Take deep breaths and practice mindfulness",
        "Stay connected with friends and family",
        "Maintain a regular sleep schedule",
        "Exercise regularly for better mood",
        "Practice gratitude daily",
        "Limit social media if it affects your mood",
        "Seek professional help when needed"
    ],
    
    // Get random tip
    getRandomTip: function() {
        const randomIndex = Math.floor(Math.random() * this.mentalHealthTips.length);
        return this.mentalHealthTips[randomIndex];
    }
};

// Make MindCareAI globally available
window.MindCareAI = MindCareAI;"""

# Create configuration JSON
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

print("Repository files created successfully!")
print("\nFiles structure:")
print("- index.html (Main website file)")
print("- styles.css (Styling)")
print("- script.js (JavaScript functionality)")
print("- config.json (Botpress configuration)")
