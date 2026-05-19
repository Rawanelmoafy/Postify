from langchain.chat_models import init_chat_model
from helpers.config import get_settings   
from langchain_tavily import TavilySearch

settings = get_settings()

model = init_chat_model(settings.MODEL_NAME, api_key = settings.GOOGLE_API_KEY)

voice_headers = {"Authorization": f"Bearer {settings.HF_TOKEN}",
           "Content-Type": "audio/wav"}
voice_model = settings.VOICE_URL

tavily_tool = TavilySearch(tavily_api_key = settings.TAVILY_API_KEY, 
                                        max_results = 1)

