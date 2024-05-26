# Import the module
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'hadibagdadii')

# Retrieve the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]
print(followers)