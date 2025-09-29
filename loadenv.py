from dotenv import load_dotenv
import os
import sys

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

load_dotenv(dotenv_path=".env")
load_dotenv(dotenv_path=".secret")

DB_PATH=os.getenv("DB_PATH")
EXECUTION_COLLECTION=os.getenv("EXECUTION_COLLECTION")
KEYWORD=os.getenv("KEYWORD")
MAX_RESULTS=os.getenv("MAX_RESULTS")

CVE_BASE_URL=os.getenv("CVE_BASE_URL")
HF_HUB_ENABLE_HF_TRANSFER=os.getenv("HF_HUB_ENABLE_HF_TRANSFER")
LAST_EXEC_LOG=os.getenv("LAST_EXEC_LOG")
EMBEDDING_ALG=os.getenv("EMBEDDING_ALG")

LOG_LEVEL=os.getenv("LOG_LEVEL")
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "./logs/AA_logs.log")
LOG_LEVEL = os.getenv("AA_LOG_LEVEL", "INFO")
LOG_MAX_BYTES=os.getenv("LOG_MAX_BYTES")
LOG_BACKUP_COUNT=os.getenv("LOG_BACKUP_COUNT")
IMAGE_LOG_DIR=os.getenv("IMAGE_LOG_DIR")

CVE_API_URL = os.getenv("CVE_API_URL")
CHATBOT_CONTEXT_FILE = os.getenv("CHATBOT_CONTEXT_FILE")

GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
HF_TOKEN=os.getenv("HF_TOKEN")

SYSTEM_PROMPT=os.getenv("SYSTEM_PROMPT")


GEMINI_MODEL=os.getenv("GEMINI_MODEL")
GEMINI_BASE_URL=os.getenv("GEMINI_BASE_URL")
OPENAI_MODEL=os.getenv("OPENAI_MODEL")

DEFAULT_LLM_PROVIDER=os.getenv("GEMINI_LLM_PROVIDER")
DEFAULT_LLM_MODEL=os.getenv("GEMINI_MODEL")

GEMINI_LLM_PROVIDER=os.getenv("GEMINI_LLM_PROVIDER")
OPENAI_LLM_PROVIDER=os.getenv("OPENAI_LLM_PROVIDER")

TEMPERATURE=os.getenv("TEMPERATURE")
TOP_P=os.getenv("TOP_P")
FREQUENCY_PENALTY=os.getenv("FREQUENCY_PENALTY")
PRESENCE_PENALTY=os.getenv("PRESENCE_PENALTY")
MAX_TOKENS=os.getenv("MAX_TOKENS")
