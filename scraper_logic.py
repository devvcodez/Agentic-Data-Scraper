import requests
from bs4 import BeautifulSoup
import json

class AgenticDataScraper:
    def __init__(self, target_url):
        self.target_url = target_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

    def fetch_raw_html(self):
        """Fetches raw DOM data from the target endpoint."""
        try:
            response = requests.get(self.target_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to fetch data: {e}")
            return None

    def structure_for_llm(self, raw_html):
        """Cleans and structures data into a JSON format for Agent evaluation."""
        if not raw_html:
            return None
            
        soup = BeautifulSoup(raw_html, "html.parser")
        
        # Extracting core knowledge graph components
        page_title = soup.title.string if soup.title else "No Title"
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
        
        structured_data = {
            "metadata": {
                "source": self.target_url,
                "title": page_title,
                "status": "Cleaned"
            },
            "agent_context": paragraphs[:5] # Sending top 5 nodes for LLM context
        }
        
        return json.dumps(structured_data, indent=4)

if __name__ == "__main__":
    # Test execution
    target = "https://example.com/technical-docs"
    scraper = AgenticDataScraper(target)
    
    html_data = scraper.fetch_raw_html()
    clean_json = scraper.structure_for_llm(html_data)
    
    if clean_json:
        print("[SUCCESS] Data structured for Agent Evaluation:")
        print(clean_json)
