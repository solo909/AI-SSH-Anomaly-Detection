def rule_based_detection(
    features_df,
    fail_threshold=10,        # failed 10+ times
    unique_user_threshold=5,  # tried 5+ different usernames
    rate_threshold=5.0        # 5+ attempts per minute
):
    df = features_df.copy()

    df["rule_flag"] = (
        (df["failed_attempts"] >= fail_threshold)        |
        (df["unique_users"]    >= unique_user_threshold) |
        (df["attempt_rate"]    >= rate_threshold)
    ).astype(int)

    return df
