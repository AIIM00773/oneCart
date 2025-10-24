import re
from .knowns import (
    KNOWN_MARKETPLACE_KEYWORDS,
    KNOWN_BRANDS,
    KNOWN_DEAL_WORDS,
    KNOWN_PRODUCT_STATES,
    KNOWN_PRODUCT_CATEGORIES,
    ExceptionsFromName,
    KNOWN_INTENT_KEYWORDS,
    KNOWN_COUNTRY_KEYWORDS,
    KNOWN_STOP_WORDS,
    KNOWN_AFTER_TOKENS,
    COMMON_PRE_COUNTRY_WORDS,
    KNOWN_PRODUCT_KEYWORDS
)

# ==========================================================
# INITIAL SETUP
# ==========================================================
TOKEN_PATTERN = re.compile(r"\b\w+\b", re.UNICODE)

# Convert all known lists to sets for O(1) lookup
KNOWN_WORDS_SET = set(
    KNOWN_MARKETPLACE_KEYWORDS
    + KNOWN_BRANDS
    + KNOWN_DEAL_WORDS
    + KNOWN_PRODUCT_STATES
    + KNOWN_PRODUCT_CATEGORIES
    + ExceptionsFromName
    + KNOWN_INTENT_KEYWORDS
    + KNOWN_COUNTRY_KEYWORDS
    + KNOWN_STOP_WORDS
    + KNOWN_AFTER_TOKENS
    + COMMON_PRE_COUNTRY_WORDS
)

# Base structure for parsed query
BASE_OBJ = {
    "user_countries_of_preference": [],
    "user_query_intent": [],
    "markets_to_query": [],
    "item_name_tokens": [],
    "item_category_tokens": [],
    "item_brand_tokens": [],
    "item_deals_tokens": [],
    "item_state_tokens": [],
    "item_max_price": None,
}

objIntent ={
  "item": {
    "name": "running shoes",
    "category": "footwear",
    "brand": "Nike",
    "attributes": {
      "color": "red",
      "size": [],
      "gender": [],
      "material": []
    }
  },
  "quantity": 1,
  "purpose": "marathon",
  "time": {
    "raw": "next month",
    "start_date": [],
    "end_date": []
  },
  "location": {
    "type": "store",
    "name": [],
    "address": [],
    "proximity": "near me"
  },
  "price": {
    "min": [],
    "max": 120,
    "currency": "USD"
  },
  "delivery": {
    "required_by": [],
    "method": []
  },
  "urgency": "high",
  "user_notes": [],
  "intent": "buy"
}





# ==========================================================
# TOKEN CLEANING & SPELL CORRECTION
# ==========================================================
def clean_tokens(text: str):
    """Clean text, correct spelling (only unknowns), and tokenize."""
    words = TOKEN_PATTERN.findall(text.lower().strip())
    corrected_words = []

    for word in words:
        if word in KNOWN_WORDS_SET:
            corrected = word  # Keep trusted keywords untouched
        else:
            suggestion = word
            corrected = suggestion if suggestion else word
        corrected_words.append(corrected)
        
    print(str(corrected_words))
    return list(enumerate(corrected_words))

# ==========================================================
#FIND INTENT
# ==========================================================
def find_intent(tokens, key_words, obj):
    """Detect main intent from query."""
    total = len(tokens)
    for idx, token in tokens:
        if token in key_words:
            ratio = total / (idx + 1)
            if ratio > total / 2:  # Appears early in the query
                obj["user_query_intent"].append(token)
                break
    return obj

# ==========================================================
# FIND COUNTRY
# ==========================================================
def find_country(tokens, key_words, obj):
    """Identify mentioned country and possibly product before it."""
    for idx, token in tokens:
        if token in key_words:
            pre_token = tokens[idx - 1][1] if idx > 0 else ""
            pre_pre_token = tokens[idx - 2][1] if idx > 1 else pre_token

            print(f"Checking '{token}' — prev: '{pre_token}', pre-prev: '{pre_pre_token}'")

            # Country confirmation
            if pre_token in COMMON_PRE_COUNTRY_WORDS or pre_pre_token in COMMON_PRE_COUNTRY_WORDS:
                obj["user_countries_of_preference"].append(token)

            # Collect possible product name before country mention
            elif pre_pre_token and pre_pre_token not in KNOWN_WORDS_SET:
                obj["item_name_tokens"].append(pre_pre_token)
    return obj


# ==========================================================
# FIND MARKETPLACE
# ==========================================================
def find_marketplace(tokens, key_words, obj):
    """Extract marketplace mentions."""
    obj["markets_to_query"].extend([token for _, token in tokens if token in key_words])
    return obj





# ==========================================================
#  FIND ITEMS — improved version
# ==========================================================
def find_item_name_tokens(tokens, key_words, obj):
    """
    Extracts item name tokens from user query.
    - Includes words that are likely product identifiers
    - Ignores filler words and known non-item words
    - Keeps multi-word items together when possible
    """
    obj["item_name_tokens"] = []
    item_tokens = []

    for index, token in tokens:
        token_lower = token.lower()

        # If token is in known product list or not in common words → likely product
        if token_lower in key_words or token_lower not in KNOWN_WORDS_SET:
            item_tokens.append(token_lower)
        else:
            print(f"--- Skipped filler word: {token} ---")


    obj["item_name_tokens"].extend(item_tokens)
    return obj




    
    
    
# ==========================================================
# MAIN PARSER
# ==========================================================
def parse_query(query: dict):
    """Main query parsing pipeline."""
    text = query.get("query", "").lower().strip()
    obj = BASE_OBJ.copy()  # faster than deepcopy since base has no nested mutable types

    # Tokenize + correct
    tokens = clean_tokens(text)

    # Run all finders
    obj = find_intent(tokens, KNOWN_INTENT_KEYWORDS, obj)
    obj = find_country(tokens, KNOWN_COUNTRY_KEYWORDS, obj)
    obj = find_marketplace(tokens, KNOWN_MARKETPLACE_KEYWORDS, obj)

    obj = find_item_name_tokens(tokens,KNOWN_PRODUCT_KEYWORDS,obj)

       
    return obj

