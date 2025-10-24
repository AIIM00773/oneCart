



# ===========================
# Imports
# ===========================

# NLP & Matcher
import spacy
from spacy.matcher import Matcher

# Data 
import time
import random
import json, glob





# ===========================
# Load NLP Model
# ===========================
nlp = spacy.load("en_core_web_sm")



# ===========================
# Load Training Data from JSON from CRAWLERS DIR 
# ===========================

files = glob.glob("CRAWLERS/*.json")

print(len(files))

mainfile = files[0]


with open(mainfile, "r") as file:
    TrainingMarketData1 = json.load(file)



# ===========================
# Initialize Matcher
# ===========================
matcher = Matcher(nlp.vocab)


# Helper function to clean lowercase and ensure uniqueness
def unique_clean(values):
    return sorted(set(v.strip().lower() for v in values if v and v != "N/A"))


# --- Extract dynamic keywords from scraped data ---
scraped_brands = unique_clean([item["product_Brand"] for item in TrainingMarketData1])

scraped_categories = unique_clean( [cat for item in TrainingMarketData1 for cat in item["product_Category"].split(",")] )

scraped_products = unique_clean([item["product_Name"] for item in TrainingMarketData1])




# --- Combine scraped + known data ---

all_brands = sorted(set(scraped_brands))
all_categories = sorted(set(scraped_categories))
all_products = sorted(set(scraped_products ))




# ===========================
# Define Pattern Builders
# ===========================
def build_patterns(words):
    """Return list of patterns for lowercase token matches."""
    return [[{"LOWER": word}] for word in words if word and len(word.split()) <= 3]



# --- Build patterns ---
brand_patterns = build_patterns(all_brands)
category_patterns = build_patterns(all_categories)
product_patterns = build_patterns(all_products)








IntentWords = [
    "buy", "purchase", "order", "get", "shop", "acquire", "grab",    "find", "search", "look for", "show me", "browse", "recommend", "suggest", "discover", "explore", "see"
    "book", "checkout", "pick up", "reserve", "find","show",  "locate",  "get",       "search",   "look for", "browse",    "explore",  "check"   
    ]




intent_patterns = build_patterns(sorted(set(IntentWords)))



condition = [
    "new", "used", "refurbished", "second hand", "brand new", "latest",
    "old model", "previous version","best", "top", "popular", "trending", "recommended", "high rated", "trusted", "reliable", "favorite"
]



state_patterns = build_patterns(sorted(set(condition))) 


location = [ "near me", "close to", "in", "at", "around", "store", "shop", "mall", "local", "online", "website", "retailer", "branch" ]


timeIntentWords = [ "today", "tomorrow", "next week", "next month", "weekend", "holiday", "before", "after", "later", "now", "soon", "asap", "urgent"]



kenya_marketplaces = [ "Jumia Kenya","Kilimall","Masoko","Sky.Garden","Jiji ", "BidorBuy Kenya","PigiaMe","Taimba","Shopit Kenya","Avechi","Zuri","Zumi","Autochek Kenya","Cheki Kenya","Twiga Foods","Naivas Online",
    "Carrefour Kenya Online","MallforAfrica Kenya","Pigiame","Text Book Centre Online","Greenbell Online Market"
]

market_patterns = build_patterns(sorted(set(kenya_marketplaces)))


_countries = ["Kenya","Tanzania","Uganda","Rwanda","Ethiopia","Somalia","South Sudan","Burundi","Eritrea","Djibouti","Nigeria","South Africa","Egypt","Kenya","Ethiopia","Ghana","Morocco","Algeria","Tanzania","Uganda",
        "Tunisia","Senegal","Angola","Ivory Coast","Sudan","Rwanda","United States","China","India","United Kingdom","Germany","France","Japan","Canada","Brazil","Australia","Italy","South Korea","Russia","Mexico","Spain",
        "Saudi Arabia","Netherlands","Turkey","Switzerland","Sweden"
    ]


country_patterns = build_patterns(sorted(set(_countries)))




common_colors = ["red","blue","green","yellow","black","white","gray","orange","purple","pink","brown","beige","cyan","magenta","maroon","navy","teal","olive","violet","gold","silver","cream","turquoise","indigo",
 "lime","coral","peach","tan", "chocolate","burgundy"
]



color_patterns = build_patterns(sorted(set(common_colors)))






