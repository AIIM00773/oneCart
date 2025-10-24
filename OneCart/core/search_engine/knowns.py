


# --- Comprehensive Popular Brands (Kenya & International) ---
# Covers electronics, fashion, appliances, groceries, beauty, baby, and more
KNOWN_BRANDS = [
    # --- Electronics & Tech ---
    "samsung", "infinix", "tecno", "itel", "realme", "xiaomi", "oppo", "iphone", "apple",
    "nokia", "lg", "hisense", "sony", "tcl", "lenovo", "hp", "dell", "asus", "acer",
    "huawei", "oraimo", "anker", "vivo", "oneplus", "panasonic", "philips", "jbl",
    "canon", "nikon", "go pro", "toshiba", "sandisk", "seagate", "western digital",
    "beats", "logitech", "anker", "mi", "amazon basics", "google", "bosch",
    
    # --- Home Appliances ---
    "armco", "ramtons", "bruhm", "mika", "von", "syinix", "bosch", "panasonic",
    "haier", "sharp", "blueflame", "whirlpool", "hotpoint", "kenwood", "scarlett",
    "delonghi", "black+decker", "philco", "beko", "defy", "electrolux",
    
    # --- Fashion & Footwear ---
    "nike", "adidas", "puma", "reebok", "new balance", "skechers", "vans",
    "timberland", "converse", "fila", "under armour", "asics", "crocs", "ugg",
    "zara", "hm", "shein", "gucci", "prada", "louis vuitton", "balenciaga",
    "dior", "versace", "burberry", "levis", "diesel", "lacoste", "tommy hilfiger",
    "uniqlo", "superdry", "off-white", "dr martens", "bata", "clarks",
    
    # --- Baby & Kids ---
    "pampers", "huggies", "molfix", "johnsons", "nestle", "cerelac", "chicco",
    "avent", "nuk", "mothercare", "babyshop", "gerber", "pigeon", "pureborn",
    
    # --- Beauty & Personal Care ---
    "nivea", "dove", "vaseline", "olay", "garnier", "loreal", "maybelline",
    "mac", "revlon", "clinique", "the ordinary", "cerave", "neutrogena",
    "ponds", "simple", "palmers", "sheamoisture", "tresemme", "colgate",
    "oral b", "gillette", "old spice", "axe", "fa", "rexona", "sensodyne",
    
    # --- Food & Groceries ---
    "brookside", "fresha", "kenafric", "coca cola", "pepsi", "fanta", "sprite",
    "delmonte", "kenpoly", "sunlight", "omo", "aerial", "tropical heat", "unga",
    "daima", "menengai", "protex", "lifebuoy", "dettol", "kenchic", "jubilee",
    
    # --- Automotive & Tools ---
    "toyota", "nissan", "honda", "mazda", "subaru", "mitsubishi", "bmw",
    "mercedes", "audi", "ford", "bosch", "castrol", "shell", "total",
    "motul", "goodyear", "michelin", "pirelli", "dunlop", "yokohama",
    
    # --- Furniture & Home Living ---
    "royal", "ashley", "ikea", "toto", "supafoam", "melamine", "tupperware",
    "ramtons home", "mika home", "bruhm home", "deluxe", "household essentials",
    
    # --- Sports & Outdoor ---
    "decathlon", "speedo", "north face", "patagonia", "columbia", "reebok",
    "nike", "adidas", "wilson", "head", "yonex", "everlast",
    
    # --- Misc & Accessories ---
    "casio", "fossil", "citizen", "rolex", "seiko", "tag heuer", "samsung gear",
    "fitbit", "garmin", "mi band", "anker", "oraimo", "baseus", "ugreen"
]




