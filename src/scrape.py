import json
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig, Controller
from dotenv import load_dotenv
from models.linkedin_urls import LinkedInUrls

load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")


controller = Controller(output_model=LinkedInUrls)


# Configure the browser using Playwright's built-in browser
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)


async def main():
    agent = Agent(
        task=f"""Go to Linkedin.com and search for posts by people that state "I was laid off" and click on their name or profile picture to go to their profile page. Get the link to their profile and save it to a json file. Go back to the search page and find the next 2 posts and repeat until you have found 3 total linkedin profile links.
        The json file should be named "LinkedinUrls.json" and the urls should be a list of the URL links to the profile pages.
        """,
        llm=llm,
        controller=controller,
        browser=browser,
        save_conversation_path="src/logs/conversation.json",
        planner_interval=4,  # plan every 4 steps
    )
    history = await agent.run()
    result = history.final_result()

    if result:
        # Parse the result into Pydantic model
        parsed: LinkedInUrls = LinkedInUrls.model_validate_json(result)

        # Save to a JSON file
        with open("src/linkedin_urls.json", "w") as f:
            json.dump(parsed.model_dump(), f, indent=2)

        # Print what we got
        print("\nFound LinkedIn Profile URLs:")
        for url in parsed.urls:
            print(f"- {url}")


asyncio.run(main())
