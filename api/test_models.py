from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

try:
    models = client.models.list()

    for model in models.data:
        print(model.id)

except Exception as e:
    print(e)