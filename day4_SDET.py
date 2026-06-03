test_cases = [
    {"id": 1, "user": "admin", "pass": "Test@123", "expected": "PASS", "type": "Valid Login"},
    {"id": 2, "user": "guest", "pass": "wrong", "expected": "FAIL", "type": "Invalid Pass"},
    {"id": 3, "user": "", "pass": "", "expected": "FAIL", "type": "Empty Fields"},
    {"id": 4, "user": "ADMIN", "pass": "Test@123", "expected": "FAIL", "type": "Case Sensitive"}
]

def run_login_test(case):
    actual = "PASS" if case["user"]=="admin" and case["pass"]=="Test@123" else "FAIL"
    assert actual == case["expected"], f"Test {case['id']} Failed: Expected {case['expected']}, got {actual}"
    print(f"Test {case['id']} [{case['type']}]: {actual}")

print("=== SDET Dictionary Test Suite ===")
for case in test_cases:
    run_login_test(case)

print("Day 4 SDET: All dictionary-based tests passed!")