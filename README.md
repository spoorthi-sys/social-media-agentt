# Social Media Agent

This AI Social Media Content Agent automates the creation of captions, post ideas, and content calendars for any niche. It simplifies the content creation process and supports creators in maintaining consistent online engagement.

It helps creators, marketers, and businesses instantly generate high-quality captions, post ideas, and content calendars for platforms like Instagram, LinkedIn, and Twitter.

This project is designed to be simple, fast, and deployment-ready for platforms like Hugging Face Spaces.

---

## 🚀 Features
- AI-Generated Captions
- Post Ideas Generator
- Fast AI Responses

---

## Limitations

-Requires a valid OpenAI API key to run
-No image or video generation (text-only content)
-Cannot directly post to social media platforms
-Limited personalization (no brand voice memory)
-No analytics or performance tracking
-Basic UI due to Streamlit limitations

---


## 🛠 Tech Stack
- Programming Language :   Python
- Framework :   Streamlit,  OpenAI,  python-dotenv
- Tools Used :  GitHub,  Streamlit Cloud,  VS Code

---

## Setup & run instructions
   1. Clone the Repository
      git clone https://github.com/spoorthi-sys/social-media-agentt.git
   2. Create & Activate Virtual Environment
      python -m venv venv
      venv\Scripts\activate
   3. Install Dependencies
      pip install -r requirements.txt
   4. Add Your OpenAI API Key
      Create a .env file in the root folder:
      OPENAI_API_KEY=your_api_key_here
   5. Run the Streamlit App
      streamlit run app/streamlit_app.py
   6. Use the App
      Once the app starts, it will open automatically in your browser.
      You can generate:
         Captions
         Post ideas
         7-day content calendars
   7. Stop the Serve
      Press Ctrl + C

---

## Potential Improvements

   - Add templates for specific industries (fitness, fashion, tech, cooking, travel).
   - Improve UI/UX with multi-page navigation, dark mode, and better layout.
   - Add analytics such as best posting time, engagement prediction, etc.
   - Use a database (SQLite/Firebase) to store user history or previous content.
   - Add user authentication so users can save and revisit generated content.
   - Integrate with scheduling tools (like Buffer or Hootsuite API) to auto-post.

            









