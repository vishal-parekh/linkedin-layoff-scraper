# LinkedIn Layoff Post Scraper

An intelligent web scraper that uses AI to find and collect LinkedIn profile URLs of people who have posted about being laid off. This tool leverages advanced language models and browser automation to efficiently search and extract relevant information from LinkedIn.

## Features

- 🔍 Automated LinkedIn search for layoff-related posts
- 🤖 AI-powered content understanding using GPT-4
- 🌐 Browser automation for seamless interaction
- 📊 Structured data output in JSON format
- 🔄 Intelligent navigation and profile extraction
- 📝 Conversation logging for debugging and analysis

## Technology Stack

- **Python 3.12+**: Core programming language
- **LangChain**: Framework for building applications with LLMs
- **GPT-4**: Advanced language model for understanding post content
- **Browser-Use**: Browser automation framework
- **Pydantic**: Data validation and settings management
- **Playwright**: Browser automation engine
- **Poetry**: Dependency management and packaging

## Prerequisites

- Python 3.12 or higher
- Poetry for dependency management
- Google Chrome browser
- LinkedIn account (for authentication)
- **Important Browser Setup**:
  - Must be logged into LinkedIn in your Chrome browser
  - On macOS, ensure Chrome is completely quit before running the script
  - Chrome should be installed in the default location (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` on macOS)

## Installation

1. Install dependencies using Poetry:
```bash
poetry install
```

2. Create a `.env` file in the project root with your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Ensure Chrome is completely quit (on macOS)

2. Activate the Poetry environment:
```bash
poetry shell
```

3. Run the scraper:
```bash
poetry run python src/scrape.py
```

The script will:
- Open LinkedIn and search for layoff-related posts
- Use AI to identify relevant posts
- Extract profile URLs of people who posted about layoffs
- Save the results to `LinkedinUrls.json`

## Output

The script generates a JSON file (`LinkedinUrls.json`) containing an array of LinkedIn profile URLs:
```json
{
  "urls": [
    "https://www.linkedin.com/in/profile1",
    "https://www.linkedin.com/in/profile2",
    "https://www.linkedin.com/in/profile3"
  ]
}
```

## Project Structure

```
linkedin-layoff-post-scraper/
├── src/
│   ├── models/
│   │   └── linkedin_urls.py    # Data models
│   ├── scrape.py              # Main scraper script
│   └── logs/                  # Conversation logs
├── pyproject.toml             # Poetry dependencies
└── README.md                  # This file
```

## How It Works

1. **Browser Automation**: The script uses Playwright under the hood of the browser-use package to automate Chrome browser interactions with LinkedIn.

2. **AI-Powered Search**: 
   - Uses GPT-4o to understand post content and context
   - Identifies genuine layoff announcements
   - Extracts relevant profile information

3. **Data Collection**:
   - Navigates through search results
   - Clicks on profile links
   - Extracts and validates profile URLs

4. **Output Generation**:
   - Structures data using Pydantic models
   - Saves results in JSON format
   - Maintains conversation logs for debugging

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and research purposes only. Please ensure you comply with LinkedIn's terms of service and robots.txt when using this scraper.
