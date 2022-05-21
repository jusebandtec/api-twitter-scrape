from twitter_scraper import get_tweets
import pandas as pd

tweets = get_tweets("pix", pages = 5)
tweets_df = pd.DataFrame()
for tweet in tweets:
    print('Keys:', list(tweet.keys()), '\n')
    break

for tweet in tweets:
    _ = pd.DataFrame({'text' : [tweet['text']],
                    'isRetweet' : tweet['isRetweet'],
                    'replies' : tweet['replies'],
                    'retweets' : tweet['retweets'],
                    'likes' : tweet['likes']
                    })
    tweets_df = tweets_df.append(_, ignore_index = True)
tweets_df.head()