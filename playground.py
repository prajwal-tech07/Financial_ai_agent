from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app  # <-- Add this line
import os
from dotenv import load_dotenv
load_dotenv()   

phi.api_key=os.getenv("PHI_API_KEY")

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

app=Playground(agents=[web_search_agent, financial_agent]).get_app()
if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)