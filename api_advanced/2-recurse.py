import praw

def recurse(subreddit, hot_list=None, reddit=None, limit=25):
    if hot_list is None:
        hot_list = []
    
    if reddit is None:
        # Initialize the Reddit API connection using praw
        reddit = praw.Reddit(
            client_id='your_client_id',
            client_secret='your_client_secret',
            user_agent='your_user_agent',
        )
    
    try:
        # Fetch hot submissions for the given subreddit
        subreddit_obj = reddit.subreddit(subreddit)
        hot_submissions = subreddit_obj.hot(limit=limit)
        
        # Append titles of hot submissions to the hot_list
        for submission in hot_submissions:
            hot_list.append(submission.title)
        
        # Check if there are more pages to fetch (pagination)
        if len(hot_list) < limit:
            return hot_list
        else:
            # Recursive call to fetch next page
            return recurse(subreddit, hot_list, reddit, limit)
    
    except praw.exceptions.RedirectException:
        # Handle invalid subreddit which might redirect to search results
        return None
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == '__main__':
    subreddit = 'programming'
    result = recurse(subreddit)
    if result is not None:
        print(f"Number of hot articles in '{subreddit}': {len(result)}")
    else:
        print("None")

