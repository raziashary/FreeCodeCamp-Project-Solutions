def player(prev_play, opponent_history=[], play_order=[]):
    if not prev_play:
        opponent_history.clear()
        play_order.clear()
    
    opponent_history.append(prev_play)

    # Look for patterns in the last 5 moves
    if len(opponent_history) > 5:
        play_order.append("".join(opponent_history[-5:]))

    # Potential next plays based on the last 4 moves
    if len(opponent_history) > 4:
        last_four = "".join(opponent_history[-4:])
        potential_plays = [
            last_four + "R",
            last_four + "P",
            last_four + "S",
        ]
    else:
        potential_plays = ["R", "P", "S"]

    # Count occurrences of potential plays in play_order
    sub_order = {k: play_order.count(k) for k in potential_plays if k in play_order}

    # prediction if have sub order
    if sub_order:
        prediction = max(sub_order, key=sub_order.get)[-1]
    else:
        # Simple frequency analysis for early game
        counters = {"R": 0, "P": 0, "S": 0}
        if len(opponent_history) >= 2:
            if opponent_history[-1] == opponent_history[-2]:
                counters[opponent_history[-1]] *= 0.5
        for play in opponent_history:
            if play in counters:
                counters[play] += 1
        prediction = max(counters, key=counters.get)

    # move choosing
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
