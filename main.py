import tweepy

# API key 설정
consumer_key = '#'
consumer_secret = '#'
access_token = '#'
access_token_secret = '#'

fIn = open('apiInfo.txt', 'r+')
while True:
	line = fIn.readline()
	if not line: break
	info = line.split("\t")
	consumer_key = info[0]
	consumer_secret = info[1]
	access_token = info[2]
	access_token_secret = info[3]
fIn.close()


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)