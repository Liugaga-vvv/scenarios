# This function takes a list of votes as input and returns the winner
def calculate_winner(votes):
    # Initialize an empty dictionary to store the vote counts
    vote_count = {}

    # Iterate through each vote in the input list
    for vote in votes:
        # Convert the vote to lowercase to handle case-insensitive inputs
        vote = vote.lower()

        # Check if the vote already exists in the vote_count dictionary
        if vote in vote_count:
            # If it does, increment the vote count by 1
            vote_count[vote] += 1
        else:
            # If it doesn't, add the vote to the dictionary with a count of 1
            vote_count[vote] = 1

    # Find the maximum vote count from the dictionary values
    max_count = max(vote_count.values())

    # Get a list of all the candidates with the maximum vote count
    winner = [key for key, value in vote_count.items() if value == max_count]

    # If there is a tie between multiple candidates, return "Tie"
    if len(winner) > 1:
        return "Tie"
    # Otherwise, return the winner in title case
    else:
        return winner[0].capitalize()
