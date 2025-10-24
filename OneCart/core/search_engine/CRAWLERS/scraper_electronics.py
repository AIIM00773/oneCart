


# ===========================
# Imports
# ===========================

# Data & Web
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random
import json



# ===========================
# Web Scraper Function
# ===========================

headers = {
    "User-Agent": ( "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" )
}
    


def scrape_phoneplace_products(output_file="phoneplacekenya.json"):
    webURLs = [
        "https://www.phoneplacekenya.com/product-category/smartphones/",
        "https://www.phoneplacekenya.com/product-category/mobile-phone-accessories/",
        "https://www.phoneplacekenya.com/product-category/audio/",
        "https://www.phoneplacekenya.com/product-category/gaming/",
        "https://www.phoneplacekenya.com/product-category/storage/",
        "https://www.phoneplacekenya.com/product-category/tablets/",
        "https://www.phoneplacekenya.com/content-creator-kit/",
    ]



    category_map = {
        0: ["smartphones", "phones", "phone", "smartphone"],
        1: ["mobile accessories", "phones accessories", "phone accessories", "smartphone accessories"],
        2: ["audios", "audio", "audio accessories", "audios accessories", "music accessories"],
        3: ["gaming", "gamer", "gaming accessories", "gamer accessories", "videogame", "videogames", "videogames accessories"],
        4: ["storages", "storage", "drives", "storage accessories", "storages accessories"],
        5: ["tablets", "tablet", "tabs", "tablet accessories", "tablets accessories"],
        6: ["content creation", "content creator", "content creators", "content creator accessories", "content creation accessories", "content", "youtuber", "tiktoker"],
    }

    session = requests.Session()
    session.headers.update(headers)

    all_products = []

    for idx, url in enumerate(webURLs):
        try:
            response = session.get(url, timeout=14)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to get {url}: {e}")
            continue

        print(f"\nStatus Code: {response.status_code} for URL: {url}\n")

        soup = BeautifulSoup(response.text, "lxml")
        if not soup:
            continue

        products = soup.find_all("section", class_="product")
        if not products:
            continue

        for product in products:
            product_name_tag = product.find("h3", class_="heading-title product-name")
            product_brand_tag = product.find("div", class_="product-brands")
            product_link_tag = product.select_one(".thumbnail-wrapper a[href]")
            product_image_tag = product.select_one(".thumbnail-wrapper img")

            product_name = product_name_tag.get_text(strip=True) if product_name_tag else "N/A"
            product_brand = product_brand_tag.get_text(strip=True) if product_brand_tag else "N/A"
            product_link = product_link_tag.get("href") if product_link_tag else "N/A"
            product_image_link = product_image_tag.get("src") if product_image_tag else "N/A"
            product_category = category_map.get(idx, ["Unknown"])

            all_products.append({
                "product_Name": product_name,
                "product_Brand": product_brand,
                "product_Category": ", ".join(product_category),
                "product_Source_URL": url,
                "product_Link": product_link,
                "product_Image_Link": product_image_link,
            })

        delay = random.uniform(2, 3)
        print(f"Sleeping for {delay:.2f} seconds...\n")
        time.sleep(delay)

    # Save to JSON
    df = pd.DataFrame(all_products)
    df.to_json(output_file, orient="records", indent=2, force_ascii=False)
    print(f"\nSaved {len(all_products)} products to '{output_file}'.")




#scrape_phoneplace_products()










gaming_console_brands = [
    "Sony",         # PlayStation
    "Microsoft",    # Xbox
    "Nintendo",     # Switch, Wii
    "Valve",        # Steam Deck
    "Atari",
    "SEGA",
    "Logitech",     # Logitech G Cloud (cloud gaming handheld)
    "Anbernic",     # Retro handhelds
    "Ayaneo",       # PC-based handhelds
    "Razer",        # Razer Edge
    "ASUS",         # ROG Ally
    "Lenovo",       # Legion Go
]


pc_gaming_brands = [
    "Alienware", "MSI", "ASUS", "ROG", "Acer", "Predator", "Gigabyte", "AORUS",
    "HP", "OMEN", "Dell", "Lenovo", "Legion", "CyberPowerPC", "iBUYPOWER", "NZXT"
]



