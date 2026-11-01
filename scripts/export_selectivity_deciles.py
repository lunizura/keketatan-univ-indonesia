"""
Export script for computing national selectivity distribution deciles across Indonesian universities.
Analyzes SNBP and SNBT selectivity percentage distributions, calculates decile thresholds,
computes interquartile ranges, and exports statistical summaries for educational planning.
"""

import argparse
import json
import math
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
INPUT_FILE = os.path.join(DATA_DIR, "ptn_keketatan.json")
OUTPUT_FILE = os.path.join(DATA_DIR, "selectivity_deciles.json")


def calculate_percentile(sorted_data, percentile):
    """Calculate the percentile value using linear interpolation."""
    if not sorted_data:
        return 0.0
    n = len(sorted_data)
    if n == 1:
        return sorted_data[0]
    rank = (percentile / 100.0) * (n - 1)
    k = math.floor(rank)
    d = rank - k
    if k + 1 < n:
        return round(sorted_data[k] + d * (sorted_data[k + 1] - sorted_data[k]), 4)
    return round(float(sorted_data[k]), 4)


def compute_distribution_metrics(values):
    """Compute comprehensive distribution metrics including deciles and quartiles."""
    if not values:
        return {}
    s = sorted(values)
    n = len(s)
    mean_val = round(sum(s) / n, 4)

    deciles = {}
    for p in range(10, 100, 10):
        deciles[f"D{p // 10}"] = calculate_percentile(s, p)

    q1 = calculate_percentile(s, 25)
    median = calculate_percentile(s, 50)
    q3 = calculate_percentile(s, 75)
    iqr = round(q3 - q1, 4)

    return {
        "sample_size": n,
        "min": round(min(s), 4),
        "max": round(max(s), 4),
        "mean": mean_val,
        "median": median,
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "deciles": deciles,
    }


def analyze_selectivity(dataset):
    """Analyze SNBP and SNBT selectivity across overall and rumpun partitions."""
    snbp_all = []
    snbt_all = []
    snbp_saintek = []
    snbt_saintek = []
    snbp_soshum = []
    snbt_soshum = []

    for item in dataset:
        snbp_val = item.get("snbp", {}).get("keketatan_persen")
        snbt_val = item.get("snbt", {}).get("keketatan_persen")
        rumpun = item.get("rumpun", "").strip()

        if snbp_val is not None:
            snbp_all.append(float(snbp_val))
            if rumpun.lower() == "saintek":
                snbp_saintek.append(float(snbp_val))
            elif rumpun.lower() == "soshum":
                snbp_soshum.append(float(snbp_val))

        if snbt_val is not None:
            snbt_all.append(float(snbt_val))
            if rumpun.lower() == "saintek":
                snbt_saintek.append(float(snbt_val))
            elif rumpun.lower() == "soshum":
                snbt_soshum.append(float(snbt_val))

    return {
        "metadata": {
            "source": "ptn_keketatan.json",
            "total_study_programs": len(dataset),
        },
        "snbp": {
            "overall": compute_distribution_metrics(snbp_all),
            "saintek": compute_distribution_metrics(snbp_saintek),
            "soshum": compute_distribution_metrics(snbp_soshum),
        },
        "snbt": {
            "overall": compute_distribution_metrics(snbt_all),
            "saintek": compute_distribution_metrics(snbt_saintek),
            "soshum": compute_distribution_metrics(snbt_soshum),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compute national selectivity distribution deciles for Indonesian higher education."
    )
    parser.add_argument(
        "--input",
        default=INPUT_FILE,
        help="Path to input ptn_keketatan.json file",
    )
    parser.add_argument(
        "--output",
        default=OUTPUT_FILE,
        help="Path to output selectivity_deciles.json file",
    )
    parser.add_argument(
        "--print-summary",
        action="store_true",
        help="Print text summary to console",
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file not found at {args.input}", file=sys.stderr)
        sys.exit(1)

    with open(args.input, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    result = analyze_selectivity(dataset)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Selectivity deciles successfully exported to: {args.output}")

    if args.print_summary or True:
        snbp = result["snbp"]["overall"]
        snbt = result["snbt"]["overall"]
        print("-" * 60)
        print("NATIONAL SELECTIVITY SUMMARY (OVERALL)")
        print("-" * 60)
        print(f"Total Programs Analyzed: {result['metadata']['total_study_programs']}")
        print(f"SNBP Selectivity: Median={snbp['median']}%, Q1={snbp['q1']}%, Q3={snbp['q3']}%")
        print(f"SNBT Selectivity: Median={snbt['median']}%, Q1={snbt['q1']}%, Q3={snbt['q3']}%")
        print("SNBP Decile Thresholds:")
        for k, v in snbp["deciles"].items():
            print(f"  {k}: {v}%")
        print("SNBT Decile Thresholds:")
        for k, v in snbt["deciles"].items():
            print(f"  {k}: {v}%")
        print("-" * 60)


if __name__ == "__main__":
    main()
