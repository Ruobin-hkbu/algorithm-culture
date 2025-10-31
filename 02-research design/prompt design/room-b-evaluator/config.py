# Room B Evaluator Configuration - OpenAI API
# API Configuration for OpenAI

# API Configuration for OpenAI
API_KEY = "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"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"  # OpenAI endpoint
MODEL_NAME = "gpt-3.5-turbo"  # Using gpt-3.5-turbo for better compatibility
API_PROVIDER = "openai"  # Identifies this as OpenAI configuration

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