# --- Deal, Offer & Discount Related Words (Kenyan & Global E-commerce Context) ---
KNOWN_DEAL_WORDS = [
    # --- General Deal Indicators ---
    "cheap", "affordable", "discount", "discounted", "deal", "deals", "offer", "offers",
    "promo", "promotion", "promotions", "flash", "flash sale", "clearance", "clearance sale",
    "budget", "bargain", "special offer", "price drop", "reduced price", "best price", 
    "low price", "lowest price", "under", "below", "less than", "off", "save", "saving", "savings",
    "markdown", "sale", "sales", "slashed", "cut price", "offer price", "limited offer",

    # --- Marketing & Seasonal Phrases ---
    "flash deal", "flash sales", "crazy deals", "crazy offer", "bundle offer", "combo deal",
    "buy one get one", "bogo", "buy 1 get 1", "half price", "price cut", "special discount",
    "holiday sale", "black friday", "cyber monday", "clearance event", "deal of the day",
    "offer week", "mega sale", "end month offer", "monthly promo", "back to school", 
    "valentine offer", "easter sale", "christmas offer", "midyear sale",

    # --- Local / Regional Phrases ---
    "jumia deals", "kilimall sale", "jiji offer", "crazy jumia deal", "price slash",
    "hot deal", "hot sale", "best deals", "amazing offer", "offer alert", "jumia flash",
    "limited time offer", "affordable deal", "discount price", "budget friendly", 
    "cheap price", "offer now", "deal alert",

    # --- Numerical/Comparison Terms ---
    "below", "under", "less than", "from", "starting at", "up to", "off percent",
    "% off", "half off", "discount up to", "reduced to"
]





KNOWN_PRODUCT_STATES = [
    # --- New & Unused ---
    "new", "brand new", "sealed", "boxed", "open box", "unused", "never used",
    "unopened", "factory sealed", "original packaging", "brandnew", "brand-new",

    # --- Used & Second-Hand ---
    "used", "slightly used", "fairly used", "preowned", "pre-owned", "second hand", "second-hand",
    "lightly used", "gently used", "like new", "almost new", "previously owned", "used but working",
    "tokunbo",  # common in Nigerian context, also appears on East African listings

    # --- Refurbished / Reconditioned ---
    "refurbished", "reconditioned", "renewed", "manufacturer refurbished", "certified refurbished",
    "factory refurbished", "repaired", "tested working",

    # --- Imports / Regional Conditions ---
    "ex-uk", "ex uk", "uk used", "exuk", "ex japan", "japanese used", "ex us", "us used", "ex germany",
    "dubai used", "ex dubai", "china used", "ex china", "foreign used", "imported used",

    # --- Marketplace Phrases ---
    "slightly new", "like-new", "mint condition", "excellent condition", "good condition",
    "working perfectly", "fully functional", "tested ok", "as is", "open but unused"
]







KNOWN_PRODUCT_CATEGORIES = [
    # Electronics
    "phone","phones", "smartphone", "tablet", "laptop", "computer", "tv", "television", "earphones", "headphones", 
    "charger", "power bank", "watch", "smartwatch", "camera", "speaker", "bluetooth speaker",
    
    #  Home Appliances
    "fridge", "freezer", "microwave", "blender", "cooker", "oven", "iron", "fan", "heater", 
    "water dispenser", "washing machine", "gas cooker", "electric kettle", "coffee maker",

    #  Home & Living
    "sofa", "bed", "mattress", "curtains", "mosquito net", "carpet", "table", "chair", 
    "wardrobe", "tv stand", "wall clock",

    #  Baby Products
    "diapers", "baby wipes", "baby clothes", "baby formula", "stroller", "crib", "baby bottle", 
    "pacifier", "baby shoes", "baby blanket", "toys",

    #  Fashion & Apparel
    "dress", "shirt", "trouser", "jeans", "sneakers", "heels", "tshirt", "hoodie", "jacket", "shoes",
    "boots", "cap", "hat", "bag", "belt", "scarf", "socks", "suit", "shorts", "sweater",
    "mtumba", "second hand clothes", "school uniform",

    #  Beauty & Personal Care
    "makeup", "lipstick", "foundation", "perfume", "cologne", "lotion", "soap", "body spray",
    "sanitary pads", "deodorant", "toothpaste", "shampoo", "conditioner", "skincare",

    #  Health
    "painkillers", "face mask", "sanitizer", "vitamins", "cough syrup", "bandages", "thermometer",

    #  Groceries & Food
    "rice", "flour", "cooking oil", "sugar", "milk", "bread", "maize flour", "tea", "coffee",
    "snacks", "noodles", "water", "juice", "spices", "salt", "honey",

    #  Tools & DIY
    "hammer", "screwdriver", "drill", "toolkit", "spanner", "pliers", "tape measure", "glue gun",

    # Automotive
    "car battery", "engine oil", "car seat", "wipers", "tyres", "car mat", "car charger",

    #  Books & Stationery
    "exercise book", "pen", "pencil", "notebook", "textbook", "dictionary", "ruler", "backpack",

    # Pets
    "dog food", "cat food", "pet bed", "pet shampoo", "leash", "collar", "bird cage",

    # Gaming
    "ps4", "ps5", "xbox", "gamepad", "gaming laptop", "gaming mouse", "controller",

    # Sports & Fitness
    "dumbbell", "yoga mat", "treadmill", "sports shoes", "jersey", "gym bag", "football", "basketball"
]





