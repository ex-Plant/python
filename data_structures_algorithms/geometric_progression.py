# total = a1 × r^n
# Calculate the number of followers an influencer will have after a given number of months according to the influencer type:

# "fitness": follower count quadruples each month
# "cosmetic": follower count triples each month
# other: follower count doubles each month

def get_follower_prediction(follower_count, influencer_type, num_months):
    def multiply(val):
        return follower_count * val ** num_months 
    
    if influencer_type == "fitness":        
        return multiply(4)

    if influencer_type == "cosmetic":
        return multiply(3)
        
    return multiply(2)
    