price_patterns = [

    # --- Numeric followed by currency ---
    # Examples: "1200 USD", "500 Ksh", "150 dollars"
    [
        {"IS_DIGIT": True}, 
        {"LOWER": {"IN": ["kes", "ksh", "sh", "shillings", "usd", "$", "dollar", "dollars"]}}
    ],

    # --- Currency followed by numeric (less common) ---
    # Examples: "$150", "USD 1200"
    [
        {"LOWER": {"IN": ["kes", "ksh", "sh", "shillings", "usd", "$", "dollar", "dollars"]}},
        {"IS_DIGIT": True}
    ],

    # --- Approximate / comparative prices ---
    # Examples: "under 1500 Ksh", "around 500 dollars"
    [
        {"LOWER": {"IN": ["under", "above", "around", "about", "less", "more"]}, "OP": "?"},
        {"IS_DIGIT": True},
        {"LOWER": {"IN": ["kes", "ksh", "sh", "shillings", "usd", "$", "dollar", "dollars"]}, "OP": "?"}
    ],
]










condition_patterns = [

    # ------------------------------------------------------
    # Basic single-word conditions
    # e.g. "new", "used", "refurbished", "sealed"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": [
            "new", "used", "refurbished", "reconditioned", "repaired",
            "open", "sealed", "faulty", "defective", "broken", "old"
        ]}},
    ],

    # ------------------------------------------------------
    # Common 2-word conditions
    # e.g. "brand new", "second hand", "open box", "factory sealed"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": [
            "brand", "second", "factory", "open", "pre", "fairly"
        ]}},
        {"LOWER": {"IN": [
            "new", "hand", "sealed", "box", "owned", "used"
        ]}},
    ],

    # ------------------------------------------------------
    # Phrases starting with "in" or "with" + adjective + condition noun
    # e.g. "in good condition", "in perfect working condition"
    # ------------------------------------------------------
    [
        {"LOWER": "in"},
        {"LOWER": {"IN": [
            "good", "excellent", "perfect", "great", "poor", "fair", "working", "mint"
        ]}},
        {"LOWER": {"IN": [
            "condition", "shape", "order"
        ]}, "OP": "?"},
    ],

    # ------------------------------------------------------
    # Condition with degree modifier
    # e.g. "like new", "almost new", "barely used"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": [
            "like", "almost", "barely", "nearly", "slightly", "gently", "fairly"
        ]}},
        {"LOWER": {"IN": ["new", "used", "worn"]}},
    ],

    # ------------------------------------------------------
    # “Pre-owned”, “well maintained”, “lightly used”, etc.
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": [
            "pre", "lightly", "well"
        ]}},
        {"LOWER": {"IN": [
            "owned", "used", "maintained", "kept"
        ]}},
    ],

    # ------------------------------------------------------
    # Extended forms like “factory refurbished”, “professionally repaired”
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": [
            "factory", "professionally", "manufacturer", "expertly"
        ]}},
        {"LOWER": {"IN": [
            "refurbished", "repaired", "reconditioned"
        ]}},
    ],

    # ------------------------------------------------------
    # Negative or warning condition phrases
    # e.g. "not working", "for parts", "needs repair"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["not", "for", "needs", "requires"]}},
        {"LOWER": {"IN": ["working", "parts", "repair", "fixing", "replacement"]}},
    ],

    # ------------------------------------------------------
    # Auction / resale-related conditions
    # e.g. "as is", "sold as is"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["as", "sold"]}},
        {"LOWER": "is"},
    ],

    # ------------------------------------------------------
    # Extra nuanced forms: “unused”, “brand-new”, “pre-owned”
    # (with hyphenated or compound possibilities)
    # ------------------------------------------------------
    [
        {"TEXT": {"REGEX": r"^(brand-new|pre-owned|unused|like-new|factory-sealed)$"}}
    ],
]









