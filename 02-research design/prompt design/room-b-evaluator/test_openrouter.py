#!/usr/bin/env python3
"""
Test if this is actually an OpenRouter API key
OpenRouter is a service that provides access to various AI models including OpenAI
"""

import requests
from config import API_KEY

def test_openrouter():
    """Test if the API key works with OpenRouter"""
    
    print("🔍 Testing OpenRouter API...")
    print(f"API Key: {API_KEY[:15]}...{API_KEY[-10:]}")
    
    # OpenRouter endpoint
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
        'HTTP-Referer': 'http://localhost:3000',  # Optional: for app identification
        'X-Title': 'Room B Evaluator'  # Optional: for app identification
    }
    
    # Test payload with a cheaper model
    payload = {
        'model': 'openai/gpt-3.5-turbo',  # OpenRouter format
        'messages': [
            {'role': 'user', 'content': 'Say "Hello from OpenRouter!"'}
        ],
        'max_tokens': 20,
        'temperature': 0.1
    }
    
    try:
        print(f"\n📡 Making request to OpenRouter...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            message = result['choices'][0]['message']['content']
            print(f"✅ SUCCESS! OpenRouter works!")
            print(f"Response: {message}")
            
            # Check usage info
            if 'usage' in result:
                usage = result['usage']
                print(f"📊 Token usage: {usage}")
            
            return True
            
        else:
            print(f"❌ Error Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Request Error: {str(e)}")
        return False

def list_openrouter_models():
    """List available models on OpenRouter"""
    
    print(f"\n📋 Getting available OpenRouter models...")
    
    url = "https://openrouter.ai/api/v1/models"
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            models = result.get('data', [])
            
            # Filter for OpenAI models
            openai_models = [m for m in models if 'openai' in m['id'] or 'gpt' in m['id']]
            
            print(f"✅ Found {len(openai_models)} OpenAI-compatible models:")
            for model in openai_models[:10]:  # Show first 10
                name = model['id']
                pricing = model.get('pricing', {})
                prompt_cost = pricing.get('prompt', 'N/A')
                print(f"   - {name} (${prompt_cost}/1M tokens)")
            
            return openai_models[0]['id'] if openai_models else None
            
        else:
            print(f"❌ Models list failed: {response.status_code}")
            print(response.text[:200])
            return None
            
    except Exception as e:
        print(f"❌ Models list error: {str(e)}")
        return None

def main():
    """Test OpenRouter"""
    
    print("🔄 OpenRouter API Test")
    print("="*50)
    
    # Test if this is an OpenRouter key
    if test_openrouter():
        print(f"\n🎉 SUCCESS! This is an OpenRouter API key!")
        
        # Get available models
        model = list_openrouter_models()
        
        if model:
            print(f"\n📝 Updating configuration for OpenRouter...")
            
            # Update config file for OpenRouter
            try:
                config_content = f'''# Room B Evaluator Configuration - OpenRouter
# OpenRouter provides access to multiple AI models including OpenAI

# API Configuration for OpenRouter
API_KEY = "{API_KEY}"
API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"  # OpenRouter endpoint
MODEL_NAME = "{model}"  # Available OpenAI model via OpenRouter
API_PROVIDER = "openrouter"  # Identifies this as OpenRouter configuration

# Evaluation Settings
EVALUATION_TEMPERATURE = 0.1
MAX_TOKENS = 2000

# Scoring Thresholds  
APPROVAL_THRESHOLD = 75
REVISION_THRESHOLD = 60

# Output Settings
DEFAULT_OUTPUT_DIR = "evaluation_results"
INCLUDE_FULL_RESPONSE = True
AUTO_SAVE_RESULTS = True
'''
                
                with open('config.py', 'w', encoding='utf-8') as f:
                    f.write(config_content)
                
                print("✅ Configuration updated for OpenRouter!")
                print(f"Now using model: {model}")
                print("\nYou can now run test_evaluator.py - it should work!")
                
            except Exception as e:
                print(f"❌ Config update error: {e}")
        
    else:
        print(f"\n❌ Not an OpenRouter key either")
        print("Please double-check where you got this API key from")

if __name__ == "__main__":
    main()