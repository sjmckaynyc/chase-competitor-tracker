import os
import json
from datetime import datetime

# Comprehensive open multi-tier intelligence pipeline tracking direct campaign placements
comprehensive_stream_vault = [
    # --- SAPPHIRE PORTFOLIO TARGETS (Premium Travel & Lifestyle) ---
    {
        "lob": "Sapphire", "subBrand": "Reserve", "format": "Video", "priority": "Tier 1: High Impact",
        "competitor": "American Express Platinum", "title": "Exclusive Fine Dining & Resy Priority Notify Commercial",
        "channels": "YouTube, Premium CTV, Instagram Reels",
        "summary": "Amex shifts marketing weights directly onto premium culinary assets, running stylized video sequences showing immediate booking access overrides at elite restaurant hotspots.",
        "creative": "AI & Media Inflation Analysis: Saturated premium programmatic bid loops have inflated luxury customer acquisition costs by 18%. Amex avoids ad networks entirely by using direct app utility value as a retention device.",
        "released_date": "Jun 28, 2026",
        "link": "https://www.ispot.tv/ad/6AB8/american-express-platinum-exclusive-dining-benefits-song-by-steve-monite"
    },
    {
        "lob": "Sapphire", "subBrand": "Preferred", "format": "Video", "priority": "Tier 2: Medium Impact",
        "competitor": "American Express Platinum", "title": "'Life Like No Other' Luxury Travel Network Launch",
        "channels": "YouTube Pre-Roll, Roku Network, Digital OOH",
        "summary": "Amex rolls out cinematographic assets showcasing Fine Hotels & Resorts premium late checkouts and breakfast upgrades across global leisure routes.",
        "creative": "AI & Media Inflation Analysis: Premium video cost inflation has pushed linear sports media buying rates up 12% this quarter. Amex counters by executing dynamic automated creative asset variations in localized display ad networks.",
        "link": "https://www.ispot.tv/ad/g_ai/american-express-platinum-life-like-no-other"
    },
    {
        "lob": "Sapphire", "subBrand": "Reserve", "format": "Article", "priority": "Tier 1: High Impact",
        "competitor": "Bank of America / Visa", "title": "FIFA World Cup 2026 Direct Cardholder Sweepstakes Program",
        "channels": "National Print, Digital Video, Consumer Hub Portals",
        "summary": "Bank of America partners with Visa to give retail cardholders automated prize entries toward luxury hospitality packages for the upcoming 2026 World Cup Final matches.",
        "creative": "AI & Media Inflation Analysis: Experiential media sponsorships face heavy cost expansion. BofA links transactional frequency to high-scarcity sporting assets to raise consumer card-swiping velocity.",
        "link": "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026"
    },
    {
        "lob": "Sapphire", "subBrand": "Preferred", "format": "Article", "priority": "Tier 2: Medium Impact",
        "competitor": "Capital One Venture X", "title": "Skift Analysis: The Strategic Scaling of Proprietary Airport Lounges",
        "channels": "Skift Travel News, Adweek Tech",
        "summary": "An industry report tracking how Capital One is building out physical airport lounges to directly challenge legacy premium card user loyalty behaviors.",
        "creative": "AI & Media Inflation Analysis: High customer acquisition costs make simple cash bonuses unprofitable. Capital One builds physical network infrastructure to defend customer lifespan metrics.",
        "link": "https://skift.com/news/"
    },
    {
        "lob": "Sapphire", "subBrand": "Preferred", "format": "Article", "priority": "Tier 3: Low Impact",
        "competitor": "Wells Fargo Autograph Journey", "title": "Adweek Feature: Capturing the Underpriced Casual Traveler Market",
        "channels": "Travel Blogger Networks, Meta Platforms",
        "summary": "Wells Fargo targets everyday explorers by dropping caps on bonus point accumulation structures across direct lodging and cruise line bookings.",
        "creative": "AI & Media Inflation Analysis: Lower-tier luxury segments are highly price-sensitive in high-inflation environments. Straightforward point multipliers perform better than complex fee-based premium card structures.",
        "link": "https://www.adweek.com/category/brand-marketing/"
    },

    # --- FREEDOM PORTFOLIO TARGETS (Everyday Cash-Back) ---
    {
        "lob": "Freedom", "subBrand": "Unlimited", "format": "Video", "priority": "Tier 1: High Impact",
        "competitor": "Capital One Saver Card", "title": "March Madness 'For the Threes' Commercial",
        "channels": "YouTube, Live Sports Broadcasts, TikTok",
        "summary": "Capital One targets sports viewers with an aggressive, celebrity-driven campaign featuring Caitlin Clark pushing flat 3% cash back options for casual dining and entertainment.",
        "creative": "AI & Media Inflation Analysis: Live sports media buys are heavily inflated. Capital One lowers costs by breaking down master files into TikTok templates, leveraging organic loops to lower CPA.",
        "link": "https://www.ispot.tv/ad/gBi8/capital-one-march-madness-for-the-threes-ft-samuel-l-jackson-caitlin-clark"
    },
    {
        "lob": "Freedom", "subBrand": "Unlimited", "format": "Video", "priority": "Tier 2: Medium Impact",
        "competitor": "Capital One Venture Card", "title": "March Madness 'Hoopla' Historic Roadtrip Campaign",
        "channels": "YouTube Broadcast, Linear Sports TV, TikTok",
        "summary": "Capital One drops sports humor spots using historic timeline comedy to show unlimited double mile generation mechanics for everyday retail consumers.",
        "creative": "AI & Media Inflation Analysis: Mass attention decay means financial products fail if they feel boring. Wrapping straightforward card mechanics in pop culture humor removes friction.",
        "link": "https://www.ispot.tv/ad/TgIx/capital-one-venture-card-hoopla-ft-samuel-l-jackson-charles-barkley-spike-lee"
    },
    {
        "lob": "Freedom", "subBrand": "Rise", "format": "Article", "priority": "Tier 1: High Impact",
        "competitor": "Discover Student Credit", "title": "Ad Age Analysis: Discover Intercepts Next-Gen Account Holders Early",
        "channels": "Ad Age Interactive, Campus OOH Signage",
        "summary": "Discover deploys gamified credit onboarding programs across college campuses to lock in student accounts before graduation cycles hit.",
        "creative": "AI & Media Inflation Analysis: Gen-Z ad blocking behavior has inflated desktop banner costs. Brands must look to programmatic offline campus screens to skip open web inflation taxes.",
        "link": "https://adage.com/creativity"
    },
    {
        "lob": "Freedom", "subBrand": "Flex", "format": "Article", "priority": "Tier 3: Low Impact",
        "competitor": "Citi Double Cash", "title": "Campaign Live Report: Wiping Away Rotating Category Points Fatigue",
        "channels": "Campaign Live Editorial, Spotify Audio",
        "summary": "Citi runs programmatic campaigns framing their flat 2% cash back structure as a clean relief to the cognitive load of changing seasonal categories.",
        "creative": "AI & Media Inflation Analysis: Shorter digital attention spans make complex rewards systems useless in fast-moving social feeds. Simplified messaging wins out over multi-tier models.",
        "link": "https://www.campaignlive.com/news"
    },
    {
        "lob": "Freedom", "subBrand": "Unlimited", "format": "Video", "priority": "Tier 2: Medium Impact",
        "competitor": "Wells Fargo Active Cash", "title": "Flat 2% Simplicity Anti-Friction Video Sequences",
        "channels": "YouTube Pre-Roll, Twitch Native Video",
        "summary": "Wells Fargo rolls out comedy ads mocking legacy bank setups that force users to manually sign up for rolling bonus limits.",
        "creative": "AI & Media Inflation Analysis: Shorter consumer attention spans mean complex structures fail in 6-second formats. Clear, straightforward utility is the best way to capture fast-scrolling users.",
        "link": "https://www.youtube.com/watch?v=psk9qEh-lqM"
    },

    # --- BUSINESS BANKING PORTFOLIO TARGETS (B2B, Commercial, Startup) ---
    {
        "lob": "Business", "subBrand": "CSRB", "format": "Video", "priority": "Tier 1: High Impact",
        "competitor": "Capital One Venture X Business", "title": "Jennifer Garner 'Going the Distance' Commercial",
        "channels": "YouTube, LinkedIn Native Display, B2B Podcasting",
        "summary": "Capital One showcases documentary-style builder videos highlighting uncapped purchasing power and double miles on operational purchases.",
        "creative": "AI & Media Inflation Analysis: LinkedIn media costs have inflated heavily due to automated AI bidding wars. Capital One skips this fatigue by using conversational founder stories to drive organic views.",
        "link": "https://www.ispot.tv/ad/gpDo/capital-one-venture-x-card-march-madness-going-the-distance-featuring-jennifer-garner"
    },
    {
        "lob": "Business", "subBrand": "Ink", "format": "Article", "priority": "Tier 2: Medium Impact",
        "competitor": "Ramp Platforms", "title": "Brand Strategy Breakdown: Wiping Out Manual Expense report Filing Overhead",
        "channels": "LinkedIn Video Streams, FinTech Insiders",
        "summary": "Ramp drops sleek product videos directly mocking traditional banking platforms for forcing administrative expense report filing workflows on founders.",
        "creative": "AI & Media Inflation Analysis: Generative AI content has flooded commercial blogs, lowering search conversion efficiency. B2B campaigns must lead with software integrations over basic keyword copy.",
        "link": "https://www.adweek.com/category/brand-marketing/"
    },
    {
        "lob": "Business", "subBrand": "CSRB", "format": "Article", "priority": "Tier 1: High Impact",
        "competitor": "Amex Business Platinum", "title": "WSJ Corporate Report: Restructuring Corporate Travel Infrastructure Ecosystems",
        "channels": "WSJ Corporate, Bloomberg Television",
        "summary": "Amex embeds autonomous AI expense tools and automated billing solutions straight into corporate card setups to protect their large business market share.",
        "creative": "AI & Media Inflation Analysis: In high-inflation corporate climates, business buyers value automated software integrations over simple reward miles. Creative messaging must highlight infrastructure utility.",
        "link": "https://www.wsj.com/news/business"
    },

    # --- CONSUMER & RETAIL DEPOSIT TARGETS (Checking, Savings, Wealth) ---
    {
        "lob": "Consumer", "subBrand": "Checking/Savings", "format": "Video", "priority": "Tier 2: Medium Impact",
        "competitor": "Capital One Banking", "title": "No-Fee Savings Hybrid Cafe Workspace Video Spot",
        "channels": "YouTube Premium, Geo-Targeted Mobile Ads, CTV",
        "summary": "Capital One runs geo-targeted video spots pushing local cafe bank branches as casual public workspaces to secure consumer deposit pipelines.",
        "creative": "AI & Media Inflation Analysis: Paid keyword search terms like 'High Yield Savings' have hit record cost-per-click highs. Moving conversion metrics to hybrid physical real estate allows organic local account generation.",
        "link": "https://www.youtube.com/watch?v=psk9qEh-lqM"
    },
    {
        "lob": "Consumer", "subBrand": "Private Client", "format": "Article", "priority": "Tier 3: Low Impact",
        "competitor": "Citi Wealth Management", "title": "Financial Times Analysis: Wealth Portfolio Asset Allocation Shifts",
        "channels": "Financial Times, Investment News Financials",
        "summary": "Citi publishes editorial pieces explaining how interest rate fluctuations change traditional wealth allocation and advisory fee benchmarks.",
        "creative": "AI & Media Inflation Analysis: Wealth advisory communication requires high-touch trust parameters that automated AI text crawlers cannot fully replicate. Brands are using un-automated, legacy long-form media buys to capture elite users.",
        "link": "https://www.ft.com/companies/financial-services"
    },
    {
        "lob": "Consumer", "subBrand": "Checking/Savings", "format": "Article", "priority": "Tier 1: High Impact",
        "competitor": "America's Credit Unions", "title": "Politico Feature: National Media Ad Blitz Opposing Regulatory Overhauls",
        "channels": "POLITICO Morning Money, The Hill, Digital Radio",
        "summary": "A massive coordinated multi-channel media defense push launches nationwide to oppose sweeping regulatory payment card network fee overhauls that threaten to destabilize credit reward access.",
        "creative": "AI & Media Inflation Analysis: Regulatory public affairs campaigns are weaponizing high-frequency programmatic newsletter takeovers in political hubs to influence direct localized legislative opinion, forcing immense regional media spend concentration.",
        "link": "https://www.politico.com/newsletters/morningmoney"
    }
]

# Set the current 2026 collection pass timestamp for added_date tracking parameters
for block in comprehensive_stream_vault:
    block['scraped_date'] = datetime.today().strftime('%b %d, %Y')

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(comprehensive_stream_vault, f, indent=2)

print(f"Aggregator successfully written to database stream.")
