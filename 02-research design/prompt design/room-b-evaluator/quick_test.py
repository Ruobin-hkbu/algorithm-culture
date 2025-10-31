#!/usr/bin/env python3
"""
Simple API Key Validation Test
"""

import requests
import json

# Your API key
API_KEY = "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"

def minimal_test():
    """Most basic API test possible"""
    
    print("🔥 MINIMAL API TEST")
    print("="*30)
    print(f"Key: {API_KEY[:12]}...{API_KEY[-8:]}")
    
    # Try the simplest possible request
    url = "https://api.openai.com/v1/models"
    headers = {'Authorization': f'Bearer {API_KEY}'}
    
    print("\n🔍 Testing models endpoint...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ API KEY WORKS!")
            data = response.json()
            models = [m['id'] for m in data.get('data', []) if 'gpt' in m['id']]
            print(f"Available models: {models[:3]}")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def chat_test():
    """Try a simple chat completion"""
    
    print("\n🤖 CHAT TEST")
    print("="*20)
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hi"}],
        "max_tokens": 5
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=15)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            message = result['choices'][0]['message']['content']
            print(f"✅ CHAT WORKS! Response: {message}")
            return True
        else:
            print(f"❌ Chat failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Chat error: {e}")
        return False

if __name__ == "__main__":
    
    print("🧪 QUICK API VALIDATION")
    print("="*40)
    
    # Test 1: Models
    if minimal_test():
        # Test 2: Chat if models work
        chat_test()
    
    print("\n" + "="*40)
    print("If both tests fail, the API key needs to be:")
    print("1. Regenerated at platform.openai.com")
    print("2. From the correct OpenAI account") 
    print("3. With active billing/credits")