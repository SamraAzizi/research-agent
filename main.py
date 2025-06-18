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

            for i, company in enumerate(result.companies, 1):
                print(f"\n{i}. 🏢 {company.name}")
                print(f"   🌐 Website: {company.website}")
                print(f"   💰 Pricing: {company.pricing_model}")
                print(f"   📖 Open Source: {company.is_open_source}")

                if company.tech_stack:
                    print(f"   🛠️  Tech Stack: {', '.join(company.tech_stack[:5])}")

                if company.language_support:
                    print(
                        f"   💻 Language Support: {', '.join(company.language_support[:5])}"
                    )