from typing import List
import tweepy
from dotenv import load_dotenv
import os
from collections import namedtuple


class Scrape:

    def __init__(self):
        load_dotenv()

    def initialize(self):
        bearer_token = os.getenv('BEARER_TOKEN')
        self.client = tweepy.Client(bearer_token = bearer_token)
        return self

    def get_id_user_by_usernames(self, users):
        users = self.client.get_users(usernames = users)
        return [{'id': user.id, 'name': user.name} for user in users.data]

    def get_tweets_from_words(self) -> List[namedtuple]:
        query = f'#pix lang:pt -is:retweet'
        tweets_tuple = []
        Tweet_namedtuple = namedtuple("Tweet", ["name", "tweet", "likes", "retweets", "criado_em", "source"])
        for response in tweepy.Paginator(
                self.client.search_recent_tweets,
                query=query,
                tweet_fields=['entities','context_annotations', 'created_at', 'public_metrics', 'source', 'geo', 'referenced_tweets'],
                max_results= 100,  
                place_fields = ['place_type', 'geo'],
                expansions=['author_id', 'geo.place_id', 'referenced_tweets.id.author_id', 'referenced_tweets.id']
            ):
            users = {user.id: user for user in response.includes["users"]}
            for tweet in response.data:
                if users[tweet.author_id]:
                    user = users[tweet.author_id]
                    tweets_tuple.append(Tweet_namedtuple(user.name, 
                                            tweet.text, 
                                            tweet.public_metrics['like_count'], 
                                            tweet.public_metrics['retweet_count'], 
                                            tweet.created_at.strftime('%d-%m-%Y %H:%M:%S'), 
                                            tweet.source
                                            )
                                        )

        return tweets_tuple
