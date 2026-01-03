# estimated_spread = average_audience_followers * ( num_followers ^ 1.2 )

# In the formula above, average_audience_followers is the average of the numbers in the audiences_followers list. This list contains the individual follower counts of the author's followers. For example, if audiences_followers = [2, 3, 2, 19], then:

# the author has 4 total followers
# each follower has their own 2, 3, 2, and 19 followers, respectively.
# Complete the get_estimated_spread function by implementing the formula above. The only input is audiences_followers, which is a list of the follower counts of all the followers the author has. Return the estimated spread. If the audiences_followers list is empty, return 0.

def get_estimated_spread(audiences_followers):
    if len(audiences_followers) == 0:
         return 0
    num_followers = len(audiences_followers)
    followers_sum = sum(audiences_followers)

    average_audiance_followers = followers_sum / num_followers
    return average_audiance_followers * (num_followers ** 1.2 ) 
   
