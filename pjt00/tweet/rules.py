import rules

@rules.predicate
def is_tweet_user(user, tweet):
    return tweet.user == user

rules.add_perm('tweet.can_tedit', is_tweet_user) 
