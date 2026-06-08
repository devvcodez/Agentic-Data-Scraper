# Agentic Data Scraper 
A lightweight, high-performance Python backend pipeline designed to extract, clean, and structure raw web DOM data for Large Language Model (LLM) agent evaluation and knowledge graph generation.

##  Overview
When training or evaluating AI agents, raw HTML is noisy and unstructured. This script acts as a middleware pipeline, taking raw web endpoints and parsing the data into clean, context-rich JSON payloads. It ensures that agents and evaluators receive strict, structured data to minimize hallucination and improve knowledge graph accuracy.

## Core Features
*   **DOM Extraction:** Safely fetches raw HTML with built-in timeout and error handling.
*   **Data Sanitization:** Strips unnecessary markup and isolates core contextual nodes (paragraphs, titles) for maximum signal-to-noise ratio.
*   **LLM Structuring:** Outputs strict JSON payloads designed for immediate ingestion by AI evaluation systems and prompt pipelines.

##  Tech Stack
*   **Core:** Python 3.x
*   **Network:** Requests (HTTP client)
*   **Parsing:** BeautifulSoup4 (HTML DOM manipulation)

## Quick Start

```bash
# Clone the repository
git clone [https://github.com/devvcodez/Agentic-Data-Scraper.git](https://github.com/devvcodez/Agentic-Data-Scraper.git)

# Install required dependencies
pip install requests beautifulsoup4

# Execute the pipeline
python scraper_logic.py
