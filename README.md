
# JQuery-scraping

JQuery-scraping is a Python package designed for web scraping and Selenium-based automation, utilizing one of the easiest and most powerful JavaScript libraries: JQuery. This package enables users to execute JQuery scripts within web pages through Selenium, simplifying the process of web scraping and interacting with web elements.

## Getting Started

To use JQuery-scraping for your web scraping projects, follow these steps:

### Installation

1. Clone this repository or download the source code.
2. Navigate to the root directory of the project.
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Basic Usage

To get started with JQuery-scraping, you can run the following basic code to test the setup:

```python
from src.lib.Browser import BROWSER

Browser = BROWSER()
Browser.jquery()
result = Browser('return 3')
print(result)
```

This code initializes a browser session, injects JQuery, and executes a simple JavaScript command.

### Examples

The project includes several Jupyter notebooks demonstrating how to scrape various websites:

- **Amazon Scraping**: Check out the [Amazon-Scrape.ipynb](src/Amazon-Scrape.ipynb) notebook for a detailed example of how to scrape Amazon web pages.
- **Custom Amazon Scraping**: For a customized Amazon scraping example, see [Amazon-Scrape-custom.ipynb](src/Amazon-Scrape-custom.ipynb).
- **Coordinate Scraping**: To scrape geographical coordinates, refer to [Coordinate scrape.ipynb](src/Coordinate%20scrape.ipynb).
- **Facebook Scraping**: For scraping Facebook, take a look at [Facebook-Scrape.ipynb](src/Facebook-Scrape.ipynb).

## Contributing

Contributions to JQuery-scraping are welcome! Please feel free to submit pull requests or open issues to improve the project or add new features.