rating_patterns = [

    # ------------------------------------------------------
    # Numeric or decimal + "star"/"stars"
    # e.g. "4 stars", "4.5 stars", "5 star", "3-star"
    # ------------------------------------------------------
    [
        {"TEXT": {"REGEX": r"^\d+(\.\d+)?$"}},
        {"LOWER": {"IN": ["star", "stars", "⭐"]}},
    ],
    [
        {"TEXT": {"REGEX": r"^\d(\.\d)?-star$"}},  # e.g. "5-star", "4.5-star"
    ],

    # ------------------------------------------------------
    # Written number + "star"/"stars"
    # e.g. "five stars", "four star rated"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": [
            "one", "two", "three", "four", "five"
        ]}},
        {"LOWER": {"IN": ["star", "stars"]}},
    ],

    # ------------------------------------------------------
    # "rated" expressions
    # e.g. "rated 5 stars", "rated four star", "rated highly"
    # ------------------------------------------------------
    [
        {"LOWER": "rated"},
        {"TEXT": {"REGEX": r"^\d+(\.\d+)?$"}, "OP": "?"},
        {"LOWER": {"IN": ["star", "stars"]}, "OP": "?"},
    ],
    [
        {"LOWER": "rated"},
        {"LOWER": {"IN": ["highly", "poorly", "well", "badly"]}},
    ],

    # ------------------------------------------------------
    # Quality adjectives often used for rating intent
    # e.g. "top rated", "best rated", "highly rated", "most reviewed"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["top", "best", "highly", "most"]}},
        {"LOWER": {"IN": ["rated", "reviewed", "review", "loved"]}},
    ],

    # ------------------------------------------------------
    # Explicit "rating" expressions
    # e.g. "4.8 rating", "excellent rating", "customer rating"
    # ------------------------------------------------------
    [
        {"TEXT": {"REGEX": r"^\d+(\.\d+)?$"}, "OP": "?"},
        {"LOWER": {"IN": ["rating", "ratings"]}},
    ],
    [
        {"LOWER": {"IN": [
            "excellent", "good", "poor", "average", "great", "amazing",
            "superb", "bad", "terrible", "decent"
        ]}},
        {"LOWER": {"IN": ["rating", "ratings", "reviews", "review"]}, "OP": "?"},
    ],

    # ------------------------------------------------------
    # Customer satisfaction phrases
    # e.g. "highly reviewed", "customer favorite", "top choice"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["customer", "users", "buyers", "clients"]}},
        {"LOWER": {"IN": ["favorite", "favourite", "choice", "rated", "reviewed", "pick"]}},
    ],

    # ------------------------------------------------------
    # Star emoji or symbolic pattern
    # e.g. "⭐⭐⭐⭐⭐", "★★★★★"
    # ------------------------------------------------------
    [
        {"TEXT": {"REGEX": r"^[⭐★]{2,}$"}},
    ],
]













seller_patterns = [

    # ------------------------------------------------------
    # Generic seller terms
    # e.g. "seller", "vendor", "merchant", "shop", "store"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["seller", "sellers", "vendor", "vendors", "merchant", "merchants", "retailer", "retailers", "dealer", "dealers", "shop", "shops", "store", "stores", "distributor", "distributors", "supplier", "suppliers"]}},
    ],

    # ------------------------------------------------------
    # "sold by" or "provided by" phrases
    # e.g. "sold by Nike", "provided by Jumia", "offered by vendor"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["sold", "provided", "offered", "supplied", "distributed"]}},
        {"LOWER": "by"},
        {"IS_ALPHA": True, "OP": "+"},  # seller name / brand
    ],

    # ------------------------------------------------------
    # Shop or store name mentions
    # e.g. "from Jumia", "at Carrefour", "through Amazon"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["from", "at", "through", "via"]}},
        {"IS_TITLE": True, "OP": "+"},  # brand/seller name
    ],
    [
        {"LOWER": {"IN": ["available", "found", "listed"]}},
        {"LOWER": "on"},
        {"IS_TITLE": True, "OP": "+"},  # e.g. “available on Kilimall”
    ],

    # ------------------------------------------------------
    # Seller reference with pronouns
    # e.g. "their store", "his shop", "her boutique"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["their", "his", "her", "our", "my"]}},
        {"LOWER": {"IN": ["shop", "store", "boutique", "outlet", "page", "account"]}},
    ],

    # ------------------------------------------------------
    # Location + seller pattern
    # e.g. "local shops near me", "stores in Nairobi"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["store", "stores", "shop", "shops", "seller", "vendors", "outlets"]}},
        {"LOWER": {"IN": ["near", "around", "in", "within"]}},
        {"IS_ALPHA": True, "OP": "+"},
    ],

    # ------------------------------------------------------
    # Brand + seller
    # e.g. "official Samsung store", "Apple reseller", "authorized dealer"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["official", "authorized", "verified", "trusted", "certified"]}},
        {"LOWER": {"IN": ["seller", "vendor", "store", "dealer", "reseller", "shop"]}},
    ],
    [
        {"IS_TITLE": True},  # Brand name like "Apple"
        {"LOWER": {"IN": ["store", "shop", "reseller", "dealer", "vendor"]}},
    ],

    # ------------------------------------------------------
    # Seller comparison or quality
    # e.g. "best sellers", "top rated vendor", "trusted seller"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["best", "top", "trusted", "verified", "popular", "leading"]}},
        {"LOWER": {"IN": ["seller", "sellers", "vendors", "shops", "stores"]}},
    ],
    [
        {"LOWER": {"IN": ["seller", "vendor", "shop", "store"]}},
        {"LOWER": {"IN": ["rating", "reviews", "trust", "score"]}, "OP": "?"},
    ],

    # ------------------------------------------------------
    # Seller-related questions
    # e.g. "who sells Nike shoes", "which seller has this", "where can I buy from"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["who", "which", "where"]}},
        {"LOWER": {"IN": ["sell", "sells", "selling", "vendor", "seller", "shop", "store", "has", "offers"]}},
    ],
    [
        {"LOWER": {"IN": ["can", "do", "does"]}},
        {"LOWER": {"IN": ["you", "they", "any", "this", "that"]}, "OP": "?"},
        {"LOWER": {"IN": ["sell", "offer", "supply", "provide"]}},
        {"IS_ALPHA": True, "OP": "*"},
    ],

    # ------------------------------------------------------
    # Platform references (marketplace context)
    # e.g. "third-party sellers", "official store on Jumia"
    # ------------------------------------------------------
    [
        {"LOWER": {"IN": ["third", "third-party", "independent"]}},
        {"LOWER": {"IN": ["seller", "vendor", "merchant"]}},
    ],
    [
        {"LOWER": {"IN": ["official", "flagship", "brand"]}},
        {"LOWER": {"IN": ["store", "shop", "page"]}},
        {"LOWER": "on", "OP": "?"},
        {"IS_TITLE": True, "OP": "?"},  # e.g. “official store on Jumia”
    ],

]















