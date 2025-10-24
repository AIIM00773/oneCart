


import re

import copy 
# ==========================================================
# INITIAL SETUP
# ==========================================================
TOKEN_PATTERN = re.compile(r"\b\w+\b", re.UNICODE)




objIntent = {
    "intents": ["buy"],  # could be ["compare", "find", "track"]
    "items": [
        {
            "name": [],
            "category": [],
            "brand": [],
            "alternative_brands": [],
            "attributes": {
                "color": [],
                "size": [],
                "gender": [],
                "material": [],
                "custom": {}  # flexible slot for unexpected attrs like "arch support" or "eco-friendly"
            },
            "condition": [],  # "used", "refurbished", or "new" 
            "quantity": 1,
            "price": {
                "min": [],
                "max": 120,
                "approx": False,  # True if user says “around $100”
                "currency": ["KESH"]
            }
        }
    ],
    "purpose": [],
    "User_of_the_Item": {
        "gender": ["all"] , # male female 
        "age_group": ["all"], #child , young adult , Adult
    
    },
    "timestamps": {
        "raw": [],
        "start_date": [],
        "end_date": []
    },
    "market": {
        "type": [ "online" ],  # "store", "online", "any"
        "name": [],
        "address": [],
        "proximity": ["any"]   # near me  ...
    },
    "delivery": {
        "aproximation_in_hours":[24],
        "method": ["shipping"],  # ["pickup", "shipping", "express"]
        "speed_preference": ["normal"] # first
    },
    "urgency": "high",
    "offers": {
        "on_sale": False,
        "discount_only": False,
        "deals": False,
        "Trending": False,
        "Featured": False
    },
    "user_notes": [],
    "meta": {
        "query_raw": "",
        "language": "en",
        "confidence": 0.0,
        "source": "text"  # could also be "voice" or "image"
    }
}








# ==========================================================
# TOKEN CLEANING & SPELL CORRECTION
# ==========================================================
def clean_tokens(text: str):
    wordslist = list(enumerate(TOKEN_PATTERN.findall(text.lower().strip())))
    if wordslist and len(wordslist) > 0:
        enumaratedTokens = wordslist
    #print(f"\n{enumaratedTokens}\n")
    
    return(enumaratedTokens)



    
    
# ==========================================================
# MAIN PARSER
# ==========================================================
def parse_query(query: dict):
    """Main query parsing pipeline."""
    text = query.get("query", "").lower().strip()
    clean_tokens(text)
    
    obj = copy.deepcopy(objIntent)  # faster than deepcopy since base has no nested mutable types
          
    return (obj,clean_tokens(text)) 

