



from matcher import nlp, matcher
from collections import defaultdict



promptSuggestions = [
  #🛍️ Shopping Deals (Diverse & Simple)
  "Find sports shoes in Kenya",
  "Show affordable smartphones in Nairobi",
  "Find grocery discounts in Kenya",
  "Locate laptops under 100000 KES",
  "Get deals on kitchen appliances",
  "Find discounted gaming consoles",
  "Show original perfumes online in Kenya",
  "Find prices for smart TVs above 50 inches",
  "Get deals on fashion sneakers",
  "Find women's handbags under 5000 KES",
  "Locate affordable jackets for men",
  "Show trending wristwatches",
  "Find LED lights on discount",
  "Get best prices for headphones",
  "Find compact coffee makers in Kenya",
  "Show affordable office chairs",
  "Locate smart home devices under 20000 KES",
  "Find best deals on backpacks",
  "Get discounts on sunglasses",
  "Show ergonomic keyboards",

  # 🏠 Home & Lifestyle
  "Show affordable sofa sets",
  "Find energy-efficient refrigerators",
  "Get deals on kitchen blenders",
  "Locate home decor items in Nairobi",
  "Show bed frames with delivery",
  "Find stylish curtains under 5000 KES",
  "Show budget-friendly dining tables",
  "Locate mattresses on sale",
  "Find compact wardrobes",
  "Get best deals on wall art",

  # 🧑‍💻 Tech & Gadgets
  "Find laptops for programming under 120000 KES",
  "Show gaming PCs on discount",
  "Locate budget-friendly tablets",
  "Find a smartwatch for Android phones",
  "Show wireless earbuds with long battery life",
  "Locate Bluetooth speakers under 5000 KES",
  "Find power banks with fast charging",
  "Show portable projectors in Kenya",
  "Find USB-C monitors on sale",
  "Get deals on gaming mice",

  # 🛒 Groceries & Essentials
  "Find supermarkets with rice and sugar discounts",
  "Show where to buy baby diapers in bulk",
  "Locate cooking oil offers this week",
  "Find organic skincare products on sale",
  "Get fresh fruit delivery in Nairobi",
  "Find affordable milk brands",
  "Show discounted snacks and chocolates",
  "Locate cleaning supplies under 1000 KES",
  "Find best deals on bottled water",
  "Get vegetable bundles delivered",

  #👟 Fashion & Apparel
  "Show affordable t-shirts for men",
  "Find women's dresses under 4000 KES",
  "Locate stylish sneakers in Kenya",
  "Get best deals on jackets",
  "Show watches under 3000 KES",
  "Find affordable hats and caps",
  "Locate trendy sunglasses",
  "Get discounts on belts and wallets",
  "Show sports socks packs",
  "Find affordable leggings for women",

  # 🎁 Seasonal / Event-Based
  "Find Black Friday deals near me",
  "Show Christmas offers on electronics",
  "Find Valentine's Day gift bundles",
  "Locate back-to-school deals on stationery",
  "Get Easter weekend travel deals",
  "Show New Year discounts on party supplies",
  "Find Mother's Day gift ideas",
  "Locate Father's Day gadgets",
  "Get deals on graduation gifts",
  "Find Halloween decorations on sale"
]


# -----------------------------
# Price keywords to anchor numeric extraction
# -----------------------------
price_keywords = ["under", "around", "about", "for", "max", "min"]

# -----------------------------
# Process each prompt
# -----------------------------
for prompt in promptSuggestions:
    print(f"\nPrompt: {prompt}")
    doc = nlp(prompt)
    raw_matches = matcher(doc)

    results = defaultdict(set)  # cleaned results per prompt

    for match_id, start, end in raw_matches:
        label = nlp.vocab.strings[match_id]
        span = doc[start:end].text.strip()

        # Only keep numeric PRICE if near currency or preceded by price hint
        if label == "PRICE":
            words = span.split()
            filtered_nums = []

            for i, w in enumerate(words):
                if w.isdigit():
                    prev_word = words[i-1].lower() if i > 0 else ""
                    next_word = words[i+1].lower() if i+1 < len(words) else ""
                    if next_word in ["usd", "$", "dollars", "kes", "ksh", "shillings"] or prev_word in price_keywords:
                        filtered_nums.append(w)

            if not filtered_nums:
                continue
            span = filtered_nums[0]

        results[label].add(span)

    # Print final cleaned results for this prompt
    for label, spans in results.items():
        for span in spans:
            print(f"{label}: {span}")
            
            
