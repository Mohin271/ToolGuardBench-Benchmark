"""
==========================================================
ToolGuardBench Evaluator v1.0
----------------------------------------------------------
Evaluates the quality of the generated benchmark dataset.

Features
--------
1. Dataset Loading
2. Duplicate Sample ID Detection
3. Duplicate Query Detection
4. Missing Value Detection
5. Empty String Detection
6. Risk Score Validation
7. Decision Validation

Author:
MOHIN

==========================================================
"""

import os
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

DATASET_PATH = "../dataset/ToolGuardBench.csv"

VALID_DECISIONS = [

    "ALLOW",

    "REVIEW",

    "BLOCK"

]

# ==========================================================
# Load Dataset
# ==========================================================

def load_dataset():

    if not os.path.exists(DATASET_PATH):

        raise FileNotFoundError(

            f"Dataset not found:\n{DATASET_PATH}"

        )

    df = pd.read_csv(DATASET_PATH)

    return df


# ==========================================================
# Dataset Information
# ==========================================================

def dataset_information(df):

    print("=" * 60)

    print("GENERAL INFORMATION")

    print("=" * 60)

    print(f"Total Samples : {len(df)}")

    print(f"Columns       : {len(df.columns)}")

    print(f"Templates     : {df['tool_name'].nunique()}")

    print(f"Categories    : {df['attack_type'].nunique()}")

    print()


# ==========================================================
# Duplicate Sample IDs
# ==========================================================

def check_duplicate_ids(df):

    duplicates = df[df.duplicated("sample_id")]

    print("=" * 60)

    print("DUPLICATE SAMPLE IDs")

    print("=" * 60)

    print(

        f"Duplicate IDs : {len(duplicates)}"

    )

    return duplicates


# ==========================================================
# Duplicate Queries
# ==========================================================

def check_duplicate_queries(df):

    duplicates = df[

        df.duplicated("user_query")

    ]

    print("=" * 60)

    print("DUPLICATE USER QUERIES")

    print("=" * 60)

    print(

        f"Duplicate Queries : {len(duplicates)}"

    )

    return duplicates


# ==========================================================
# Missing Values
# ==========================================================

def check_missing_values(df):

    print("=" * 60)

    print("MISSING VALUES")

    print("=" * 60)

    missing = df.isnull().sum()

    print(missing)

    print()

    return missing


# ==========================================================
# Empty Strings
# ==========================================================

def check_empty_strings(df):

    print("=" * 60)

    print("EMPTY STRINGS")

    print("=" * 60)

    total_empty = 0

    for column in df.columns:

        if df[column].dtype == object:

            count = (

                df[column]

                .astype(str)

                .str.strip()

                .eq("")

                .sum()

            )

            total_empty += count

            print(

                f"{column:20} : {count}"

            )

    print()

    return total_empty


# ==========================================================
# Risk Score Validation
# ==========================================================

def validate_risk_scores(df):

    invalid = df[

        (df["risk_score"] < 0)

        |

        (df["risk_score"] > 100)

    ]

    print("=" * 60)

    print("RISK SCORE VALIDATION")

    print("=" * 60)

    print(

        f"Invalid Scores : {len(invalid)}"

    )

    print()

    return invalid


# ==========================================================
# Decision Validation
# ==========================================================

def validate_decisions(df):

    invalid = df[

        ~df["decision"].isin(

            VALID_DECISIONS

        )

    ]

    print("=" * 60)

    print("DECISION VALIDATION")

    print("=" * 60)

    print(

        f"Invalid Decisions : {len(invalid)}"

    )

    print()

    return invalid
# ==========================================================
# Tool Distribution
# ==========================================================

def tool_distribution(df):

    print("=" * 60)
    print("TOOL DISTRIBUTION")
    print("=" * 60)

    distribution = df["tool_name"].value_counts()

    print(distribution)
    print()

    return distribution


# ==========================================================
# Attack Type Distribution
# ==========================================================

def attack_distribution(df):

    print("=" * 60)
    print("ATTACK TYPE DISTRIBUTION")
    print("=" * 60)

    distribution = df["attack_type"].value_counts()

    print(distribution)
    print()

    return distribution


# ==========================================================
# Decision Distribution
# ==========================================================

def decision_distribution(df):

    print("=" * 60)
    print("DECISION DISTRIBUTION")
    print("=" * 60)

    distribution = df["decision"].value_counts()

    print(distribution)
    print()

    return distribution


# ==========================================================
# Human Review Distribution
# ==========================================================

def human_review_distribution(df):

    print("=" * 60)
    print("HUMAN REVIEW DISTRIBUTION")
    print("=" * 60)

    distribution = df["human_required"].value_counts()

    print(distribution)
    print()

    return distribution


# ==========================================================
# Risk Statistics
# ==========================================================

def risk_statistics(df):

    print("=" * 60)
    print("RISK SCORE STATISTICS")
    print("=" * 60)

    print(f"Average Risk Score : {df['risk_score'].mean():.2f}")
    print(f"Minimum Risk Score : {df['risk_score'].min()}")
    print(f"Maximum Risk Score : {df['risk_score'].max()}")

    print()


# ==========================================================
# Save Reports
# ==========================================================

def save_reports(duplicate_ids, duplicate_queries):

    os.makedirs("../reports", exist_ok=True)

    duplicate_ids.to_csv(
        "../reports/duplicate_ids.csv",
        index=False
    )

    duplicate_queries.to_csv(
        "../reports/duplicate_queries.csv",
        index=False
    )


# ==========================================================
# Final Dataset Status
# ==========================================================

def dataset_status(
    duplicate_ids,
    duplicate_queries,
    invalid_scores,
    invalid_decisions
):

    print("=" * 60)
    print("FINAL DATASET STATUS")
    print("=" * 60)

    errors = (
        len(duplicate_ids)
        + len(invalid_scores)
        + len(invalid_decisions)
    )

    if errors == 0:

        print("STATUS : PASS")

    else:

        print("STATUS : FAIL")

    print()

    print(
        f"Duplicate Queries : {len(duplicate_queries)} "
        "(Warning only)"
    )

    print("=" * 60)


# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 60)
    print("ToolGuardBench Evaluator v1.0")
    print("=" * 60)

    df = load_dataset()

    dataset_information(df)

    duplicate_ids = check_duplicate_ids(df)

    duplicate_queries = check_duplicate_queries(df)

    check_missing_values(df)

    check_empty_strings(df)

    invalid_scores = validate_risk_scores(df)

    invalid_decisions = validate_decisions(df)

    tool_distribution(df)

    attack_distribution(df)

    decision_distribution(df)

    human_review_distribution(df)

    risk_statistics(df)

    save_reports(
        duplicate_ids,
        duplicate_queries
    )

    dataset_status(
        duplicate_ids,
        duplicate_queries,
        invalid_scores,
        invalid_decisions
    )


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    main()