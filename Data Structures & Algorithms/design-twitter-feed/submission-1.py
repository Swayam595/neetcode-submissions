class Twitter:
    # TC -> O(1)
    # SC -> O(N)
    def __init__(self):
        self.__user_dict = dict()
        self.__tweet_dict = dict()
        self.__time = 0
        
    # TC -> O(1)
    # SC -> O(1)
    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.__add_user_if_not_present(user_id)

        self.__tweet_dict[user_id].append([self.__time, tweet_id])
        self.__time += 1

        if len(self.__tweet_dict[user_id]) > 10:
            self.__tweet_dict[user_id].popleft()

    # TC -> O(N * log(10) + 10 * log(10)) ~ O(N)
    # SC -> O(1)
    def getNewsFeed(self, user_id: int) -> List[int]:
        feed = []

        for user_tweet in self.__tweet_dict[user_id]:
            feed.append(user_tweet)

        for following in self.__user_dict[user_id]:
            for tweet in self.__tweet_dict[following]:
                 heapq.heappush(feed, tweet)
                 if len(feed) > 10:
                    heapq.heappop(feed)
        
        feed_sorted = sorted(feed, key = lambda x: x[0], reverse = True)
        return [feed[1] for feed in feed_sorted]        

    # TC -> O(1)
    # SC -> O(1)
    def follow(self, follower_id: int, followee_id: int) -> None:
        self.__add_user_if_not_present(follower_id)
        self.__add_user_if_not_present(followee_id)

        self.__user_dict[follower_id].add(followee_id)
        
    # TC -> O(1)
    # SC -> O(1)
    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id not in self.__user_dict[follower_id]:
            return
            
        self.__user_dict[follower_id].remove(followee_id)
    
    # TC -> O(1)
    # SC -> O(1)
    def __add_user_if_not_present(self, user_id) -> None:
        if user_id not in self.__user_dict:
            self.__user_dict[user_id] = set()
            self.__tweet_dict[user_id] = deque()
    
        