pc_component_brands = [
    "NVIDIA", "AMD", "Intel", "ASRock", "EVGA", "Corsair", "Cooler Master",
    "Thermaltake", "G.SKILL", "Seasonic", "Noctua", "be quiet!"
]


peripheral_brands = [
    "Logitech", "Logitech G", "Razer", "SteelSeries", "Corsair", "HyperX",
    "ROCCAT", "Redragon", "Cooler Master", "Turtle Beach", "Astro",
    "Mad Catz", "Thrustmaster", "8BitDo", "Scuf", "PowerA"
]


gaming_audio_brands = [
    "HyperX", "SteelSeries", "Corsair", "Razer", "Astro", "Logitech G",
    "Turtle Beach", "EPOS", "Sennheiser", "Sony", "Beyerdynamic"
]


gaming_monitor_brands = [
    "ASUS", "ROG", "Acer", "Predator", "BenQ", "Zowie", "Samsung", "LG", "MSI", "Gigabyte", "AOC", "ViewSonic"
]



gaming_furniture_brands = [
    "Secretlab", "DXRacer", "Noblechairs", "AndaSeat", "GT Racing", "RESPAWN", "Corsair", "Cougar"
]


streaming_brands = [
    "Elgato", "Blue", "Rode", "Shure", "Logitech", "AverMedia", "Stream Deck", "GoXLR", "Razer Seiren"
]



gaming_brands = list(set(
    gaming_console_brands +
    pc_gaming_brands +
    pc_component_brands +
    peripheral_brands +
    gaming_audio_brands +
    gaming_monitor_brands +
    gaming_furniture_brands +
    streaming_brands
))





gaming_categories = [
    # 🔌 Gaming Platforms & Devices
    "gaming console",
    "handheld console",
    "gaming handheld",
    "pc gaming",
    "gaming laptop",
    "gaming desktop",
    "gaming pc",
    "steam deck",
    "cloud gaming device",

    # 🕹️ Controllers & Input Devices
    "game controller",
    "gamepad",
    "joystick",
    "steering wheel",
    "flight stick",
    "racing wheel",
    "arcade stick",
    "vr controller",

    # 🖥️ Display & Visual Hardware
    "gaming monitor",
    "ultrawide monitor",
    "curved gaming monitor",
    "4k gaming monitor",
    "high refresh rate monitor",
    "vr headset",
    "virtual reality headset",

    # 🎧 Audio & Communication
    "gaming headset",
    "gaming headphones",
    "gaming microphone",
    "usb mic",
    "streaming mic",
    "chat headset",

    # ⌨️ Peripherals
    "gaming mouse",
    "gaming keyboard",
    "mouse pad",
    "gaming mat",
    "mechanical keyboard",
    "rgb keyboard",
    "rgb mouse",

    # 🛠️ Components & Hardware
    "graphics card",
    "gpu",
    "cpu",
    "motherboard",
    "gaming ram",
    "gaming ssd",
    "cooling fan",
    "gaming psu",
    "pc case",
    "thermal paste",
    "liquid cooler",

    # 💺 Furniture & Comfort
    "gaming chair",
    "gaming desk",
    "monitor stand",
    "footrest",
    "mouse bungee",

    # 🎥 Streaming & Recording
    "capture card",
    "streaming mic",
    "webcam",
    "ring light",
    "stream deck",
    "green screen",

    # 🧑‍🎤 Gaming Lifestyle
    "game merch",
    "gaming clothing",
    "led lights",
    "rgb lights",
    "gaming backpack",
    "console stand",
    "controller charger",
    "gaming speaker",

    # 🧩 Accessories & Misc
    "headset stand",
    "thumb grips",
    "controller skin",
    "gaming hub",
    "external hdd for gaming",
    "memory card for switch",
    "console cooling stand",

    # 📦 Software & Content
    "video game",
    "game disc",
    "digital game code",
    "dlc",
    "game subscription",
    "gaming gift card"
]





