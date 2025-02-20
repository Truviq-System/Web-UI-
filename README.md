# Web Contact Information Scraper

A Python-based web scraping tool that automatically navigates websites to extract contact information, with a focus on Engineering, Artificial Intelligence, and Computer Science departments. The tool can handle language detection and translation to English, making it versatile for international use.

## Features

- Automated web navigation and scraping
- Language detection and English translation
- Focused extraction of contact information (email addresses, phone numbers, names)
- Priority targeting of specific departments (Engineering, AI, CS)
- Chrome browser automation
- Async processing capabilities

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- Google Chrome browser
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Truviq-System/Web-Ui-open-ai.git
cd web-contact-scraper
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install browser-use langchain-openai asyncio
```

## Configuration

1. Ensure you have the correct path to your Chrome executable in the code. The default is set for Windows:
```python
chrome_instance_path='C:\Program Files\Google\Chrome\Application\chrome.exe'
```

For macOS users, typically:
```python
chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
```

For Linux users, typically:
```python
chrome_instance_path='/usr/bin/google-chrome'
```

2. Set up your OpenAI API key:
```bash
# Windows
set OPENAI_API_KEY=your_api_key_here

# macOS/Linux
export OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the script:
```bash
python university.py
```

2. When prompted, enter one URL to scrape (comma-separated):
```
Enter 1 URLs: https://example.com
```

3. The script will process the URL and display the results, including:
- Website language detection
- Contact information found
- Any errors encountered during processing

## Output Format

The results will be displayed in the following format:
```
==================================================
Contact Information Results:
==================================================

-------------- URL --------------
https://example.com

------------- RESULT -------------
[Extracted contact information will appear here]
--------------------------------------------------
```

## Error Handling

The script includes error handling for:
- Invalid URLs
- Connection timeouts
- Language detection/translation issues
- General scraping errors

## Limitations

- Currently processes one URL at a time
- Requires a stable internet connection
- Chrome browser must be installed
- May be affected by website's robot policies
- Requires OpenAI API access

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Uses the browser-use library for web automation
- Powered by OpenAI's GPT-4 for intelligent scraping
- Built with langchain for AI chain operations

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
