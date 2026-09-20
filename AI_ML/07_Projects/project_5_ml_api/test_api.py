"""
ML API Test Script
==================

Test all API endpoints to verify they work correctly.

Usage:
    1. Start the API:  uvicorn app:app --port 8000
    2. Run tests:      python test_api.py

Requirements:
    pip install requests
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000"


def test_root():
    """Test the root endpoint."""
    print("Testing GET / ...")
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "message" in data
    print(f"  ✅ Root: {data['message']}")
    return True


def test_health():
    """Test the health check endpoint."""
    print("Testing GET /health ...")
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "status" in data
    assert "model_loaded" in data
    print(f"  ✅ Health: status={data['status']}, model_loaded={data['model_loaded']}")
    return True


def test_predict():
    """Test the predict endpoint with valid input."""
    print("Testing POST /predict ...")
    payload = {
        "features": [8.3252, 41.0, 6.98, 1.02, 322.0, 2.56, 37.88, -122.23]
    }
    response = requests.post(
        f"{BASE_URL}/predict",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 503:
        print("  ⚠️  Model not loaded (expected if no model file exists)")
        return True
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "prediction" in data
    print(f"  ✅ Prediction: {data['prediction']}")
    return True


def test_predict_invalid():
    """Test the predict endpoint with invalid input."""
    print("Testing POST /predict (invalid input) ...")
    payload = {"features": []}
    response = requests.post(
        f"{BASE_URL}/predict",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code in (400, 422), f"Expected 400/422, got {response.status_code}"
    print(f"  ✅ Invalid input correctly rejected ({response.status_code})")
    return True


def test_predict_missing_body():
    """Test the predict endpoint with missing body."""
    print("Testing POST /predict (no body) ...")
    response = requests.post(f"{BASE_URL}/predict")
    assert response.status_code == 422, f"Expected 422, got {response.status_code}"
    print(f"  ✅ Missing body correctly rejected (422)")
    return True


def test_model_info():
    """Test the model info endpoint."""
    print("Testing GET /model/info ...")
    response = requests.get(f"{BASE_URL}/model/info")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "model_version" in data
    print(f"  ✅ Model info: version={data['model_version']}, type={data.get('model_type')}")
    return True


def test_docs():
    """Test that API docs are accessible."""
    print("Testing GET /docs ...")
    response = requests.get(f"{BASE_URL}/docs")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print(f"  ✅ Docs page accessible")
    return True


def run_all_tests():
    """Run all API tests."""
    print("=" * 50)
    print("ML API Test Suite")
    print(f"Target: {BASE_URL}")
    print("=" * 50)

    tests = [
        test_root,
        test_health,
        test_predict,
        test_predict_invalid,
        test_predict_missing_body,
        test_model_info,
        test_docs,
    ]

    passed = 0
    failed = 0

    for test_fn in tests:
        try:
            test_fn()
            passed += 1
        except requests.ConnectionError:
            print(f"\n❌ Cannot connect to {BASE_URL}")
            print("   Make sure the API is running: uvicorn app:app --port 8000")
            sys.exit(1)
        except AssertionError as e:
            print(f"  ❌ FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ❌ ERROR: {e}")
            failed += 1

    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed, {len(tests)} total")
    print("=" * 50)

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
