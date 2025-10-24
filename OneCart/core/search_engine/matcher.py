



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



# Project-specific known keyword lists
from knowns import (
KNOWN_BRANDS,
KNOWN_PRODUCT_CATEGORIES,
KNOWN_INTENT_KEYWORDS,
KNOWN_PRODUCT_STATES,
KNOWN_MARKETPLACE_KEYWORDS,
KNOWN_COUNTRY_KEYWORDS,
KNOWN_PRODUCT_KEYWORDS
)



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

print(mainfile)

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
all_brands = sorted(set(scraped_brands + KNOWN_BRANDS))
all_categories = sorted(set(scraped_categories + KNOWN_PRODUCT_CATEGORIES))
all_products = sorted(set(scraped_products + KNOWN_PRODUCT_KEYWORDS))


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
intent_patterns = build_patterns(KNOWN_INTENT_KEYWORDS)
state_patterns = build_patterns(KNOWN_PRODUCT_STATES)
market_patterns = build_patterns(KNOWN_MARKETPLACE_KEYWORDS)
country_patterns = build_patterns(KNOWN_COUNTRY_KEYWORDS)

# --- Price and quantity patterns ---
price_patterns = [
    [{"IS_DIGIT": True}, {"LOWER": {"IN": ["kes", "ksh", "shillings", "$", "usd", "dollars"]}}],
    [{"LOWER": {"IN": ["under", "below", "less"]}}, {"IS_DIGIT": True}],
]



quantity_patterns = [
    # -----------------------------
    # Numeric + unit
    # -----------------------------
    [{"IS_DIGIT": True}, {"LOWER": {"IN": [
        "piece", "pieces", "box", "boxes", "pack", "packs",
        "unit", "units", "item", "items", "kg", "kgs",
        "g", "grams", "ml", "liter", "liters", "bottle", "bottles",
        "dozen", "dozens", "pair", "pairs", "set", "sets"
    ]}}],

    # -----------------------------
    # Written number + unit (e.g. "three boxes", "two pairs")
    # -----------------------------
    [{"LOWER": {"IN": [
        "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve"
    ]}}, {"LOWER": {"IN": [
        "piece", "pieces", "box", "boxes", "pack", "packs",
        "unit", "units", "item", "items", "kg", "kgs", "g",
        "grams", "ml", "liter", "liters", "bottle", "bottles",
        "pair", "pairs", "set", "sets", "dozen", "dozens"
    ]}}],

    # -----------------------------
    # Bulk expressions (e.g. "pack of 6", "set of 3")
    # -----------------------------
    [{"LOWER": {"IN": ["pack", "packs", "set", "sets", "bundle", "bundles"]}},
     {"LOWER": "of"},
     {"IS_DIGIT": True}],

    # -----------------------------
    # Special quantity words (approximation)
    # -----------------------------
    [{"LOWER": {"IN": ["a few", "an", "few", "couple", "some", "several", "many"]}},
     {"LOWER": {"IN": ["pieces", "items", "packs", "boxes", "units", "pairs", "sets"]}}],

    # -----------------------------
    #Expressions like "a dozen", "half dozen", "one dozen"
    # -----------------------------
    [{"LOWER": {"IN": ["a", "one", "half"]}}, {"LOWER": "dozen"}],
]





# ===========================
# Register All Patterns to Matcher
# ===========================
matcher.add("BRAND", brand_patterns)
matcher.add("CATEGORY", category_patterns)
matcher.add("PRODUCT", product_patterns)
matcher.add("INTENT", intent_patterns)
matcher.add("STATE", state_patterns)
matcher.add("MARKET", market_patterns)
matcher.add("COUNTRY", country_patterns)
matcher.add("PRICE", price_patterns)
matcher.add("QUANTITY", quantity_patterns)

print(f"✅ Matcher built with {len(brand_patterns)} brands, {len(category_patterns)} categories, and {len(product_patterns)} products.")