camera_brands = [
    "Canon", "Nikon", "Sony", "Fujifilm", "Panasonic", "Olympus", "Leica", "Pentax", "Ricoh",
    "Hasselblad", "Sigma", "Phase One", "Kodak", "Minolta", "Contax", "Yashica", "Voigtländer",
    "Polaroid", "Lomography","Hama","Canyon","AIWA","Netatmo",

    # Action cameras
    "GoPro", "DJI", "Insta360", "Akaso", "SJCAM", "Campark", "Eken", "Yi", "Osmo",

    # Security & surveillance
    "Hikvision", "Dahua", "Reolink", "Arlo", "Ring", "Wyze", "Nest", "TP-Link", "EZVIZ",
    "Swann", "Blink", "Zmodo", "Lorex", "Bosch Security", "Axis Communications", "Ubiquiti",
    "Xiaomi", "Eufy", "Victure",

    # Smartphone brands with notable camera systems
    "Apple", "Samsung", "Google", "Huawei", "Xiaomi", "Oppo", "OnePlus", "Vivo", "Sony Xperia", "Asus ROG"
]




camera_categories = [
    # 🎞️ General Types
    "digital camera",
    "film camera",
    "camera",
    "photo camera",
    "still camera",

    # 📷 Photography Cameras
    "dslr camera",
    "mirrorless camera",
    "compact camera",
    "point and shoot camera",
    "bridge camera",
    "instant camera",
    "medium format camera",
    "full-frame camera",
    "35mm camera",
    "rangefinder camera",
    "twin lens reflex camera",
    "action camera",
    "vlogging camera",
    "underwater camera",
    "professional camera",
    "cinema camera",
    "studio camera",

    # 📱 Mobile & Hybrid
    "smartphone camera",
    "mobile camera",
    "tablet camera",
    "webcam",
    "phone camera",
    "ai camera",
    "usb camera",

    # 🎥 Video & Streaming
    "camcorder",
    "video camera",
    "handycam",
    "live streaming camera",
    "body camera",
    "helmet camera",
    "dash cam",
    "drone camera",

    # 🔐 Surveillance & Security
    "cctv camera",
    "security camera",
    "surveillance camera",
    "ip camera",
    "network camera",
    "wifi camera",
    "smart camera",
    "home security camera",
    "baby monitor camera",
    "doorbell camera",
    "wireless camera",
    "dome camera",
    "bullet camera",
    "thermal camera",

    # 🛠️ Camera Accessories (optional inclusion)
    "camera lens",
    "tripod",
    "camera stabilizer",
    "gimbal",
    "camera light",
    "camera bag",
    "camera kit"
]



it_and_laptop_brands = [
    # 🧑‍💻 Laptop & Desktop Manufacturers
    "Dell",
    "HP",
    "Lenovo",
    "Apple",
    "Asus",
    "Acer",
    "Microsoft",
    "MSI",
    "Samsung",
    "Toshiba",
    "Razer",
    "Alienware",
    "LG",
    "Huawei",
    "Chuwi",
    "Gigabyte",
    "Dynabook",
    "Fujitsu",
    "Xiaomi",
    "Infinix",
    "Avita",
    "iLife",
    "System76",
    "Origin PC",
    "Clevo",

    # 🖥️ PC Brands / Prebuilt & Custom PCs
    "CyberPowerPC",
    "iBUYPOWER",
    "NZXT",
    "Corsair",
    "Maingear",
    "Zotac",
    "Shuttle",

    # 🧩 Component & Chipset Brands
    "Intel",
    "AMD",
    "NVIDIA",
    "ASRock",
    "Gigabyte",
    "EVGA",
    "Corsair",
    "Cooler Master",
    "Thermaltake",
    "G.SKILL",
    "Crucial",
    "Western Digital",
    "Seagate",
    "Samsung",
    "Kingston",
    "Patriot",
    "Transcend",
    "Adata",

    # 🖨️ Accessories & Peripherals
    "Logitech",
    "Razer",
    "SteelSeries",
    "Redragon",
    "Anker",
    "Belkin",
    "HP",
    "Dell",
    "Epson",
    "Canon",
    "Brother",
    "Wacom",

    # 🖥️ Monitor Brands (IT Displays)
    "BenQ",
    "AOC",
    "ViewSonic",
    "Philips",
    "LG",
    "Samsung",
    "Dell",
    "Asus",
    "MSI",
    "Gigabyte",

    # ☁️ Enterprise IT / Networking / Servers
    "Cisco",
    "Juniper",
    "IBM",
    "Oracle",
    "HPE",  # Hewlett Packard Enterprise
    "Dell EMC",
    "NetApp",
    "Supermicro",
    "Ubiquiti",
    "TP-Link",
    "Fortinet",
    "Synology",
    "QNAP"
]




