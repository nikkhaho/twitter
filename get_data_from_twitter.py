import hazm_text
import datetime
import get_from_text
import tweepy


access_token ='839431366626394113-DZM6dI5Mey5HMMJY0eprtMuBnrwVmcs'
access_token_secret ='LGFUm7wpfpvXpHIZ3MlAexSmApw37jGPU9QvETCcEdiGh'
consumer_key ='hamp22ieArlw4OtT5Rzd9DVbD'
consumer_secret ='ElOfF30QxXN3Ry8DIkvvZVIRKw0xPUBzGNwp1dJS24j8KXHWAj'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweetCount = 50
language = "fa"

docs1=[]
docs2=[]
def gettwbyid(ide):
 if ide!="":
  results = api.user_timeline(id=ide, count=tweetCount,lang=language, since=datetime.date.today(), until=datetime.date.today())
  for tweet in results:
    if str(tweet.created_at)[:10] == str(datetime.date.today()):
     f=get_from_text.get_tag(tweet.text)
     g=get_from_text.get_id(tweet.text)
     hashtag=[]
     ids=[]
     for d in f:
         hashtag.append(d)
     for t in g:
         ids.append(t)
     timee=str(tweet.created_at)
     tw=hazm_text.normal(tweet.text)
     detectlang=hazm_text.detectlang(tw)
     if detectlang=="fa":
      doc = {
           'user':tweet.author.name,
           'tweet': tw,
           'hashtags':hashtag ,
           'ids': ids,
           'user_location': tweet.user.location,
           'time':timee,
           'userid':tweet.author.screen_name,
           'tweetid':tweet.id
                     }
      docs1.append(doc)
  return docs1
 else:
  return 0


def gettwbytag(tag):
 if tag!="":
  for tweet in api.search(q=(tag),language=language):
      f=get_from_text.get_tag(tweet.text)
      g=get_from_text.get_id(tweet.text)
      hashtag1=[]
      ids1=[]
      if str(tweet.created_at)[:10] == str(datetime.date.today()):
       for d in f:
          hashtag1.append(d)

       for t in g:
          ids1.append(t)
       timee=str(tweet.created_at)
       tw=hazm_text.normal(tweet.text)
       detectlang=hazm_text.detectlang(tw)
       if detectlang=="fa":
        doc2 = {
            'user':tweet.author.name,
            'tweet': tweet.text,
            'hashtags':hashtag1 ,
            'ids': ids1,
            'user_location': tweet.user.location,
            'time':timee,
            'userid':tweet.author.screen_name,
            'tweetid':tweet.id
                      }
        docs2.append(doc2)

  return docs2
 else:
  return 0

