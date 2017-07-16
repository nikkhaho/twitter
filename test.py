from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import datetime
import twitter
import tweepy

access_token ='839431366626394113-DZM6dI5Mey5HMMJY0eprtMuBnrwVmcs'
access_token_secret ='LGFUm7wpfpvXpHIZ3MlAexSmApw37jGPU9QvETCcEdiGh'
consumer_key ='hamp22ieArlw4OtT5Rzd9DVbD'
consumer_secret ='ElOfF30QxXN3Ry8DIkvvZVIRKw0xPUBzGNwp1dJS24j8KXHWAj'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
name = "@payamsh6162"
language = "fa"
tweettext=[]
tweetname=[]
tweetid=[]
tweetcreat=[]
tweetlocation=[]
tweethashtag=[]

results = api.user_timeline(id=name,lang=language, since=datetime.date.today(), until=datetime.date.today())
for tweet in results:
     if str(tweet.created_at)[:10] == str(datetime.date.today()):
      tweettext.append(tweet.text)
      tweetcreat.append(tweet.created_at)
print(tweettext)
# print(tweettext)
print (tweetcreat)

    # tweetname.append(tweet.author.name)
    # print(tweetname)
    # tweetid.append(tweet.author.screen_name)
    # print (tweetid)


    #
    # tweetlocation.append(tweet.user.location)
    # print (tweetlocation)
    #
    # print ("///////////////////////////////////////////")
    #
