🧠 Real-Time AI Assistant with LiveKit
This project is a voice-enabled AI assistant that combines real-time communication, intelligent tools, and multilingual support to deliver smart, interactive experiences. It is designed to run inside a LiveKit room, where it can listen 🎧, speak 🗣️, search 🔍, and provide contextual replies in real time.

🚀 Key Features
• 	🌦 Weather Updates → Instantly fetches live weather information for any city.
• 	🔍 Web Search → Retrieves fresh results using DuckDuckGo.
• 	🗣️ Conversational AI → Powered by Google’s Realtime LLM for natural dialogue.
• 	🎙️ Voice Output → Responds with expressive voices for human-like interaction.
• 	🎛️ Noise Cancellation → Ensures clear audio even in busy environments.
• 	🌍 Multilingual Support → Extendable to Tamil, English, Hindi, and more.
• 	🔐 Secure Setup → Uses  for managing API keys safely.

📂 Project Structure
• 	requirements.txt → Lists dependencies.
• 	tools.py → Contains custom tools (weather + search).
• 	prompts.py → Defines agent instructions and conversation flow.
• 	main.py → Entry point that launches the assistant in a LiveKit session.
• 	README.md → Documentation for setup and usage.

🤖 How It Works
1. 	The assistant joins a LiveKit room with video/audio enabled.
2. 	It listens to user input and processes it using Google’s Realtime LLM.
3. 	When needed, it calls tools like weather 🌦 or search 🔍 to fetch external data.
4. 	Replies are generated with contextual instructions, ensuring natural and helpful responses.
5. 	Noise cancellation 🎛️ keeps communication clear and professional.

📦 Dependencies
• 	LiveKit Agents & Plugins (Google, OpenAI, Noise Cancellation)
• 	LangChain Community (DuckDuckGo search integration)
• 	Requests (API calls)
• 	Python-dotenv (environment variable management)
