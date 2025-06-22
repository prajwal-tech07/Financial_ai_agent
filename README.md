# 💰 Financial AI Agent

A multi-agent financial analysis system built using the Phi Framework and Groq's LLaMA-3 model. It fetches live stock data, analyst recommendations, and recent financial news to provide powerful insights using multi-agent orchestration.

## Features

- 🧠 Multi-agent architecture using Phi framework
- 📈 Real-time financial data using YFinance
- 🌐 Web search integration via DuckDuckGo
- 📊 Structured stock analysis and analyst ratings
- 🔌 Groq’s ultra-fast LLMs with tool support

## Prerequisites

- Python 3.8 or higher
- Groq API Key (get it from https://console.groq.com)

## Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/financial-ai-agent.git
cd financial-ai-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your Groq API Key
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# Run the financial agent
python financial_agent.py
```

## Example Query

By default, it analyzes NVIDIA (NVDA). To analyze another stock like AAPL, open `financial_agent.py` and change this line:

```python
multi_ai_agent.print_response("Summarize analysts recommendation and share the latest news for AAPL", stream=True)
```

## Sample Output

- ✅ Analyst ratings and price targets
- 📰 Latest news headlines and summaries
- 📊 Stock fundamentals and performance data
- 📋 Structured tables and insights

## Project Structure

```
financial-ai-agent/
├── financial_agent.py     # Main application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (you create this)
├── .gitignore             # Ignore unnecessary files
└── README.md              # Project documentation
```

## Agent & Model Configuration

- Web Search Agent → Finds recent financial news
- Financial Agent → Analyzes stock via YFinance
- Multi-Agent System → Combines insights into one response
- LLM Model → Groq LLaMA3-70B with high performance and low latency

## API Key Setup

```bash
# Go to https://console.groq.com
# Login and generate a new API key
# Add it to your .env file like this:
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

## Dependencies (in requirements.txt)

```
phi-ai
groq
yfinance
duckduckgo-search
python-dotenv
```

## Customization

To change stock analysis:

```python
multi_ai_agent.print_response("Summarize analysts recommendation and share the latest news for TSLA", stream=True)
```

To add more tools:

```python
from phi.tools.newspaper import Newspaper
from phi.tools.wikipedia import Wikipedia

tools = [YFinanceTools(), Newspaper(), Wikipedia()]
```

To modify instructions:

```python
financial_agent = Agent(
    name="Financial Agent",
    instructions=[
        "Focus on technical analysis",
        "Include risk assessment",
        "Compare with sector averages"
    ],
    ...
)
```

## Common Issues

- ❌ Model Error → Update to latest model ID: `llama3-70b-8192`
- 🔑 Invalid Key → Check your `.env` file for correct `GROQ_API_KEY`
- ⏱️ Rate Limiting → Groq has generous free limits; delay requests if needed

## Contributing

```bash
# Fork the repo
# Create a branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push changes
git push origin feature/amazing-feature

# Open a Pull Request on GitHub
```

## Acknowledgments

- Phi Framework – Multi-agent intelligence
- Groq – Fast LLM inference
- YFinance – Financial market data
- DuckDuckGo – News search

## Screenshots
![Screenshot 2025-06-22 210226](https://github.com/user-attachments/assets/dd308c2c-b8ef-4a60-90c3-cda6e822d0d4)
![Screenshot 2025-06-22 210241](https://github.com/user-attachments/assets/ef3b528c-37c2-408f-aade-6acdf7ea7773)


