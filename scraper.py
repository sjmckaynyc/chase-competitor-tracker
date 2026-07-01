import os
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
import time

GEMINI_KEY = os.environ.get('GEMINI_API_KEY')
if not GEMINI_KEY:
    print("Error: GEMINI_API_KEY environment variable not found. Please check GitHub Secrets.")
    exit(1)

search_queries = [
    "Chase bank OR JPMorgan marketing OR campaign OR commercial",
    "American Express OR Amex Platinum ad OR campaign OR marketing",
    "Capital One Savor OR Venture X commercial OR marketing",
    "Discover Card OR Wells Fargo Active Cash campaign OR ad",
    "Citi Double Cash OR Bank of America ad OR sweepstakes",
    "Chime OR SoFi OR Ramp OR Brex fintech marketing OR campaign"
]

all_raw_articles = []
seen_links = set()

print("Opening the floodgates. Scraping Google News...")

for query in search_queries:
    encoded_query = urllib.parse.quote(query)
    rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-US&gl=US&ceid=US:en"
    
    try:
        req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            for item in root.findall('.//item'):
                title = item.find('title').text if item.find('title') is not None else ""
                link = item.find('link').text if item.find('link') is not None else ""
                pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
                
                if title and link and link not in seen_links:
                    seen_links.add(link)
                    
                    try:
                        parsed_date = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %Z")
                        clean_date = parsed_date.strftime("%b %d, %Y")
                        sort_date = parsed_date
                    except:
                        clean_date = pub_date[:16]
                        sort_date = datetime.min
                        
                    all_raw_articles.append({
                        "title": title,
                        "link": link,
                        "published_date": clean_date,
                        "sort_date": sort_date
                    })
    except Exception as e:
        print(f"Failed to fetch {query}: {e}")

all_raw_articles.sort(key=lambda x: x["sort_date"], reverse=True)

print(f"Found {len(all_raw_articles)} live articles. Processing through the AI Filter...")

processed_data = []
today_stamp = datetime.today().strftime('%b %d, %Y')

batch_size = 10
for i in range(0, len(all_raw_articles), batch_size):
    batch = all_raw_articles[i:i+batch_size]
    
    prompt_text = "You are an elite Competitive Intelligence AI for Chase. Analyze these raw financial news articles. Return a raw JSON array of objects. Use the EXACT link and published_date provided.\n\n"
    for idx, article in enumerate(batch):
        prompt_text += f"Article {idx+1}:\nTitle: {article['title']}\nLink: {article['link']}\nDate: {article['published_date']}\n\n"
        
    prompt_text += f"""
CRITICAL FILTERING RULES:
Act as a strict intelligence filter. You must DISCARD any article that is:
- Routine stock market news or earnings calls.
- Local branch openings, basic charity events, or minor executive hires.
- Generic economic fluff.

ONLY return objects for articles that represent a clear strategic move, new ad campaign, credit card launch, rewards change, or direct competitive threat.

Instructions for each approved object:
- "lob": Assign "Sapphire", "Freedom", "Business", or "Consumer".
- "subBrand": Short segment tag (e.g., Reserve, Unlimited, CSRB, Checking/Savings).
- "format": "Video" (if ad, commercial, tv) else "Article".
- "priority": Rate the threat level as "Tier 1: High Impact" or "Tier 2: Medium Impact".
- "competitor": Brand name.
- "title": Clean the headline.
- "channels": Estimate 2-3 media placements.
- "summary": 1-2 sentence overview of the strategic move.
- "creative": Provide "AI & Media Inflation Analysis Summary".
- "published_date": EXACT date from the prompt.
- "link": EXACT link from the prompt.
- "added_date": "{today_stamp}"

Output MUST be a valid JSON array of ONLY the important articles. If none are important, return an empty array []. No markdown code blocks.
"""

    data = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {"temperature": 0.2}
    }
    
    try:
        req = urllib.request.Request(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}",
            data=json.dumps(data).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req, timeout=45) as response:
            res_json = json.loads(response.read().decode('utf-8'))
            ai_text = res_json['candidates'][0]['content']['parts'][0]['text'].strip()
            
            # Ultra-safe formatting cleanup so it never crashes
            if "```json" in ai_text:
                ai_text = ai_text.split("```json")[1]
            elif "```" in ai_text:
                ai_text = ai_text.split("```")[1]
            if "```" in ai_text:
                ai_text = ai_text.split("```")[0]
                
            ai_text = ai_text.strip()
            
            batch_results = json.loads(ai_text)
            processed_data.extend(batch_results)
            print(f"Successfully filtered and processed batch {i//batch_size + 1}")
    except Exception as e:
        print(f"Error processing batch {i//batch_size + 1}, skipping...: {e}")
        
    # THE THROTTLE: Tell the script to go to sleep for 5 seconds between batches so the API doesn't lock us out.
    time.sleep(5)

# Save the Final Dynamic Output
if processed_data:
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, indent=2)
    print(f"Live Intelligence Hub updated with {len(processed_data)} highly relevant, verified articles.")
else:
    print("Pipeline failure: No articles processed or none passed the filter.")
