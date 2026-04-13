
def rule_based_detection(features_df, fail_threshold=2):                # If failed attmepts > or = 2 , flag as suspicious
    features_df["rule_flag"] = features_df["failed_attempts"].apply(            # Creates new coll in features_df table to track rule_flag
        lambda x: 1 if x >= fail_threshold else 0                           # Applying the flag rule
    )
    return features_df                                                  # Returns updated table