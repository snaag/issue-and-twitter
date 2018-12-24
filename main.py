from konlpy.tag import Twitter
import tweepy 

twitter = Twitter()
# 변수
max_count = 500

# tweet hash dict
dict_tweet_hash = dict() # {tweet:[favorite_count, retweet_count]}

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

# twitter api 생성
api = tweepy.API(auth, wait_on_rate_limit=True)

# keyword와 관련된 문장을 크롤링한다
keyword = '홍대입구'
count = 0
for tweet in tweepy.Cursor(api.search,
							q=keyword,
							result_type='recent',
							exclude_replies = True).items(max_count):
	if tweet.text in dict_tweet_hash:
		pass
	else:
		dict_tweet_hash[tweet.text] = [tweet.favorite_count, tweet.retweet_count]
		count+=1
		# print(str(count),"->",tweet.text," & like: ", tweet.retweet_count)

# dict_tweet_hash print
for key, value in dict_tweet_hash.items():
	print(key, value)



# work_각 tweet을 20글자까지만 보고, 각 텍스트를 숫자로 바꾼 다음 합을 구한 후 hash를 구하낟
# for_중복된 tweet들을 없앨려고
# def stringToHash(tweet):
# 	tweet_len = tweet.len()
# 	limit = 20
# 	if tweet_len<limit :

# 	else :


