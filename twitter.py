import tweepy
import time


#authenticador do twitter#
auth = tweepy.OAuthHandler('nN6gfj68xdG6lt8KAVT3yLPdt','oVWvcf4mGgSng7uS1NzK7IkFNosornGV7EhFLTdnEoTNSEijnP')
auth.set_access_token('1372545170005184513-wptOvtcnODuT9BlWGWgJwZaarb4UB1','4O97ppmjOBmja1TAmeSsKLQvQDTpHSucLGYfQweRSAQVU')

#Create api#
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Anapolis','Anápolis'
numeroDeTweets = 1000




