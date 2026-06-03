test_users = ["admin", "guest", "user1", ""]
test_passwords = ["Test@123", "wrong", "pass", ""]

def login_test(username, password):
    if username == "admin" and password == "Test@123":
        return "PASS"
    return "FAIL"

print("=== SDET Data-Driven Test Results ===")
for i in range(len(test_users)):
    user = test_users[i]
    pwd = test_passwords[i]
    result = login_test(user, pwd)
    print(f"Test {i+1}: User='{user}' Pass='{pwd}' -> {result}")
    
    if user == "admin" and pwd == "Test@123":
        assert result == "PASS"
    else:
        assert result == "FAIL"

print("Day 3 SDET: All data-driven tests passed!")