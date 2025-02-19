from browser_use import Agent, Browser, BrowserConfig
from langchain_openai import ChatOpenAI
import asyncio

# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',  # Windows path
    )
)

async def main():
    # Ask the user for the target URL
    url = input("Enter the URL to search for contact information: ").strip()

    # Construct task description
    task_description = (
        f"Navigate to {url} and thoroughly search the webpage for contact information. "
        "Look for email addresses, phone numbers, physical addresses, and social media links. "
        "Check common sections like 'Contact Us', 'About', and page footers. "
        "Extract any found information and present it in a clear summary."
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
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())