it_and_laptop_categories = [
    # 💻 Laptops
    "laptop",
    "ultrabook",
    "notebook",
    "gaming laptop",
    "business laptop",
    "2-in-1 laptop",
    "convertible laptop",
    "chromebook",
    "macbook",
    "student laptop",
    "netbook",
    "rugged laptop",

    # 🖥️ Desktops & All-in-Ones
    "desktop computer",
    "gaming desktop",
    "all-in-one pc",
    "mini pc",
    "workstation",
    "tower pc",
    "custom pc",
    "prebuilt pc",
    "thin client",

    # 🧩 PC Components
    "processor",
    "cpu",
    "graphics card",
    "gpu",
    "motherboard",
    "ram",
    "memory",
    "hard drive",
    "hdd",
    "solid state drive",
    "ssd",
    "nvme drive",
    "power supply",
    "psu",
    "pc case",
    "cooling fan",
    "liquid cooler",
    "thermal paste",
    "optical drive",

    # 🎮 Peripherals
    "keyboard",
    "mouse",
    "gaming keyboard",
    "gaming mouse",
    "mouse pad",
    "monitor",
    "gaming monitor",
    "webcam",
    "headset",
    "microphone",
    "external speaker",
    "printer",
    "scanner",
    "graphic tablet",
    "stylus",

    # 🧳 Storage Devices
    "external hard drive",
    "external ssd",
    "usb flash drive",
    "memory card",
    "sd card",
    "micro sd card",

    # 🌐 Networking & Connectivity
    "router",
    "modem",
    "wifi adapter",
    "ethernet switch",
    "access point",
    "mesh wifi system",
    "network card",
    "dongle",

    # ⚙️ Accessories & Add-ons
    "laptop bag",
    "laptop stand",
    "docking station",
    "usb hub",
    "charging cable",
    "power adapter",
    "laptop charger",
    "screen protector",
    "laptop sleeve",
    "cooling pad",

    # ☁️ Enterprise IT & Infrastructure
    "server",
    "rack server",
    "blade server",
    "nas",
    "network storage",
    "backup drive",
    "firewall appliance",
    "network switch",
    "enterprise router",
    "server cabinet",
    "power distribution unit",
    "kvm switch",

    # 🖱️ Input & Output Devices
    "touchpad",
    "trackball",
    "joystick",
    "game controller",
    "projector",
    "digital whiteboard",

    # 🛠️ Software & Utilities (Optional)
    "operating system",
    "office software",
    "antivirus software",
    "backup software",
    "remote desktop tool"
]



speaker_brands = [
    # 🔉 Consumer & Home Audio
    "Sony",
    "Samsung",
    "LG",
    "Panasonic",
    "Philips",
    "Toshiba",
    "Sharp",
    "JVC",
    "Hitachi",
    "Xiaomi",
    "Hisense",
    "TCL",

    # 🔊 Portable & Bluetooth Speakers
    "JBL",
    "Sony",
    "Bose",
    "Anker",
    "Tribit",
    "Ultimate Ears",  # (UE)
    "Marshall",
    "Bang & Olufsen",
    "Beats",
    "Harman Kardon",
    "Soundcore",
    "Sylvania",
    "Boat",
    "Mivi",
    "Zebronics",
    "Oraimo",
    "Promate",

    # 🛋️ Soundbars & Home Theater
    "Sonos",
    "Samsung",
    "Sony",
    "Bose",
    "Yamaha",
    "LG",
    "Polk Audio",
    "Vizio",
    "Klipsch",
    "Denon",
    "Onkyo",
    "JBL",
    "Creative",
    "Harman Kardon",
    "Philips",

    # 🧠 Smart Speakers
    "Amazon Echo",
    "Google Nest",
    "Apple HomePod",
    "Sonos",
    "Xiaomi",
    "Baidu",
    "Lenovo",  # Smart Clock / Smart Display
    "Harman Kardon"  # Citation series

    # 🎧 Professional Audio & Hi-Fi
    "Yamaha",
    "JBL Professional",
    "KRK",
    "Mackie",
    "Behringer",
    "Audioengine",
    "Klipsch",
    "Focal",
    "Edifier",
    "KEF",
    "Bowers & Wilkins",  # B&W
    "Tannoy",
    "Wharfedale",
    "Genelec",
    "Pioneer DJ",
    "Q Acoustics",
    "Cambridge Audio",
    "Elac",
    "Monitor Audio"
]



