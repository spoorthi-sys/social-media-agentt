# agent/prompts.py

caption_prompt = """
You are a professional social media content creator.

Write an Instagram caption on the topic: "{topic}"
Brand tone: {tone}

Rules:
- Start with a short hook (one sentence).
- Keep caption short (2-5 short lines).
- Include 3-5 relevant hashtags at the end.
- End with a clear CTA (one line).
- If topic includes product name, mention the product once.

Provide only the caption (no extra commentary).
"""

idea_prompt = """
You are a creative social media strategist.

Generate {n} unique content ideas for the niche: "{niche}".
Each idea should be:
- One short title (5–10 words)
- A 1-line description of the execution (how to make it a Reel/Post)

Output as a numbered list.
"""

calendar_prompt = """
You are a social media planner.

Create a 7-day content calendar for the niche: "{niche}".
For each day, provide:
- Day number (Day 1, Day 2, ...)
- Post idea (one line)
- Caption (2–3 short lines; include CTA)
- 4 hashtags
- Suggested posting time (e.g., "Mon 7 PM")

Output in a clean bullet format.
"""