location_patterns = [

    # ---------------------------------------------------------
    # Generic location indicators (e.g. "near me", "around me", "close by")
    # ---------------------------------------------------------
    [
        {"LOWER": {"IN": ["near", "around", "around me", "close", "closeby", "nearby", "closeby"]}},
        {"LOWER": {"IN": ["me", "here", "my", "location", "area"]}, "OP": "?"},
    ],

 

    # ---------------------------------------------------------
    # Named location keywords (e.g. "deliver to my address", "pickup point in town")
    # ---------------------------------------------------------
    [
        {"LOWER": {"IN": ["deliver", "ship", "send", "take"]}},
        {"LOWER": {"IN": ["to", "at"]}},
        {"LOWER": {"IN": ["home", "house", "address", "office", "school", "town", "location", "place", "market", "mall"]}, "OP": "?"},
        {"IS_ALPHA": True, "OP": "*"},
    ]
    
    
]

    
    
    
    
currency_patterns = [

    # ---------------------------------------------------------
    # Currency symbols and textual forms (e.g. "$", "Ksh", "shillings", "dollars")
    # ---------------------------------------------------------
    [
        {"TEXT": {"IN": [
            "$", "€", "£", "₦", "₵", "₹", "¥", "₽", "₩", "₺", 
            "Ksh", "ksh", "KES", 
            "shilling", "shillings", "dollar", "dollars", "euro", "euros", "pound", "pounds"
        ]}},
    ],

]









# ========================================
# Register All Patterns to Matcher
# ========================================

# Helper: safely add patterns
def add_patterns(matcher, name, patterns):
    """Add patterns to matcher with safety checks and flexibility."""
    if name not in matcher:
        matcher.add(name, patterns)
    else:
        print(f"[INFO] Matcher '{name}' already exists, skipping duplicate registration.\n")

# ----------------------------------------------------
# 1️⃣ Core Product Information Entities
# ----------------------------------------------------
add_patterns(matcher, "BRAND", brand_patterns)         
add_patterns(matcher, "CATEGORY", category_patterns)   
add_patterns(matcher, "PRODUCT", product_patterns)     

# ----------------------------------------------------
# 2️⃣ Contextual Entities (Market, Country, State)
# ----------------------------------------------------
add_patterns(matcher, "MARKET", market_patterns)        
add_patterns(matcher, "COUNTRY", country_patterns)     
add_patterns(matcher, "STATE", state_patterns)          

# ----------------------------------------------------
# 3️⃣ User Intent & Action Detection
# ----------------------------------------------------
add_patterns(matcher, "INTENT", intent_patterns)        
add_patterns(matcher, "PRICE", price_patterns)          
add_patterns(matcher, "COLOR", color_patterns)          



# ----------------------------------------------------
# 4️⃣ Descriptive & Qualitative Attributes
# ----------------------------------------------------

add_patterns(matcher, "CONDITION", condition_patterns)  
add_patterns(matcher, "RATING", rating_patterns)        
add_patterns(matcher, "CURRENCY", currency_patterns)     


print(f"✅ Matcher built with {len(brand_patterns)} brands, {len(category_patterns)} categories, and {len(product_patterns)} products.")





