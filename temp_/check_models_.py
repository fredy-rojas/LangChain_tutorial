#%% Import libraries
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# openai.api_key = 'your-api-key'

# List available models
models = openai.models.list()

# Assuming 'models' is a SyncPage object
for model in models.data:  # Accessing the 'data' attribute directly
    print(model.id)  # Accessing properties of the 'Model' object


# %%
