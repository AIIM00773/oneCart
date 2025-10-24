




import requests
from itertools import combinations

PATH = "https://api.escuelajs.co/api/v1/products/"

def fetch_items(query_object):
    """
    Fetches items from the fake store API using smart token aggregation.
    - Combines name tokens into logical search groups
    - Uses category or price filters when available
    - Minimizes redundant API calls
    """
    if not query_object or not isinstance(query_object, dict):
        return {"error": "Invalid query_object"}

    try:
        # Extract token groups
        category_tokens = query_object.get('item_category_tokens', [])
        name_tokens = query_object.get('item_name_tokens', [])
        min_price = query_object.get('min_price')
        max_price = query_object.get('max_price')

        # === Step 1: Prepare token combinations ===
        # Example: ["smart", "phone", "samsung"] → ["smart", "phone", "samsung", "smart phone", "phone samsung", "smart phone samsung"]
        search_phrases = set()
        for i in range(1, len(name_tokens) + 1):
            for combo in combinations(name_tokens, i):
                search_phrases.add(" ".join(combo))

        if not search_phrases:
            return {"message": "No valid name tokens to search."}

        # === Step 2: Construct base filters ===
        base_filters = {}
        if category_tokens:
            base_filters["categorySlug"] = category_tokens[0]
        if min_price:
            base_filters["price_min"] = min_price
        if max_price:
            base_filters["price_max"] = max_price

        # === Step 3: Make requests for each phrase ===
        all_results = []
        for phrase in search_phrases:
            params = {"title": phrase, **base_filters}
            query_str = "&".join(f"{k}={v}" for k, v in params.items())
            url = f"{PATH}?{query_str}"

            print(f"🔍 Fetching: {url}")
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if isinstance(data, list) and data:
                        all_results.extend(data)
            except Exception as e:
                print(f"❌ Error fetching {url}: {e}")

        # === Step 4: Deduplicate results ===
        unique_results = []
        seen_ids = set()
        for item in all_results:
            pid = item.get("id")
            if pid and pid not in seen_ids:
                seen_ids.add(pid)
                unique_results.append(item)

        return unique_results if unique_results else {"message": "No results found."}

    except Exception as e:
        return {"error": str(e)}
