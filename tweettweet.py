import tweepy
import time

auth = tweepy.OAuthHandler('9o50S2t4LoaB4f54XJwYnTjKP', 'sSdoF2UB1ckwchpaNrOn8LhpaytQIYJZBulY9pqX5yISkqeRZy')
auth.set_access_token('3118672119-IkrwJGdzfEAWkXtuQIvKpGINHScqzNlntf0g0CO', 'N1RhdeiNJbeHW3CupWACCeBc1G9MSP0Sp5hTSmZ2GRtVI')

api = tweepy.API(auth)
user = api.me()

def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        return


#GenerousBot
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Mina Dobrasinovic':
        follower.follow()
    break


#Narcisstic Bot
search_string='python'
numberof_python=2

for tweet in tweepy.Cursor(api.search,search_string).items(numberof_python):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break