KNOWN_INTENT_KEYWORDS = [
    # --- Core action verbs ---
    "want", "find", "get", "provide", "show", "look", "search", "buy", "compare", "check", "fetch",
    "see", "explore", "discover", "browse", "locate", "scan", "recommend", "suggest", "give",
    "list", "display", "pull", "bring", "showcase", "highlight", "find me", "get me",
    "look for", "look up", "search for", "check for", "hunt for", "track down", "identify",
    "fetch me", "find out", "view", "show me", "get details", "display results",

    # --- Conversational / polite variants ---
    "can you find", "could you show", "help me get", "help me find", "please show", "please find",
    "please help me find", "please get me", "i need", "need to find", "i’m looking for",
    "looking for", "trying to find", "could you get", "assist me with", "help find",

    # --- Shopping-related intents ---
    "order", "shop", "purchase", "checkout", "place order", "add to cart", "buy now", "reserve",
    "make an order", "view price", "view prices", "see offers", "get deals", "check deals",
    "compare prices", "see discounts", "find offers", "get offers", "find deals", "shop for",

    # --- Discovery / browsing verbs ---
    "explore", "discover", "scroll", "view options", "check options", "see what’s available",
    "find available", "show available", "browse through", "go through", "find out more",

    # --- Questions phrased as commands ---
    "what are", "where can i find", "how to find", "show me the best", "find for me", 
    "can you get", "could you get", "can you show", "may i see", "tell me about",
    "suggest me", "recommend me", "what’s available", "can you list", "could you list"
]



# MARKETPLACE NAMES AND VARIATIONS (Kenya-specific 🇰🇪 ) Includes known e-commerce platforms, supermarket delivery portals, 


KNOWN_MARKETPLACE_KEYWORDS = [
    "jumia", "jiji", "kilimall", "carrefour", "naivas", "quickmart", "uchumi", "tuskys", "chandarana",
    "facebook marketplace", "whatsapp market", "telegram market", "instagram shop", "x shop",
    "tiktok shop", "amazon", "ebay", "aliexpress", "shein",

]



# 🌍 COUNTRY / REGION NAMES Focus: East Africa + key African markets + a few international regions for test realism


KNOWN_COUNTRY_KEYWORDS = [
    "kenya", "ug", "uganda", "tz", "tanzania", "rwanda", "burundi","ethiopia", "south sudan", "somalia",

    # --- Central & Southern Africa ---
    "zambia", "zimbabwe", "malawi", "botswana", "namibia", "mozambique","lesotho", "eswatini", "angola", "dr congo", "congo",

    # --- West Africa ---
    "nigeria", "naija", "ghana", "cameroon", "senegal", "ivory coast", "côte d’ivoire", "benin", "togo", "sierra leone", "liberia",

    # --- North Africa ---
    "egypt", "morocco", "tunisia", "algeria", "sudan", "libya",

    # --- Global / Common Mentions (Testing + Imports/Brands) ---
    "south africa", "sa", "united states", "us", "usa", "u.s.", "uk", "united kingdom", "england", "canada", "india", "china", 
    "dubai", "uae", "japan", "france", "germany"
]






