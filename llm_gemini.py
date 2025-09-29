from openai import OpenAI
import os
from typing import Optional
import requests

from logger import get_logger
import loadenv as env

## Creating the factory to generate the LLM. 
# The client or service shall pass the relevant llm name to get the LLM client

# -------------------- Constants --------------------
logger = get_logger("LLM_Gemini")

DEFAULT_LLM_PARAMS = {
    "temperature": float(env.TEMPERATURE),
    "top_p": float(env.TOP_P),
    "frequency_penalty": float(env.FREQUENCY_PENALTY),
    "presence_penalty": float(env.PRESENCE_PENALTY),
    "max_tokens": int(env.MAX_TOKENS)
}

# -------------------- LLM_Gemini --------------------
class LLM_Gemini:
    def __init__(
        self,
        provider: str = env.GEMINI_LLM_PROVIDER,
        model: str = env.GEMINI_MODEL,
        llm_params: dict = None,
        session_id: Optional[str] = None
    ):
        self.provider = provider.lower()
        self.model = model
        self.llm_params = llm_params or DEFAULT_LLM_PARAMS
        self.session_id = session_id or "default-session"

        try:
            self.api_key = env.GEMINI_API_KEY
            if not self.api_key:
                raise EnvironmentError("GEMINI_API_KEY not set")
            logger.info(f"[{self.session_id}] ✅ Gemini client ready for model '{self.model}'")
        except Exception as e:
            logger.exception(f"[{self.session_id}] ❌ Initialization failed: {e}")
            raise RuntimeError("Gemini LLM setup failed. Please check your environment configuration.")

    def chat(self, prompt: str, system_prompt: str = env.SYSTEM_PROMPT, stream: bool = False):
        logger.info(f"[{self.session_id}] 🧠 Routing prompt to '{self.provider}' using model '{self.model}'")

        try:
            url = env.GEMINI_BASE_URL.format(model=self.model)
            headers = {
                "X-goog-api-key": f"{self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "contents": [
                    {
                        "parts": [
                            {"text": system_prompt + prompt}
                        ]
                    }
                ]
            }
            print(f"geminni key : {headers}")         
            print(f"geminni key : {payload}")         

            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

            # Extract response text
            reply = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            logger.info(f"[{self.session_id}] ✅ Gemini response received : {reply}")
            return reply or "⚠️ Gemini returned an empty response."

        except Exception as e:
            logger.error(f"[{self.session_id}] ❌ Gemini chat failed: {e}")
            return "⚠️ Sorry, I couldn’t process your request right now."
