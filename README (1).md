# MindCare AI - Mental Health Assistant

## 🧠 Overview

MindCare AI is an intelligent mental health assistant built with Botpress. It provides 24/7 support, mental health resources, and therapeutic conversations to help users maintain their psychological well-being.

## 🚀 Features

- **24/7 AI Support**: Always available mental health companion
- **Crisis Intervention**: Emergency contact information and resources
- **Mood Tracking**: Help users monitor their emotional state
- **Therapeutic Conversations**: Evidence-based mental health support
- **Resource Library**: Access to mental health tips and coping strategies
- **Privacy-First**: Secure and confidential conversations

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Chatbot Platform**: Botpress v3.2
- **Styling**: Custom CSS with responsive design
- **Hosting**: Compatible with GitHub Pages, Netlify, Vercel

## 📁 Project Structure

```
mindcare-ai/
├── index.html          # Main webpage
├── styles.css          # Styling and theme
├── script.js           # JavaScript functionality
├── config.json         # Botpress configuration
└── README.md          # This file
```

## 🎯 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mindcare-ai.git
   cd mindcare-ai
   ```

2. **Configure Botpress**
   - Update `config.json` with your Botpress credentials
   - Replace `clientId` and `webhookId` with your actual values
   - Customize bot responses in your Botpress dashboard

3. **Deploy**
   - **GitHub Pages**: Push to GitHub and enable Pages
   - **Netlify**: Drag and drop the folder to Netlify
   - **Vercel**: Connect your GitHub repository

## ⚙️ Configuration

### Botpress Setup

1. Create a Botpress account at [botpress.com](https://botpress.com)
2. Create a new bot and note down your:
   - Client ID
   - Webhook ID
   - Bot ID
3. Update `config.json` with your credentials
4. Customize the chatbot flows in Botpress Studio

### Customization

- **Theme Colors**: Modify `themeColor` in `config.json`
- **Styling**: Edit `styles.css` for custom appearance
- **Functionality**: Add features in `script.js`
- **Content**: Update placeholders and descriptions

## 🎨 Styling

The project uses a modern gradient design with:
- **Primary Colors**: Blue gradient (#667eea to #764ba2)
- **Typography**: Segoe UI font family
- **Layout**: Responsive design for all devices
- **Components**: Clean, accessible interface

## 🔧 Development

### Local Development

1. Open `index.html` in a web browser
2. Make changes to HTML, CSS, or JS files
3. Refresh browser to see updates
4. Test chatbot functionality

### Adding Features

- **Emergency Resources**: Extend `MindCareAI.emergencyContacts`
- **Mental Health Tips**: Add to `mentalHealthTips` array
- **Analytics**: Implement tracking in `trackUserEngagement()`
- **Custom Commands**: Add new functions to the MindCareAI object

## 🌐 Deployment Options

### GitHub Pages
```bash
# Push to main branch
git add .
git commit -m "Deploy MindCare AI"
git push origin main

# Enable Pages in repository settings
```

### Netlify
1. Drag project folder to Netlify deploy
2. Or connect GitHub repository for auto-deploy

### Vercel
```bash
npm i -g vercel
vercel --prod
```

## 📊 Features Roadmap

- [ ] User authentication
- [ ] Mood tracking analytics
- [ ] Integration with mental health APIs
- [ ] Multi-language support
- [ ] Voice interaction
- [ ] Mobile app version

## 🔒 Privacy & Security

- **Data Protection**: No personal data stored locally
- **HIPAA Compliance**: Follow healthcare data guidelines
- **Secure Communication**: All chats encrypted in transit
- **Crisis Protocol**: Automatic emergency resource provision

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Emergency Resources

- **Crisis Hotline**: 988 (National Suicide Prevention Lifeline)
- **Crisis Text Line**: Text HOME to 741741
- **Emergency**: Call 911 for immediate medical emergency

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Botpress for the amazing chatbot platform
- Mental health professionals for guidance
- Open source community for inspiration

## 📞 Support

For technical support or questions:
- Create an issue in this repository
- Email: support@mindcareai.com
- Documentation: [Visit our docs](https://mindcareai.com/docs)

---

**Disclaimer**: MindCare AI is not a replacement for professional mental health treatment. If you're experiencing a mental health crisis, please contact emergency services or a mental health professional immediately.