KNOWN_STOP_WORDS = [
    # --- Pronouns & determiners ---
    "i", "me", "my", "mine", "you", "your", "yours", "he", "him", "his", "she", "her", "hers",
    "it", "its", "we", "us", "our", "ours", "they", "them", "their", "theirs",
    "someone", "anyone", "everyone", "no one", "somebody", "anybody", "everybody",

    # --- Articles & demonstratives ---
    "a", "an", "the", "this", "that", "these", "those", "there", "here", "such", "each", "every",

    # --- Auxiliary & linking verbs ---
    "am", "is", "are", "was", "were", "be", "been", "being", "do", "does", "did", 
    "have", "has", "had", "having", "can", "could", "shall", "should", "will", "would", 
    "may", "might", "must", "ought",

    # --- Conjunctions & connectors ---
    "and", "or", "but", "if", "then", "than", "because", "though", "although", "while",
    "when", "where", "before", "after", "once", "since", "unless", "until", "whereas",
    "however", "so", "therefore", "besides", "meanwhile", "moreover",

    # --- Prepositions ---
    "on", "in", "at", "to", "for", "from", "with", "into", "onto", "upon", "over", "under", 
    "between", "among", "around", "about", "through", "across", "by", "off", "up", "down", 
    "near", "beside", "within", "outside", "along", "beyond", "behind", "toward",

    # --- Quantifiers & general adjectives ---
    "some", "any", "many", "few", "several", "much", "more", "less", "lot", "lots", "enough",
    "other", "another", "whole", "plenty", "most", "least", "various", "certain", "same",

    # --- Politeness / conversation fillers (Kenyan English friendly) ---
    "please", "kindly", "thanks", "thank", "thank you", "excuse", "sorry",

    # --- Marketplace-neutral filler words ---
    "good", "best", "better", "nice", "fine", "great", "amazing", "cool", "awesome", "fantastic",
    "deal", "deals", "offer", "offers", "cheap", "affordable", "expensive", "budget", "pricey",

    # --- Functionally neutral words ---
    "sort", "type", "kind", "piece", "item", "product", "stuff", "things", "thing", 
    "available", "looking", "interested", "wanting", "searching", "showing", "finding",

    # --- Numeric & comparison fillers ---
    "under", "below", "over", "above", "around", "approximately", "about", "nearly",

    # --- Contextual marketplace filler ---
    "brand", "model", "version", "edition", "series", "generation"
]




ExceptionsFromName = [
    # Core grammatical stopwords
    "find", "me", "on", "the", "a", "an", "in", "of", "for", "to", "from", 
    "with", "is", "are", "was", "were", "be", "being", "been", "that", "this", "those", "these",

    # Conversational/filler words
    "can", "you", "please", "help", "kindly", "show", "give", "get", "look", "search", "buy", 
    "want", "need", "see", "tell", "fetch", "provide", "finds", "looking",

    # Common descriptive fillers (not part of product names)
    "good", "best", "cheap", "affordable", "low", "high", "latest", "new", "old",
    "original", "quality", "nice", "some", "any", "sort", "type", "kind",

    # Common structural/connector words
    "and", "or", "but", "so", "then", "there", "as", "by", "at", "into", "about", 
    "around", "between", "near", "under", "over", "above", "below",

    # Value-based & prepositional filters often excluded from name
    "under", "over", "around", "below", "above", "within", "outside", "across",
    
    # Marketplace & attribute keywords that shouldn't appear in name
    "offer", "offers", "deal", "deals", "discount", "price", "promo", "promotion", "sale",

    # Time or contextual fillers
    "today", "now", "currently", "available", "latest", "newest"
]


KNOWN_AFTER_TOKENS = [
    # Core prepositions
    "for", "in", "with", "on", "at", "under", "over", "by", "between", 
    "around", "from", "to", "near", "into", "within", "across", "along",
    "behind", "beside", "beyond", "toward", "outside", "inside", "upon",
    "through", "above", "below", "against", "among",

    # Marketplace-context and filter indicators
    "including", "excluding", "except", "featuring", "offering",
    "priced", "costing", "worth", "made", "designed", "built",
    "during", "after", "before", "since", "until", "as", "like",

    # Common secondary-attribute starters in user prompts
    "for",          # e.g. "for men", "for office use"
    "in",           # e.g. "in Kenya", "in Nairobi"
    "with",         # e.g. "with camera", "with warranty"
    "by",           # e.g. "by Nike", "by Samsung"
    "near",         # e.g. "near me"
    "at",           # e.g. "at discount"
    "under",        # e.g. "under 5000"
    "below",        # e.g. "below 1000"
    "above",        # e.g. "above 10000"
    "around",       # e.g. "around 2000"
    "to",           # e.g. "to Nairobi", "to Mombasa"
    "of"            # e.g. "pair of", "type of"
]




COMMON_PRE_COUNTRY_WORDS = [
    # Basic positional/location
    'in', 'from', 'within', 'inside', 'at', 'across', 'around', 'throughout', 'near',

    # Manufacture / production
    'made', 'manufactured', 'produced', 'built', 'assembled', 'crafted', 'grown',

    # Shipping / delivery / availability
    'to', 'for', 'into', 'delivered', 'shipping', 'shipped', 'send', 'sent',
    'exported', 'imported', 'available', 'supply',

    # Market / business context
    'across', 'within', 'serving', 'operating', 'selling', 'buy', 'market',
    'retail', 'wholesale', 'store', 'marketplace',

    # Preference / activity / origin
    'visiting', 'travelling', 'travel', 'touring', 'based', 'living', 'residing',
    'born', 'moved'
]





