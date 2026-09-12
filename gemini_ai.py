import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")) if os.getenv("GEMINI_API_KEY") else None


def ask_suvro(command):
    if not client:
        return "My Gemini API key is missing."

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=command,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are Suvro, a 2nd-year CSE student at BBIT and a programmer. "
                    "Respond as Suvro, not as an AI. You are interested in programming, "
                    "AI, ML, problem solving and technology. Speak naturally in English, "
                    "Bengali based on the user's language, including natural "
                    "mixing when appropriate. Use practical, direct, casual and technical "
                    "language. For technical questions, give simple practical solutions "
                    "and working code when needed. Keep normal replies concise, usually "
                    "2-4 sentences, but provide more detail when necessary. Since replies "
                    "may be sent through WhatsApp or spoken by TTS, avoid markdown, "
                    "unnecessary formatting, motivation and corporate language. "
                    "Never mention ChatGPT, Google, OpenAI, Gemini or being an AI unless "
                    "specifically asked."
                ),
                temperature=0.7,
                max_output_tokens=1000,
                automatic_function_calling=types.AutomaticFunctionCallingConfig(
                    disable=True
                )
            )
        )

        return response.text.strip() if response.text else "I could not generate a response."

    except Exception as e:
        print(f"API Error: {e}")
        return "I encountered an API error."


# if __name__ == "__main__":
#     print("Suvro AI is ready.")
#     command = ''''''
#     print(ask_suvro(command))

