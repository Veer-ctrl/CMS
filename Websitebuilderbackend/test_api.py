#!/usr/bin/env python3
<<<<<<< HEAD
"""
Simple API test script to verify all endpoints are working
"""
import requests
import json
import sys

BASE_URL = "http://localhost:8000/api"

def test_api_endpoints():
    print("🚀 Testing Corporate Portal API Endpoints...")
    print("=" * 50)
    
    # Test 1: Register a new user
    print("\n1. Testing User Registration...")
    register_data = {
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "phone": "1234567890",
        "password": "testpass123",
        "confirmPassword": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register/", json=register_data)
        if response.status_code == 201:
            print("✅ User registration successful!")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Registration failed: {response.status_code}")
            print(f"Error: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Django server. Please start the server first:")
        print("   cd backend/builderbackend && python manage.py runserver")
        return False
    except Exception as e:
        print(f"❌ Registration error: {e}")
        return False
    
    # Test 2: Verify OTP (bypassed)
    print("\n2. Testing OTP Verification...")
    otp_data = {
        "email": "test@example.com",
        "otp": "123456"  # Any 6-digit number should work
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/verify-otp/", json=otp_data)
        if response.status_code == 200:
            print("✅ OTP verification successful!")
            result = response.json()
            access_token = result['tokens']['access']
            print(f"Access token received: {access_token[:20]}...")
            
            # Test 3: Test authenticated endpoint
            print("\n3. Testing Authenticated Endpoint (Profile)...")
            headers = {"Authorization": f"Bearer {access_token}"}
            profile_response = requests.get(f"{BASE_URL}/auth/profile/", headers=headers)
            
            if profile_response.status_code == 200:
                print("✅ Profile endpoint working!")
                print(f"User data: {profile_response.json()}")
            else:
                print(f"❌ Profile endpoint failed: {profile_response.status_code}")
                
            # Test 4: Test website creation
            print("\n4. Testing Website Creation...")
            website_data = {
                "name": "Test Website",
                "slug": "test-website",
                "description": "A test website",
                "category": "business",
                "status": "published"
            }
            
            website_response = requests.post(f"{BASE_URL}/websites/", json=website_data, headers=headers)
            if website_response.status_code == 201:
                print("✅ Website creation successful!")
                website_id = website_response.json()['id']
                print(f"Website ID: {website_id}")
                
                # Test 5: Test public website access
                print("\n5. Testing Public Website Access...")
                public_response = requests.get(f"{BASE_URL}/websites/by_slug/?slug=test-website")
                if public_response.status_code == 200:
                    print("✅ Public website access working!")
                else:
                    print(f"❌ Public website access failed: {public_response.status_code}")
                    
            else:
                print(f"❌ Website creation failed: {website_response.status_code}")
                print(f"Error: {website_response.text}")
                
        else:
            print(f"❌ OTP verification failed: {response.status_code}")
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"❌ OTP verification error: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 API Testing Complete!")
    return True

if __name__ == "__main__":
    test_api_endpoints()
=======
import requests
import json

# Test the exact same data that would be sent from the frontend
test_data = {
    "firstName": "Test",
    "lastName": "User", 
    "email": "test@example.com",
    "phone": "1234567890",
    "password": "MyStr0ngP@ssw0rd!",
    "confirmPassword": "MyStr0ngP@ssw0rd!"
}

# Test both register and login
def test_register():
    print("=== Testing Register ===")
    url = "http://localhost:8000/api/auth/register/"
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=test_data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 400:
            try:
                error_data = response.json()
                print(f"Error Details: {json.dumps(error_data, indent=2)}")
            except:
                print("Could not parse error response as JSON")
        return response.status_code == 201
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_login():
    print("\n=== Testing Login ===")
    login_data = {
        "email": "test@example.com",
        "password": "MyStr0ngP@ssw0rd!"
    }
    
    url = "http://localhost:8000/api/auth/login/"
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=login_data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 400:
            try:
                error_data = response.json()
                print(f"Error Details: {json.dumps(error_data, indent=2)}")
            except:
                print("Could not parse error response as JSON")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Test register first
    register_success = test_register()
    
    # Only test login if register was successful
    if register_success:
        test_login()
    else:
        print("Skipping login test due to register failure")
>>>>>>> 4ecb2cfb1f796646c615829bf18d7126a71f8a35
