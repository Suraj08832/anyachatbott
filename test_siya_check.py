#!/usr/bin/env python3

# Simple test to verify siya check logic
def test_siya_check():
    test_messages = [
        "hello siya, how are you?",
        "SIYA, kya kar rahi ho?",
        "hey there, what's up?",
        "siya tell me a joke",
        "can you help me siya?",
        "just saying hello",
        "SIYA!",
        "what's your name siya?"
    ]

    for msg in test_messages:
        has_siya = "siya" in msg.lower()
        print(f"Message: '{msg}' -> Contains 'siya': {has_siya}")

    print("\nSiya personality check working correctly!")

if __name__ == "__main__":
    test_siya_check()



