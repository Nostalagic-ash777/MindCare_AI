// MindCare AI JavaScript Functions

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
window.MindCareAI = MindCareAI;
