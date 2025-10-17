"""
Test script for the /api-endpoint POST endpoint.
This script sends a proper POST request with all required fields.
"""

import httpx
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Configuration
API_URL = "https://tds-project1-2-x3i4.onrender.com/api-endpoint"
USER_SECRET = os.getenv("USER_SECRET")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

# Test payload
payload = {
    "secret": USER_SECRET,
    "email": "test@example.com",
    "task": "test-app-001",
    "round": 1,
    "nonce": "test-nonce-12345",
    "brief": "Create a simple hello world web app",
    "checks": [
        "App displays 'Hello World'",
        "App is responsive"
    ],
    "attachments": [],  # Optional: add base64 encoded attachments if needed
    "evaluation_url": "http://localhost:8001/notify"  # Change to your evaluation server URL
}

print("=" * 60)
print("Testing /api-endpoint POST request")
print("=" * 60)
print(f"\n📍 Target URL: {API_URL}")
print(f"📦 Payload:\n{json.dumps(payload, indent=2)}\n")

try:
    # Send POST request
    response = httpx.post(API_URL, json=payload, timeout=30.0)
    
    print(f"✅ Response Status: {response.status_code}")
    print(f"📄 Response Body:\n{response.text}\n")
    
    if response.status_code == 200:
        print("✅ SUCCESS! Endpoint is working correctly.")
        print("The request has been accepted and is being processed in the background.")
    else:
        print(f"⚠️ Unexpected status code: {response.status_code}")
        
except httpx.ConnectError:
    print("❌ Connection Error: Could not connect to the API.")
    print(f"   Make sure the server is running at {API_URL}")
    print("   Run: uvicorn app.main:app --reload")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 60)
