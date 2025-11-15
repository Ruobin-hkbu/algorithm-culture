# Room B Evaluator Configuration
# Copy this file to config.py and fill in your API details

# API Configuration
API_KEY = "your-openai-api-key-here"  # Set your OpenAI API key
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"  # OpenAI API endpoint
MODEL_NAME = "gpt-4"  # Model to use for evaluation (gpt-4 recommended for best results)

# Alternative API Configurations
# If using Azure OpenAI:
# API_ENDPOINT = "https://your-resource-name.openai.azure.com/openai/deployments/your-deployment-name/chat/completions?api-version=2024-02-15-preview"
# API_KEY = "your-azure-openai-key"

# If using other OpenAI-compatible APIs:
# API_ENDPOINT = "https://your-custom-endpoint.com/v1/chat/completions"
# API_KEY = "your-custom-api-key"

# Evaluation Settings
EVALUATION_TEMPERATURE = 0.1  # Low temperature for consistent evaluations
MAX_TOKENS = 2000  # Maximum tokens for evaluation response

# Scoring Thresholds
APPROVAL_THRESHOLD = 75  # Composite score threshold for APPROVE (out of 90)
REVISION_THRESHOLD = 60  # Composite score threshold for REVISE (out of 90)
# Below REVISION_THRESHOLD = REJECT

# Output Settings
DEFAULT_OUTPUT_DIR = "evaluation_results"  # Directory to save evaluation results
INCLUDE_FULL_RESPONSE = True  # Include full API response in results
AUTO_SAVE_RESULTS = True  # Automatically save results after evaluation