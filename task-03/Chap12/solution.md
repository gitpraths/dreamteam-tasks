# Web Scraping Overview

Web scraping involves using programs to download and process web content. Common applications include indexing web pages for search engines like Google.

### Python Modules for Web Scraping
1. **webbrowser**: Opens a browser to a specific page.
2. **requests**: Downloads files and web pages from the internet.
3. **bs4 (Beautiful Soup)**: Parses and extracts data from HTML content.
4. **selenium**: Automates web browsers, simulating user interactions.

---

## Project: `mapIt.py` with the `webbrowser` Module

The `webbrowser` module launches a browser to a specific URL.  
**Objective**: Automate opening Google Maps with a street address from the clipboard or command line.

**Steps**:
1. Read the command line arguments or clipboard content.
2. Construct the Google Maps URL.
3. Open the URL in a web browser.

---

## Downloading Files with the `requests` Module

The `requests` module simplifies downloading files from the web.

### Key Functions
- `requests.get()`: Downloads a web page and returns a `Response` object.
- `raise_for_status()`: Checks for errors during the download.
- `iter_content()`: Saves downloaded content in chunks.

### Example Workflow
1. Use `requests.get()` to fetch data.
2. Open a file in write binary (`wb`) mode.
3. Write content using `iter_content()`.

---

## Parsing HTML with Beautiful Soup

Beautiful Soup (`bs4`) is a library for extracting data from HTML.

### Steps
1. Create a `BeautifulSoup` object with HTML content.
2. Use the `select()` method with CSS selectors to locate elements.
3. Access attributes and text of the selected elements.

**Example Project**: Automating the opening of search results from a website.

---

## Controlling the Browser with Selenium

Selenium provides advanced control over web browsers, making it ideal for interacting with dynamic pages.

### Key Functionalities
- Locate elements using methods like class name or CSS selectors.
- Simulate clicks, fill forms, or interact with elements.
- Send keyboard inputs.

**Example Project**: Automating tasks such as logging into a website or downloading images.
