from agents import Agent, WebSearchTool, ModelSettings, function_tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
load_dotenv()


serper = GoogleSerperAPIWrapper()

@function_tool
def serper_search(query: str) -> str:
    """Search the web using Serper and return results as a string."""
    results = serper.run(query)
    return results


INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself."
)

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[serper_search],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
)