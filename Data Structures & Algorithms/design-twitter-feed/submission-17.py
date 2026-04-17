import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = list(self.tweets[userId])

        for followeeId in self.following[userId]:
            feed.extend(self.tweets[followeeId])

        heapq.heapify(feed)
        res = []

        while feed and len(res) < 10:
            count, tweetId = heapq.heappop(feed)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)