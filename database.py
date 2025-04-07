from phi.agent import Agent
from phi.tools.sql import SQLTools
from phi.model.google import Gemini

db_url = "sqlite:///db.sqlite3"  # Adjust path if necessary
agent = Agent(tools=[SQLTools(db_url=db_url)],model=Gemini(id="gemini-2.0-flash-exp", temperature=0.4))

agent.print_response(
    """Analyze the manufacturer_quoterequest table and:
1. Identify which columns contain product and category information
2. Count the frequency of each product and category appearing in quote requests
3. Rank them by demand frequency (most frequent first)
4. Return the top 10 products and top 10 categories with their counts

Explain your approach and show the results in a clear markdown table format.""",
    markdown=True
)