#!/usr/bin/env python3
"""
OpenAI API Test Script
Simple test to verify OpenAI API key works
"""

import requests
from config import API_KEY, MODEL_NAME

def test_openai_simple():
    """Test OpenAI API with simplest possible request"""
    
    print("🔍 Testing OpenAI API...")
    print(f"API Key: {API_KEY[:10]}...{API_KEY[-10:]}")
    print(f"Model: {MODEL_NAME}")
    
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    # Very simple test payload
    payload = {
        'model': MODEL_NAME,
        'messages': [
            {'role': 'user', 'content': 'Say "Hello, API test successful!"'}
        ],
        'max_tokens': 20,
        'temperature': 0.1
    }
    
    try:
        print(f"\n📡 Making request to OpenAI...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            message = result['choices'][0]['message']['content']
            print(f"✅ SUCCESS! Response: {message}")
            
            # Check usage info
            if 'usage' in result:
                usage = result['usage']
                print(f"📊 Token usage: {usage}")
            
            return True
            
        else:
            print(f"❌ Error Response: {response.text}")
            
            if response.status_code == 403:
                print("\n💡 403 Forbidden Error - Possible causes:")
                print("1. API key might be newly created and still activating")
                print("2. No credits/quota remaining on the account")
                print("3. API key might not have the right permissions")
                print("4. OpenAI account might need payment setup")
                
            elif response.status_code == 401:
                print("\n💡 401 Unauthorized - API key is invalid")
                
            elif response.status_code == 429:
                print("\n💡 429 Rate Limited - Too many requests")
                
            return False
            
    except Exception as e:
        print(f"❌ Request Error: {str(e)}")
        return False

def test_different_models():
    """Test with different, potentially cheaper models"""
    
    models_to_try = [
        "gpt-3.5-turbo",
        "gpt-4o-mini", 
        "gpt-4o",
        "gpt-4"
    ]
    
    print(f"\n🔄 Testing different models...")
    
    for model in models_to_try:
        print(f"\n📍 Testing {model}...")
        
        url = "https://api.openai.com/v1/chat/completions"
        
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': model,
            'messages': [{'role': 'user', 'content': 'Hi'}],
            'max_tokens': 5
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            
            if response.status_code == 200:
                print(f"   ✅ {model} works!")
                return model
            else:
                print(f"   ❌ {model} failed: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ {model} error: {str(e)}")
    
    return None

def check_account_status():
    """Try to check account status if possible"""
    
    print(f"\n💳 Checking account info...")
    
    # Try to get models list (this sometimes works even when chat doesn't)
    url = "https://api.openai.com/v1/models"
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            models = result.get('data', [])
            print(f"✅ Account active - {len(models)} models available")
            
            # Show some available models
            available_models = [m['id'] for m in models if 'gpt' in m['id']][:5]
            print(f"Available GPT models: {available_models}")
            
            return True
        else:
            print(f"❌ Account check failed: {response.status_code}")
            print(response.text[:200])
            return False
            
    except Exception as e:
        print(f"❌ Account check error: {str(e)}")
        return False

def main():
    """Run all tests"""
    
    print("🧪 OpenAI API Diagnostic Tests")
    print("="*50)
    
    # Test account status first
    account_ok = check_account_status()
    
    # Test simple API call
    if account_ok:
        api_works = test_openai_simple()
        
        if not api_works:
            # Try different models
            working_model = test_different_models()
            
            if working_model:
                print(f"\n🎉 Found working model: {working_model}")
                
                # Update config
                print("📝 Updating config with working model...")
                try:
                    with open('config.py', 'r') as f:
                        content = f.read()
                    
                    # Update model name
                    updated_content = content.replace(
                        f'MODEL_NAME = "{MODEL_NAME}"',
                        f'MODEL_NAME = "{working_model}"'
                    )
                    
                    with open('config.py', 'w') as f:
                        f.write(updated_content)
                        
                    print("✅ Config updated!")
                    
                except Exception as e:
                    print(f"⚠️ Couldn't update config: {e}")
            else:
                print("\n❌ No working models found")
        else:
            print(f"\n🎉 API is working perfectly!")
            print("You can now run test_evaluator.py successfully")
    
    else:
        print("\n🔧 TROUBLESHOOTING STEPS:")
        print("1. Check your OpenAI account at https://platform.openai.com/")
        print("2. Verify you have credits/payment method set up")
        print("3. Make sure API key has the right permissions")
        print("4. Try creating a new API key if this one doesn't work")

if __name__ == "__main__":
    main()