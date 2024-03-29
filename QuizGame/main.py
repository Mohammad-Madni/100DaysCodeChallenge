class User():
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0

profile = User("001", "Madni  Korejo")

print(profile.id + "\n" + profile.username )
print(profile.followers)
