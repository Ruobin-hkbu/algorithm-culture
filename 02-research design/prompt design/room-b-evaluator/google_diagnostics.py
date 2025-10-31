#!/usr/bin/env python3
"""
Google AI API Diagnostic Script
Tests different configurations to find the right setup
"""

import requests
import json
from config import API_KEY

def test_google_ai_simple():
    """Test Google AI with simplest possible request"""
    
    print("🔍 Testing Google AI API...")
    print(f"API Key: {API_KEY[:8]}...{API_KEY[-4:]}")
    
    # Try different model names and endpoints
    models_to_try = [
        "gemini-1.5-pro",
        "gemini-1.5-flash", 
        "gemini-pro",
        "gemini-1.0-pro"
    ]
    
    base_url = "https://generativelanguage.googleapis.com/v1beta/models"
    
    for model in models_to_try:
        print(f"\n📍 Testing model: {model}")
        
        url = f"{base_url}/{model}:generateContent?key={API_KEY}"
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        # Very simple test payload
        payload = {
            "contents": [{
                "parts": [{
                    "text": "Hello, please respond with just 'Hello back!'"
                }]
            }],
            "generationConfig": {
                "temperature": 0.1,
                "maxOutputTokens": 50
            }
        }
        
        try:
            print(f"   Making request to: {url}")
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            
            print(f"   Status Code: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"   ✅ SUCCESS! Model {model} works!")
                
                # Try to extract response
                if 'candidates' in result and result['candidates']:
                    candidate = result['candidates'][0]
                    if 'content' in candidate and 'parts' in candidate['content']:
                        text = candidate['content']['parts'][0]['text']
                        print(f"   Response: {text}")
                        return model, url  # Return working configuration
                
            else:
                error_info = response.text
                print(f"   ❌ Failed: {error_info}")
                
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    
    print("\n❌ None of the standard models worked")
    return None, None

def test_api_key_format():
    """Test if the API key format is correct for Google AI"""
    
    print(f"\n🔑 API Key Analysis:")
    print(f"   Length: {len(API_KEY)} characters")
    print(f"   Format: {API_KEY[:8]}...{API_KEY[-4:]}")
    
    # Google AI Studio API keys typically start with "AI" and are longer
    if API_KEY.startswith('AI'):
        print("   ✅ Format looks like Google AI Studio key")
    else:
        print("   ⚠️ Format doesn't match typical Google AI Studio key")
        print("   Google AI keys usually start with 'AI' and are ~40 characters")
        
def list_available_models():
    """Try to list available models"""
    
    print(f"\n📋 Attempting to list available models...")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
    
    try:
        response = requests.get(url, timeout=30)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Available models:")
            if 'models' in result:
                for model in result['models'][:5]:  # Show first 5
                    name = model.get('name', 'Unknown')
                    print(f"   - {name}")
            return result
        else:
            print(f"❌ Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    return None

def suggest_solutions():
    """Suggest possible solutions"""
    
    print(f"\n💡 TROUBLESHOOTING SUGGESTIONS:")
    print("="*50)
    
    print("1️⃣ Verify API Key Source:")
    print("   - Is this from Google AI Studio (https://aistudio.google.com/)?")
    print("   - Or from Google Cloud Console?")
    print("   - Keys should start with 'AI' for AI Studio")
    
    print("\n2️⃣ Check API Key Status:")
    print("   - Log into Google AI Studio")
    print("   - Verify the key is active and not expired")
    print("   - Check if you have remaining quota")
    
    print("\n3️⃣ Alternative Configuration:")
    print("   If using Google Cloud Vertex AI instead:")
    print("   - Endpoint: https://us-central1-aiplatform.googleapis.com/v1/projects/YOUR-PROJECT/locations/us-central1/publishers/google/models/MODEL:predict")
    print("   - Authentication: OAuth2 or Service Account")
    
    print("\n4️⃣ Test in AI Studio:")
    print("   - Go to https://aistudio.google.com/")
    print("   - Test your prompt there first")
    print("   - Verify the API key works in the interface")

def main():
    """Run all diagnostics"""
    
    print("🔧 Google AI API Diagnostics")
    print("="*50)
    
    # Test API key format
    test_api_key_format()
    
    # Try to list models first
    models_result = list_available_models()
    
    # Test simple API call
    working_model, working_url = test_google_ai_simple()
    
    if working_model:
        print(f"\n🎉 SUCCESS! Working configuration found:")
        print(f"   Model: {working_model}")
        print(f"   URL: {working_url}")
        
        # Update config file
        print(f"\n📝 Updating config.py with working model...")
        try:
            # Read current config
            with open('config.py', 'r') as f:
                content = f.read()
            
            # Update model name
            updated_content = content.replace(
                'MODEL_NAME = "gemini-1.5-pro"',
                f'MODEL_NAME = "{working_model}"'
            )
            
            # Write back
            with open('config.py', 'w') as f:
                f.write(updated_content)
                
            print("   ✅ Config updated!")
            
        except Exception as e:
            print(f"   ⚠️ Couldn't update config: {e}")
    else:
        suggest_solutions()

if __name__ == "__main__":
    main()