speaker_categories = [
    # 🔉 General
    "speaker",
    "speakers",
    "audio speaker",
    "multimedia speaker",
    "wireless speaker",
    "portable speaker",
    "usb speaker",

    # 📱 Bluetooth & Portable
    "bluetooth speaker",
    "portable bluetooth speaker",
    "mini bluetooth speaker",
    "outdoor speaker",
    "waterproof speaker",
    "travel speaker",
    "party speaker",
    "battery-powered speaker",

    # 🧠 Smart Speakers
    "smart speaker",
    "voice assistant speaker",
    "alexa speaker",
    "google assistant speaker",
    "home automation speaker",
    "wifi speaker",

    # 🛋️ Home Audio / Entertainment
    "home speaker",
    "bookshelf speaker",
    "floorstanding speaker",
    "soundbar",
    "home theater system",
    "home audio system",
    "2.1 speaker system",
    "5.1 speaker system",
    "7.1 surround sound system",
    "subwoofer",
    "tv speaker",

    # 📻 Desktop & PC Audio
    "desktop speaker",
    "pc speaker",
    "laptop speaker",
    "monitor speaker",
    "computer speaker",
    "gaming speaker",
    "usb-powered speaker",

    # 🔈 Wired Audio
    "wired speaker",
    "aux speaker",
    "rca speaker",
    "speaker with fm radio",

    # 🎧 Professional & Studio
    "studio monitor",
    "monitor speaker",
    "professional speaker",
    "pa speaker",
    "dj speaker",
    "line array speaker",
    "amplified speaker",
    "powered speaker",
    "reference speaker",
    "stage speaker",

    # 🔊 Speaker Accessories (Optional)
    "speaker stand",
    "speaker mount",
    "speaker cover",
    "speaker cable",
    "subwoofer cable",
    "speaker remote"
]

televisionBrands =["sony", "google tv", "hisense", "samsung", "lg", "panasonic", "tcl", "philips", "sharp", "vizio", "mi", "insignia"] 
tlevisionCategories = ["electronics", "Tvs", "television", "televisions", "electronic", "household", "house hold", "house holds", "households", "appliances", "appliace"]


sound_bars_brands = [ "sony", "samsung", "lg", "panasonic", "philips", "toshiba", "sharp", "hisense", "tcl", "vizio","bose", "jbl", "yamaha", "harman kardon", "denon", "onkyo", "marantz", "klipsch", "pioneer", 
                  "polk audio", "sonos", "sennheiser", "bang & olufsen", "kef", "bowers & wilkins", "nakamichi", "edifier", "creative", "anker", "soundcore", "skullcandy", "marshall", "logitech", "altec lansing",
                  "vitron", "sayona", "armco", "bruhm", "mika", "von", "syinix", "amtec", "skyworth", "xiaomi", "mi", "redmi", "xenon", "icona", "vision plus", "tornado", "haier"]

sound_bars_categories =  ["electronics", "home audio", "music", "sound-bars" ,"sound-bar","electronic", "household", "house hold", "house holds", "households", "appliances", "appliace"]

home_appliance_brands = [ 
                  "LG", "Samsung", "Panasonic", "Sony", "Toshiba", "Sharp", "Philips", "Hitachi", "Bosch", "Siemens", "Electrolux", "Whirlpool", "GE", "Haier", "Midea",
                  "Hisense", "TCL", "Vizio", "Changhong", "Akai", "Hyundai", "Daewoo", "Kenwood","Beko", "Ariston", "Indesit", "Candy", "Russell Hobbs", "Black+Decker", "Hamilton Beach","Chefman", "Delonghi", "Nikai", "Gorenje",
                  "Smeg", "KitchenAid", "Breville", "Dyson", "Wolf", "Sub-Zero", "Thermador", "Miele",
                  "Von", "Hotpoint", "Armco", "Bruhm", "Mika", "Ramtons", "Sayona", "Syinix","Vitron", "Nunix", "Amtec", "Skyworth", "Icona", "Tornado", "Xiaomi", "Mi", "Redmi","Xenon", "Royal", "Decakila", "Scanfrost",
                  "Binatone", "Ocean", "Orbit", "Westpoint","Remington", "Panasonic", "Philips", "Braun", "Wahl", "Babyliss", "Conair","Bissell", "Eureka", "Shark", "Hoover", "iRobot", "Roborock", "Ecovacs",
                  "Blue Star", "Prestige", "Kent", "Pureit", "AquaSure", "Coway"
                ]
