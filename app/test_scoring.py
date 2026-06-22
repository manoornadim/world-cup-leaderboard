from app.scoring import calculate_leaderboard, score_match


def test_score_match():
    assert score_match(2, 1, 2, 1) == 3  # exact
    assert score_match(2, 0, 1, 0) == 1  # correct result (home win)
    assert score_match(0, 2, 1, 1) == 0  # wrong


def test_leaderboard():
    leaderboard = calculate_leaderboard()

    print("\nLeaderboard:")
    for user in leaderboard:
        print(user["name"], user["points"])


if __name__ == "__main__":
    test_score_match()
    test_leaderboard()