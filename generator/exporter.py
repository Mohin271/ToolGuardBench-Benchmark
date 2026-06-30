"""
==========================================================
ToolGuardBench Exporter
----------------------------------------------------------
Exports generated benchmark datasets into:

1. CSV
2. JSONL

Author:
<AM-01>
==========================================================
"""

import csv
import json
import os


# ==========================================================
# Create Output Directory
# ==========================================================

def ensure_output_directory():

    os.makedirs("../dataset", exist_ok=True)


# ==========================================================
# Export CSV
# ==========================================================

def export_csv(dataset, filename="../dataset/ToolGuardBench.csv"):

    ensure_output_directory()

    if len(dataset) == 0:
        print("Dataset is empty.")
        return

    headers = dataset[0].keys()

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=headers
        )

        writer.writeheader()

        writer.writerows(dataset)

    print(f"CSV exported successfully: {filename}")


# ==========================================================
# Export JSONL
# ==========================================================

def export_jsonl(dataset, filename="../dataset/ToolGuardBench.jsonl"):

    ensure_output_directory()

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        for sample in dataset:

            file.write(
                json.dumps(sample)
            )

            file.write("\n")

    print(f"JSONL exported successfully: {filename}")