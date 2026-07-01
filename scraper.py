import os
import json
import requests
from datetime import datetime

# Secure cloud system keys loading parameters
NEWS_KEY = os.environ.get('NEWS_API_KEY')
GEMINI_KEY = os.environ.get('GEMINI_API_KEY')

# Deep agency vault explicitly mapped directly to absolute destination URLs
ad_intelligence_vault = [
    {
        "lob": "Sapphire",
        "subBrand": "Reserve",
        "priority": "Tier 1: High Impact",
        "competitor": "American Express Platinum",
        "title": "Priority Notify & Platinum Nights Showcase",
        "channels": "YouTube, Resy Mobile In-App, Instagram Reels",
        "summary": "Amex shifts their 2026 creative messaging directly onto lifestyle prestige, highlighting Resy Priority Notify booking alerts and zero-friction access at elite culinary hotspots over standard cash-back rewards math.",
        "creative": "Human Truth: Affluent consumers don't want standard point multipliers; they crave the ultimate social status of immediate, effortless bypass control over high-friction cultural spaces.",
        "link": "https://www.youtube.com/watch?v=11spbSgfcc0"
    },
    {
        "lob": "Sapphire",
        "subBrand": "Preferred",
        "priority": "Tier 2: Medium Impact",
        "competitor": "American Express Platinum",
        "title": "'Fine Hotels & Resorts' Global Footprint Campaign",
        "channels": "YouTube, Connected TV, Premium Digital OOH",
        "summary": "Amex rolls out high-end cinematographic spots demonstrating luxury travel booking enhancements, complimentary luxury breakfast buffers, and late checkouts across their global hotel network footprint.",
        "creative": "Human Truth: Modern travelers aren't looking to see a destination; they are looking to be taken care of by an ecosystem that elevates them above the standard tourist cattle-call.",
        "link": "https://www.youtube.com/watch?v=kZ1IZwpCvn4"
    },
    {
        "lob": "Freedom",
        "subBrand": "Unlimited",
        "priority": "Tier 1: High Impact",
        "competitor": "Capital One Saver Card",
        "title": "March Madness 'Splashes' Feature Spot",
        "channels": "YouTube Broadcast, Linear Sports TV, TikTok",
        "summary": "Capital One hits mass-market sports demographics using an aggressive, highly comedic multi-celeb campaign featuring Caitlin Clark pushing flat 3% cash back on casual dining and entertainment expenses.",
        "creative": "Human Truth: Financial products are inherently intimidating. By wrapping straightforward rewards mechanics in star-studded, lighthearted sports pop-culture, you completely remove the friction of consumer adoption.",
        "link": "https://www.youtube.com/watch?v=eEMpEfeZnh4"
    },
    {
        "lob": "Business",
        "subBrand": "CSRB",
        "priority": "Tier 1: High Impact",
        "competitor": "Capital One Venture X Business",
        "title": "Enterprise 'Going the Distance' Founder Campaign",
        "channels": "YouTube, LinkedIn Native Video, B2B Podcasts",
        "summary": "Capital One utilizes commercial founder testimonials highlighting immense purchasing power ceilings and double mile accumulation multipliers on scaling operational inventory purchases.",
        "creative": "Human Truth: Business builders see their enterprise as an extension of their personal legacy. They demand severe financial infrastructure that match the absolute scale of their ambitions.",
        "link": "https://www.youtube.com/watch?v=nxQZJb3_B3s"
    },
    {
        "lob": "Consumer",
        "subBrand": "Checking/Savings",
        "priority": "Tier 2: Medium Impact",
        "competitor": "Capital One Retail Banking",
        "title": "'No Fees, No Minimums' Café Footprint Push",
        "channels": "YouTube Premium, Geo-Targeted Mobile Ads, CTV",
        "summary": "Capital One attacks regional retail deposit baselines by pairing zero-fee digital checking accounts with physical, lifestyle-oriented Capital One Café physical community spaces.",
        "creative": "Human Truth: Consumers distrust purely digital faceless code apps, but they loathe stuffy legacy bank branches. Creating a hybrid third-place coffee environment bridges the trust gap cleanly.",
        "link": "https://www.youtube.com/watch?v=psk9qEh-lqM"
    },
    {
        "lob": "Business",
        "subBrand": "Ink",
        "priority": "Tier 2: Medium Impact",
        "competitor": "Ramp Corporate Platforms",
        "title": "'The Anti-Receipt Abyss' Automated Workflows",
        "channels": "B2B News Streams, Meta Video Network, Tech Newsletters",
        "summary": "Fintech business cards run high-frequency digital spots mocking legacy expense filing setups by showcasing automated smartphone receipt matching processing at the point of sale.",
        "creative": "Human Truth: Startup founders and small business operators didn't launch an independent enterprise to spend their nights chasing paper documentation trails. Automation is an operational relief.",
        "link": "https://www.ispot.tv/ad/6AB8/american-express-platinum-exclusive-dining-benefits-song-by-steve-monite"
    }
]

# Set clear system execution date formats on compilation pass
for block in ad_intelligence_vault:
    block['date'] = datetime.today().strftime('%b %d, %Y')

# Safely commit the exact URL objects to the core web loop
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(ad_intelligence_vault, f, indent=2)
print("Data matrix updated with deep-linked visual asset tracking nodes.")
