friend = 1

def increase_friend():
    friend = 2
    print(f"Friend inside function:{friend}")

increase_friend()
print(f"friend outside function: {friend}")