# 🛍️ MOST COMMONLY SEARCHED ITEMS (Kenya-focused, general & trending)
KNOWN_PRODUCT_KEYWORDS = [
    # --- 🖥️ Electronics ---
    "smartphone", "phone", "iphone", "samsung", "tablet", "laptop", "computer", 
    "desktop", "earphones", "headphones", "bluetooth speaker", "charger", 
    "power bank", "memory card", "usb cable", "hard drive", "flash disk", 
    "camera", "smartwatch", "tv", "television", "decoder", "monitor", "printer",

    # --- 👟 Fashion & Apparel ---
    "t-shirt", "shirt", "trouser", "jeans", "dress", "skirt", "shorts", 
    "jacket", "hoodie", "sweater", "coat", "shoes", "sneakers", "heels", 
    "sandals", "boots", "handbag", "backpack", "belt", "cap", "hat", 
    "watch", "sunglasses", "wallet",


    # --- 🍲 Home & Kitchen ---
    "fridge", "refrigerator", "microwave", "cooker", "oven", "gas cylinder", 
    "blender", "mixer", "kettle", "toaster", "rice cooker", "pressure cooker", 
    "iron box", "vacuum cleaner", "fan", "heater", "extension cable", 
    "water dispenser", "utensils", "cookware", "sofa", "bed", "mattress", 
    "table", "chair", "wardrobe", "curtains", "carpet", "lamp", "mirror",


    # --- 👶 Baby & Kids ---
    "baby clothes", "diapers", "baby shoes", "baby bottle", "stroller", 
    "car seat", "toys", "pacifier", "baby wipes", "baby lotion",


    # --- 💄 Beauty & Personal Care ---
    "perfume", "body lotion", "face cream", "foundation", "lipstick", 
    "makeup", "hair dryer", "hair straightener", "wig", "weave", 
    "shampoo", "conditioner", "soap", "toothpaste", "razor", 
    "deodorant", "nail polish", "face mask",


    # --- 📚 Education & Office ---
    "book", "notebook", "pen", "pencil", "calculator", "school bag", 
    "office chair", "office desk", "stationery", "printer ink",


    # --- 🧺 Cleaning & Home Essentials ---
    "detergent", "soap", "broom", "mop", "bucket", "dustbin", 
    "disinfectant", "tissue", "air freshener",

    # --- 🚗 Automotive ---
    "car", "motorcycle", "bike", "helmet", "engine oil", "car battery", 
    "tyres", "wipers", "car mats", "seat covers",

    # --- 💻 Accessories & Gadgets ---
    "mouse", "keyboard", "usb hub", "webcam", "router", "wifi adapter",
    "projector", "tripod", "power extension",

    # --- 📱 Mobile Categories (for intent refinement) ---
    "android phone", "iphone", "feature phone", "smartwatch", 
    "tablet", "earbuds", "charging cable", "case", "screen protector",

    # --- 🏡 Home Improvement & Tools ---
    "drill", "hammer", "screwdriver", "tool set", "paint", "ladder", 
    "tape measure", "wrench", "gloves", "safety boots",

    # --- 🧴 Health & Wellness ---
    "supplements", "vitamins", "painkillers", "bandages", "sanitizer", 
    "first aid kit", "mask", "blood pressure monitor", "thermometer",

    # --- 🐶 Pets ---
    "dog food", "cat food", "pet cage", "leash", "collar", "pet shampoo",

    # --- 🍔 Food & Groceries ---
    "rice", "sugar", "flour", "cooking oil", "salt", "snacks", "milk", 
    "tea", "coffee", "bread", "drinks", "juice", "water", "spices","honey",

    # --- 💡 Miscellaneous / Trending ---
    "solar panel", "generator", "inverter", "extension cable", 
    "power adapter", "security camera", "ring light", "microphone",
    "gaming chair", "gamepad", "console", "playstation", "xbox", 
    "air fryer", "electric kettle", "smart bulb", "led light",

    # --- 🏍️ Popular Kenyan Queries (Localized) ---
    "phones under 10000", "cheap smartphones", "best deals", 
    "second hand phones", "used laptops", "jumia offers", 
    "baby items in nairobi", "smart tvs in kenya", "solar kits", 
    "electric bikes", "fashion for men", "fashion for ladies"
]



