# Create package.json for npm compatibility
package_json = {
    "name": "mindcare-ai",
    "version": "1.0.0",
    "description": "Mental Health Assistant chatbot built with Botpress",
    "main": "index.html",
    "scripts": {
        "start": "python -m http.server 8000",
        "dev": "python -m http.server 8000",
        "deploy": "gh-pages -d ."
    },
    "keywords": [
        "mental-health",
        "chatbot",
        "botpress",
        "ai",
        "wellness",
        "healthcare"
    ],
    "author": "MindCare AI Team",
    "license": "MIT",
    "devDependencies": {
        "gh-pages": "^3.2.3"
    },
    "repository": {
        "type": "git",
        "url": "https://github.com/yourusername/mindcare-ai.git"
    },
    "homepage": "https://yourusername.github.io/mindcare-ai"
}

import json
with open('package.json', 'w') as f:
    json.dump(package_json, f, indent=2)

print("package.json created successfully!")

# Create .gitignore file
gitignore_content = """# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Logs
logs
*.log

# Build files
dist/
build/

# Temporary files
*.tmp
*.temp"""

with open('.gitignore', 'w') as f:
    f.write(gitignore_content)

print(".gitignore created successfully!")

# List all created files
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(f"\n📁 Repository structure created with {len(files)} files:")
for file in sorted(files):
    print(f"   ✅ {file}")