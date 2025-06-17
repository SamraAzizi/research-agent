from dotenv import load_dotenv
from src.workflow import Workflow

load_dotenv()


def main():
    workflow = Workflow()
    print("Developer Tools Research Agent")

    while True:
        query = input("\n🔍 Developer Tools Query: ").strip()
        if query.lower() in {"quit", "exit"}:
            break

        if query:
            result = workflow.run(query)
            print(f"\n📊 Results for: {query}")
            print("=" * 60)