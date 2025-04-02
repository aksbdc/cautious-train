# [AKSBDC]
# GOAL: Train LLM with {...} data?
# TASK: Connect GPT to API.
# END: Mindful of privacy / P.I.I. / I.P. / etc.

from huggingface_hub import hf_hub_download
import pandas as pd

REPO_ID = "YOUR_REPO_ID"
FILENAME = "data.csv"

dataset = pd.read_csv(
    hf_hub_download(repo_id=REPO_ID, filename=FILENAME, repo_type="dataset")
)

def main():
    print("Hello from cautious-train!")


if __name__ == "__main__":
    main()
