# agent/social_agent.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY is missing in your .env file")

# Initialize client
client = OpenAI(api_key=api_key)


# --------------------------------------------------------
# 🔥 Unified OpenAI call function (error-free)
# --------------------------------------------------------
def call_openai_system(prompt, model="gpt-4o-mini", max_tokens=300):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an AI assistant for social media content."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=0.7,
    )

    # ✅ CORRECT OUTPUT ACCESS (no message["content"]!)
    return response.choices[0].message.content.strip()


# --------------------------------------------------------
# 🔥 Generate Caption
# --------------------------------------------------------
def generate_caption(topic, tone):
    prompt = f"""
    Create a creative and engaging Instagram caption.

    Topic: {topic}
    Tone: {tone}

    Make it short, clean, and catchy.
    """

    return call_openai_system(prompt)


# --------------------------------------------------------
# 🔥 Generate Post Ideas
# --------------------------------------------------------
def generate_post_ideas(n, niche):
    prompt = f"""
    Generate {n} unique social media post ideas for the niche: {niche}.
    Write them as a numbered list.
    """

    return call_openai_system(prompt, max_tokens=400)


# --------------------------------------------------------
# 🔥 Generate 7-Day Content Calendar
# --------------------------------------------------------
def generate_calendar(niche):
    prompt = f"""
    Create a structured 7-day content calendar for the niche: {niche}.
    Include: post idea, caption theme, and call-to-action for each day.
    """

    return call_openai_system(prompt, max_tokens=500)
