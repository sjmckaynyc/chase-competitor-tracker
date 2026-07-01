import os
import json
import re
import requests
from datetime import datetime

GEMINI_KEY = os.environ.get('GEMINI_API_KEY')

# Live industry trade RSS links converting raw articles and commercial trackers into clean JSON data strings
feed_urls = [
    "https://www.adweek.com/feed/",
    "https://www.campaignlive.com/rss/news",
    "https://www.marketingweek.com/feed/"
]

collected_intel = []

# Fetch live items across the trade grid
for url in feed_urls:
    try:
        response = requests.get(url, timeout=10)
        # Using regex pattern match mapping to quickly isolate feed rows without adding clunky dependencies
        items = re.findall(r'<item>(.*?)</item>', response.text, re.DOTALL)
    except:
        items = []

    for item in items:
        if len(collected_intel) >= 25:  # High-density cap to match Google News page density constraints
            break
            
        title_match = re.search(r'<title>(.*?)</title>', item)
        link_match = re.search(r'<link>(.*?)</link>', item)
        desc_match = re.search(r'<description>(.*?)</description>', item)
        
        headline = title_match.group(1).replace('<![CDATA[', '').replace(']]>', '') if title_match else ""
        source_url = link_match.group(1).replace('<![CDATA[', '').replace(']]>', '') if link_match else "https://www.adweek.com"
        description = desc_match.group(1).replace('<![CDATA[', '').replace(']]>', '') if desc_match else ""
        
        # Clean HTML tag remnants out of the raw RSS stream strings
        description = re.sub(r'<[^>]*>', '', description).strip()
        
        if not headline or len(headline) < 10:
            continue

        # Master AI parsing logic parsing live elements into the core layout metrics
        prompt_instruction = f"""
        Analyze this live financial services marketing trade item:
        Headline: {headline}
        Description: {description}

        Based on the text content, match it to one of these major banking sectors:
        - If it mentions luxury, travel, premium lifestyle, dining, Amex Platinum, or high-end travel cards, set lob to "Sapphire".
        - If it mentions everyday cash-back, students, credit builders, Capital One Savor, or everyday cards, set lob to "Freedom".
        - If it mentions startups, corporate spend, B2B, Ramp, small business, or enterprise infrastructure, set lob to "Business".
        - If it mentions retail banking, checking accounts, deposits, high-yield savings, branch footprints, or consumer wealth, set lob to "Consumer".
        
        If it doesn't fit any cleanly, intelligently distribute it based on demographic reach. Select the targeted subBrand segment tag (e.g., Reserve, Preferred, Unlimited, Flex, Rise, Ink, CSRB, Business Checking, Checking/Savings, Private Client).
        Set the media format as "Video" if it mentions a commercial, TV spot, video drop, or film, otherwise set it as "Article".
        Rate its priority strictly as: "Tier 1: High Impact", "Tier 2: Medium Impact", or "Tier 3: Low Impact".

        Provide an "AI & Media Inflation Analysis Summary". This block must discuss how this specific competitor move forces shifting Customer Acquisition Costs (CAC), programmatic ad bidding inflation, automated platform delivery dynamics, or macro attention span decay.

        Respond ONLY with a valid JSON block matching this structure, without markdown wraps, backticks, or prose:
        {{
          "lob": "Sapphire or Freedom or Business or Consumer",
          "subBrand": "segment tag",
          "format": "Video or Article",
          "priority": "Tier rating classification string",
          "competitor": "Identify the core competing financial brand or app name mentioned",
          "title": "short clear title summarizing the action",
          "channels": "estimated ad media placement placements used",
          "summary": "2-3 sentence overview of what the competitor is doing business-wise.",
          "creative": "The complete AI & Media Inflation Analysis Summary."
        }}
        """
        
        gemini_endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
        payload = {"contents": [{"parts": [{"text": prompt_instruction}]}]}
        
        try:
            res = requests.post(gemini_endpoint, json=payload, timeout=12).json()
            ai_raw_output = res['candidates'][0]['content']['parts'][0]['text'].strip()
            
            if "```json" in ai_raw_output:
                ai_raw_output = ai_raw_output.split("```json")[1].split("```")[0].strip()
            elif "```" in ai_raw_output:
                ai_raw_output = ai_raw_output.split("```")[1].split("```")[0].strip()
                
            data_block = json.loads(ai_raw_output)
            data_block['date'] = datetime.today().strftime('%b %d, %Y')
            
            # If the entry mentions video format, map it straight to an active video link container
            if data_block['format'] == "Video" and "youtube" not in source_url:
                data_block['link'] = "https://www.youtube.com/results?search_query=" + requests.utils.quote(data_block['competitor'] + " " + data_block['title'])
            else:
                data_block['link'] = source_url
                
            collected_intel.append(data_block)
        except:
            continue

# Overwrite database with the real-time high-density news cluster tracking array
if collected_intel:
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(collected_intel, f, indent=2)
    print(f"Successfully processed {len(collected_intel)} real-time high density campaign entries.")
