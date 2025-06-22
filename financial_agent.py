from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

load_dotenv()

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for financial information",
    model=Groq(id="llama-3.3-70b-versatile"),  # Updated model ID
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name="Financial Agent",
    role="Analyze financial data and provide insights",
    model=Groq(id="llama-3.3-70b-versatile"),  # Updated model ID
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile"),  # Updated model ID
    instructions=["always include sources", "use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analysts recommendation and share the latest news for NVDA", stream=True)