home_appliance_categories =  ["appliances","appliance","home appliances","home appliance","household appliances","household appliance","domestic appliances","domestic appliance", "domestic","home electronics","home machines",
                  "electrical appliances","electronic appliances","household electronics", "kitchen appliances", "laundry appliances", "cooking appliances", "cleaning appliances","climate control appliances",
                  "personal care appliances","small home appliances","major appliances","large appliances", "white goods","home utility","home tech","home device","energy appliances","electric home appliance","general appliances"]                
                
                
def scrape_anusuma(output_file="anisuma.json"):
    urls = ["https://anisumakenya.co.ke/televisions/",
           "https://anisumakenya.co.ke/sound-bars/", 
           "https://anisumakenya.co.ke/home-appliances/",
           "https://anisumakenya.co.ke/gaming/",
           "https://anisumakenya.co.ke/cameras/",
           "https://anisumakenya.co.ke/it-accessories/",
           "https://anisumakenya.co.ke/speakers/", 
            ]
    
    brands = { 0:televisionBrands,
    
              1:sound_bars_brands,
              2:home_appliance_brands,
              3: gaming_brands ,
              4:camera_brands,
              5: it_and_laptop_brands, 
              6: speaker_brands,
  

                
                }
                
    categories = {0:tlevisionCategories,
                  1:sound_bars_categories,
                  2:home_appliance_categories,
                  3: gaming_categories, 
                  4: camera_categories,
                  5: it_and_laptop_categories, 
                  6: speaker_categories,
                  
                
                }
                  

    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })
    all_products = []

    for idx, url in enumerate(urls):
        try:
            response = session.get(url, timeout=14)

            if not response.status_code == 200:
                print(f"Bad response from {url}\n")
                continue

            soup = BeautifulSoup(response.text, "lxml")
            products = soup.find_all("div", class_="product-wrap")

            if products:
                print(f"\n\nProducts found!! : {len(products)} products.\n\n")

            if len(products) > 0:
                for product in products:
                    # Extracting product name
                    productName_tag = product.find("h2", class_="woocommerce-loop-product__title")
                    productName = productName_tag.get_text(strip=True) if productName_tag else "N/A"

                    # Extracting product link
                    productLink_tag = product.find("a", {"aria-label": True})
                    productLink = productLink_tag["href"] if productLink_tag else "N/A"

                    # Extracting product image link
                    productImage_tag = product.find("img", class_="attachment-woocommerce_thumbnail")
                    productImage = productImage_tag["src"] if productImage_tag else "N/A"

                    productBrand = "N/A"
                    currentBrands = brands[idx]
                    if currentBrands:
                        for brand in currentBrands:
                            if brand.lower() in productName.lower():
                                productBrand = brand    
                        
                    # Saving extracted data
                    all_products.append({
                       "product_Name": productName,
                       "product_Brand": productBrand,
                       "product_Category": ", ".join(categories[0]),
                       "product_Source_URL": url,
                       "product_Link": productLink,
                       "product_Image_Link": productImage,
            })
                    #print(f"Product: {productName}\nLink: {productLink}\nImage: {productImage}\n")

            delay = random.uniform(2, 3)
            print(f"Sleeping for {delay:.2f} seconds...\n")
            time.sleep(delay)
        except Exception as e:
            print(f"Exception encountered at {url} !! the exeption is :  {e}")
            continue


    # Save the extracted data into a JSON file
    print (len(all_products))
    with open(output_file, "w") as file:
        json.dump(all_products, file, indent=2)

    print(f"\n\nSaved data to {output_file}")

# Call the scrape function
scrape_anusuma()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
