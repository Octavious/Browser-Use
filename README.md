<a href="https://www.buymeacoffee.com/ArabicAI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
# Browser-Use

A Python project that demonstrates the use of browser automation with Browser Use (https://github.com/browser-use/browser-use) and Google's Gemini AI model. This project allows you to create AI agents that can perform web-based tasks using natural language instructions.

## Features

- Integration with Google's Gemini AI model
- Browser automation capabilities
- Asynchronous task execution
- Environment variable configuration for API keys
- Multiple example implementations

## Prerequisites

- Python 3.7 or higher
- A Google Gemini API key
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Octavious/Browser-Use.git
cd Browser-Use
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

The project includes three example implementations:

1. `first_example.py`: Basic example comparing GPU prices
2. `second_example.py`: Additional example to use a startup page/website
3. `third_example.py`: Another example implementation to use your own browser

To run any of the examples:

```bash
python first_example.py
```

## Project Structure

- `requirements.txt`: Project dependencies
- `.env`: Environment variables (API keys)
- `first_example.py`: Basic implementation example
- `second_example.py`: Additional example
- `third_example.py`: Another example
- `.venv/`: Virtual environment directory

## Dependencies

- langchain-google-genai: For Google Gemini AI integration
- python-dotenv: For environment variable management
- browser-use: For browser automation capabilities
