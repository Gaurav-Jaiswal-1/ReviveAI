import os
import groq

# Set your Groq API key (Store in .env for security)
GROQ_API_KEY = "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"

# Initialize Groq Client
client = groq.Groq(api_key=GROQ_API_KEY)

def get_response(user_input, category):
    prompt = f"Provide detailed {category} tips based on this query: {user_input}"

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Use "mixtral-8x7b-32768" for better accuracy
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,  # Adjusted for more complete answers
        temperature=0.7,  # Balanced creativity
        top_p=0.9  # Ensures diverse yet relevant responses
    )

    return response.choices[0].message.content.strip()  # Strip extra spaces

