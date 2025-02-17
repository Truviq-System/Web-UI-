from browser_use import Agent, Browser, BrowserConfig
from langchain_openai import ChatOpenAI
import asyncio

# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',  # Windows path
    )
)

async def main():
    # Ask the user for their LinkedIn profile name
    name = input("Enter your LinkedIn profile name: ").strip()

    # Define search queries
    search_queries = [
        f"{name} anti-money laundering",
        f"{name} scams",
        f"{name} adverse media"
    ]

    # Construct task description
    task_description = (
        f"Perform a Google search for '{name}' and analyze search result snippets (titles & descriptions) for potential adverse information. "
        f"For each of the following searches: '{search_queries[0]}', '{search_queries[1]}', and '{search_queries[2]}', check the first three results. "
        f"If any snippet suggests missing or critical adverse statements, visit the corresponding link and extract a brief summary of the relevant content."
    )

    # Create the agent with a single instance of the browser
    agent = Agent(
        task=task_description,
        llm=ChatOpenAI(model='gpt-4o'),
        browser=browser,
    )

    try:
        await agent.run()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await browser.close()  # Ensure the browser closes properly

if __name__ == '__main__':
    asyncio.run(main())
