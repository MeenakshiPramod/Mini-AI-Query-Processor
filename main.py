import argparse
from utils import clean_text, read_data, write_data, log
from agent import QueryAgent
import asyncio

def main():
    try:
        parser = argparse.ArgumentParser(description="Mini AI Query Processor")
        parser.add_argument("--query", type=str, help="Input query")
        parser.add_argument("--history", action="store_true", help="Show past queries")
        args = parser.parse_args()

        

        raw_query = args.query
        cleaned_query = clean_text(raw_query)

        log(f"Received query: {raw_query}")

        agent = QueryAgent(cleaned_query)
        result = asyncio.run(agent.process())

        data = read_data()
        data.append(result)
        write_data(data)

        print("\n✅ Response:")
        print(result)

        if args.history:
            data = read_data()
            print("\n📜 Query History:")
            for item in data:
                print(item)
                return

        if args.query:
            raw_query = args.query
        else:
            raise ValueError("Please provide a query using --query")

    except Exception as e:
        log(f"Error occurred: {str(e)}", level="ERROR")
        print("❌ Something went wrong. Check logs.")

if __name__ == "__main__":
    main()