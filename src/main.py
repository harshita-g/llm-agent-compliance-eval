import json
from pathlib import Path

import pandas as pd

from agent import run_agent
from evaluator import evaluate_task, summarize_results


DATA_PATH = Path("data/tasks.json")
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def load_tasks() -> list:
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    tasks = load_tasks()
    evaluations = []

    for task in tasks:
        print(f"Running {task['id']}...")
        agent_result = run_agent(task)
        evaluation = evaluate_task(task, agent_result)
        evaluations.append(evaluation)

    summary = summarize_results(evaluations)

    with open(RESULTS_DIR / "evaluations.json", "w", encoding="utf-8") as file:
        json.dump(evaluations, file, indent=2)

    with open(RESULTS_DIR / "summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)

    df = pd.DataFrame(evaluations)
    df.to_csv(RESULTS_DIR / "evaluations.csv", index=False)

    print("\nSummary:")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()