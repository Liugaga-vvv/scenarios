def calculate_winner(votes):
    vote_count = {}
    for vote in votes:
        vote = vote.lower()
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
    max_count = max(vote_count.values())
    winner = [key for key, value in vote_count.items() if value == max_count]
    if len(winner) > 1:
        return "Tie"
    else:
        return winner[0].capitalize()
