from pydantic import BaseModel, Field
from agents import Agent
from datetime import datetime
month_year = datetime.now().strftime("%B %Y")

HOW_MANY_SEARCHES = 5

INSTRUCTIONS = f"""
You are a helpful research assistant. Given a query, come up with a set of web searches to perform to best answer the query.
Output {HOW_MANY_SEARCHES} terms to query for.
If the query involves trends, news, entertainment, or anything that changes over time, include the current time context — such 
as "{month_year}" or "in the past month" — in your search terms. You MUST make sure all search queries return results relevant 
as of {month_year}. Avoid results from previous years unless explicitly requested.
"""


class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")
    
planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)