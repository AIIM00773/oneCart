


/* ==========================================================================
   MENU INTERACTIONS
   ========================================================================== */

const menuBtn = document.getElementById("menuBtn");
const mobileMenu = document.getElementById("mobileMenu");
const closeMenuBtns = document.querySelectorAll(".closeMenu");
const DisplaysSection = document.getElementById("DisplayAndAlerts");
const DisplaysSection2 = document.getElementById("DisplayAndAlerts2");
const selectionNav = document.getElementById("SelectionsNav"); 


// Open mobile menu with animation
menuBtn.addEventListener("click", () => {
  mobileMenu.classList.remove("translate-x-full");
  mobileMenu.classList.add("opacity-100");

  // Animate menu links sequentially
  mobileMenu.querySelectorAll(".closeMenu").forEach((link, i) => {
    link.classList.add(
      "opacity-0", "translate-x-1", "transition-all", "duration-500",
      "ease-out", "bg-gray-600/50", "text-white",  "p-3", "rounded-xl"
    );

    setTimeout(() => link.classList.remove("opacity-0", "translate-x-5"), i * 100);
  });
});

// Close menu
closeMenuBtns.forEach(btn =>
  btn.addEventListener("click", () => mobileMenu.classList.add("translate-x-full"))
);








const promptSuggestions = [
  // 🛍️ Shopping Deals (Diverse & Simple)
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

  // 🏠 Home & Lifestyle
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

  // 🧑‍💻 Tech & Gadgets
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

  // 🛒 Groceries & Essentials
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

  // 👟 Fashion & Apparel
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

  // 🎁 Seasonal / Event-Based
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
];




  const promptDisplay = document.getElementById("currentPrompt");
  let currentIndex = 0;

  function switchPrompt() {
    // Fade out
    promptDisplay.classList.remove("fade-in");
    promptDisplay.classList.add("fade-out");

    setTimeout(() => {
      // Change text mid-transition
      currentIndex = (currentIndex + 1) % promptSuggestions.length;
      promptDisplay.textContent = promptSuggestions[currentIndex];

      // Fade back in
      promptDisplay.classList.remove("fade-out");
      promptDisplay.classList.add("fade-in");
    }, 500); // match this to CSS transition time
  }

  // Run every 4 seconds
  setInterval(switchPrompt, 4000);

  // Click to populate input
  promptDisplay.addEventListener("click", () => {
    const searchInput = document.getElementById("searchInput");
    if (searchInput) {
      searchInput.value = promptDisplay.textContent.trim().toLowerCase();
      searchInput.focus();
    } else {
      alert("searchInput field not found!");
    }
  });







//--------------------------------------------------------------------------------------------



 // <!-- Existing typing animation (preserved, unchanged except kept consistent) -->

    document.addEventListener("DOMContentLoaded", () => {
      const message = "Market Place";
      const messageBox = document.getElementById("messageBox");
      let index = 0;

      // Clear and add cursor that the CSS styles
      messageBox.textContent = '';
      const cursor = document.createElement("span");
      cursor.className = "cursor";
      messageBox.appendChild(cursor);

      function typeWriter() {
        if (index < message.length) {
          const span = document.createElement("span");
          span.textContent = message.charAt(index);
          span.style.opacity = 0;
          span.style.transition = "opacity 0.24s ease";
          messageBox.insertBefore(span, cursor);

          setTimeout(() => { span.style.opacity = 1; }, 10);
          index++;
          setTimeout(typeWriter, 70);
        }
      }

      setTimeout(() => {
        typeWriter();
      }, 420);
    });






//-----------------------------------------------------------------------------------------------------













  //<!--------FETURED PRODUCTS HANDLING ---------------------------------------------------------------------------------->  




function InitiateProductsHandling(){
  const placeholderFeaturedProductsList = [
    {
      ProductName: "Samsung Galaxy A14",
      ImageUrl: "https://t3.ftcdn.net/jpg/06/00/84/37/240_F_600843706_i1dh4LyAz1hQb5yyxfCr2go2sf0EIbz6.jpg",
      ProductUrl: "https://example.com/products/galaxy-a14"
    },
    {
      ProductName: "HP Pavilion Laptop",
      ImageUrl: "https://t4.ftcdn.net/jpg/06/06/40/35/240_F_606403541_gctiFQ9ErxvRmcrsKf5u8zslmqlkjuh7.jpg",
      ProductUrl: "https://example.com/products/hp-pavilion"
    },
    {
      ProductName: "Nike Air Max",
      ImageUrl: "https://t4.ftcdn.net/jpg/03/07/14/94/240_F_307149460_tRu5lGtxXYqjExMRTGLYwJDbQ1XtR8fQ.jpg",
      ProductUrl: "https://example.com/products/nike-air-max"
    },
    {
      ProductName: "Apple Watch SE",
      ImageUrl: "https://t4.ftcdn.net/jpg/03/01/26/94/240_F_301269434_kxH6nptznbwzPyoZRW3DlF5SoKY8fSKL.jpg",
      ProductUrl: "https://example.com/products/apple-watch"
    },
    {
      ProductName: "Kindle Paperwhite",
      ImageUrl: "https://t3.ftcdn.net/jpg/05/02/99/19/240_F_502991977_C9BaIYr1hCkUwTG4QRSW16ufyEkHU7hC.jpg",
      ProductUrl: "https://example.com/products/kindle"
    },
    {
      ProductName: "HP Pavilion Laptop",
      ImageUrl: "https://t4.ftcdn.net/jpg/06/06/40/35/240_F_606403541_gctiFQ9ErxvRmcrsKf5u8zslmqlkjuh7.jpg",
      ProductUrl: "https://example.com/products/hp-pavilion"
    },
        {
      ProductName: "Apple Watch SE",
      ImageUrl: "https://t4.ftcdn.net/jpg/03/01/26/94/240_F_301269434_kxH6nptznbwzPyoZRW3DlF5SoKY8fSKL.jpg",
      ProductUrl: "https://example.com/products/apple-watch"
    },
    
        {
      ProductName: "Samsung Galaxy A14",
      ImageUrl: "https://t3.ftcdn.net/jpg/06/00/84/37/240_F_600843706_i1dh4LyAz1hQb5yyxfCr2go2sf0EIbz6.jpg",
      ProductUrl: "https://example.com/products/galaxy-a14"
    }
  ];

  let FeaturedProductsHolder = document.getElementById("featuredProductsContainer");

  if (!FeaturedProductsHolder) {
    console.error("Container element not found!");
    return;
  }

  FeaturedProductsHolder.innerHTML = ``;

async function PopulateFeaturedProducts(productsList) {
  if (!productsList || !productsList.length) return;

  for (let product of productsList) {
    const FeaturedProductCard = document.createElement("div");

    FeaturedProductCard.className = `
      min-w-[60%] max-w-[60%] md:min-w-[20%] md:max-w-[20%] h-[220px]
      rounded-2xl overflow-hidden relative group cursor-pointer
      bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900
      border border-white/10
      shadow-[0_4px_15px_rgba(0,0,0,0.4)]
      hover:border-cyan-400/60
      hover:shadow-[0_0_35px_rgba(56,189,248,0.45)]
      hover:from-gray-800 hover:via-gray-900 hover:to-gray-800
      transition-all duration-500 ease-[cubic-bezier(0.4,0,0.2,1)]
      backdrop-blur-xl
    `;

    FeaturedProductCard.innerHTML = `
      <!-- Glow background -->
      <span class="absolute inset-0 rounded-2xl bg-cyan-400/10 opacity-0 
                   group-hover:opacity-100 blur-2xl transition-opacity duration-700"></span>

      <!-- Product image -->
      <img src="${product.ImageUrl}" alt="${product.ProductName}"
           class="w-full h-full object-cover rounded-2xl
           opacity-80 group-hover:opacity-100 group-hover:scale-105
           transition-transform duration-700 ease-[cubic-bezier(0.4,0,0.2,1)]" />

      <!-- Overlay gradient -->
      <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/10 to-transparent"></div>

      <!-- Text content -->
      <div class="absolute bottom-4 left-6 text-white z-10">
        <h3 class="text-lg font-semibold tracking-wide drop-shadow-md group-hover:text-cyan-300 transition-colors duration-500">
          ${product.ProductName}
        </h3>
        <p class="text-sm text-cyan-400/90">Handpicked by OneCart AI</p>
      </div>
    `;

    // Click behavior (anywhere on card)
    FeaturedProductCard.addEventListener("click", () => {
      window.location.href = product.ProductUrl;
    });

    FeaturedProductsHolder.appendChild(FeaturedProductCard);
  }
}


function startFeaturedProductsSlideshow(container, interval = 4500) {
  let scrollAmount = 0;
  let card = container.children[0];

  if (!card) return; // Safety check

  let cardWidth = card.offsetWidth;
  let gap = 16; // Tailwind gap-x-4 = 16px if used

  let totalCards = container.children.length;
  let maxScroll = (cardWidth + gap) * totalCards;

  setInterval(() => {
    scrollAmount += cardWidth + gap;

    if (scrollAmount >= maxScroll - container.offsetWidth) {
      scrollAmount = 0;
    }

    container.scrollTo({
      left: scrollAmount,
      behavior: "smooth"
    });
  }, interval);
}




  async function GetFeaturedProducts() {
    const url = "YOUR_API_ENDPOINT_HERE";
    try {
      let response = await fetch(url, { method: "GET" });
      if (response.ok) {
        let data = await response.json();
        localStorage.setItem("FeaturedProductsList", JSON.stringify(data));
        
        PopulateFeaturedProducts(data);
        setTimeout(() => startFeaturedProductsSlideshow(FeaturedProductsHolder), 3000);
      } else {
        console.error("Failed to fetch products");
        PopulateFeaturedProducts(placeholderFeaturedProductsList);
        setTimeout(() => startFeaturedProductsSlideshow(FeaturedProductsHolder), 3000);
      }
    } catch (error) {
      console.error("Fetch error:", error);
      PopulateFeaturedProducts(placeholderFeaturedProductsList);
        setTimeout(() => startFeaturedProductsSlideshow(FeaturedProductsHolder), 3000);
    }
  }
  
  
  

  let existing_list = localStorage.getItem("FeaturedProductsList");
  
  if (!existing_list) {
    GetFeaturedProducts();
  } else {
    try {
      existing_list = JSON.parse(existing_list);
      PopulateFeaturedProducts(existing_list);
        setTimeout(() => startFeaturedProductsSlideshow(FeaturedProductsHolder), 3000);
    } catch {
      GetFeaturedProducts();
    }
  }
  
  };
  
  
document.addEventListener("DOMContentLoaded", () => {InitiateProductsHandling();  });








  
 



  
 // <!--------FETURED MARKETS HANDLING ---------------------------------------------------------------------------------->
      
      
  

  

function InitiateMarketsHandling(){


const placeholderMarketsObjectsList = [



  {
    MarketName: "OneCart",
    ImageUrl: "https://t3.ftcdn.net/jpg/17/29/32/90/240_F_1729329063_O1ckxG5Odz4P8bOxWU0rlvIdlteXjpOf.jpg",
    MarketUrl: ""
  },
  
  
  {
    MarketName: "Phone Place Kenya ",
    ImageUrl: "https://t3.ftcdn.net/jpg/03/67/42/72/240_F_367427224_PaF49H83VmoIs47Fz1YU1n31PHiipg35.jpg",
    MarketUrl: "https://www.phoneplacekenya.com/shop/"
  },
  {
    MarketName: "Jumia ",
    ImageUrl: "https://t3.ftcdn.net/jpg/16/30/60/64/240_F_1630606464_kcU1KNc1jBX7eg9ANqbM3MTYqysgTyXS.jpg",
    MarketUrl: "https://www.jumia.co.ke/"
  },
  {
    MarketName: "VouGe",
    ImageUrl:" https://t4.ftcdn.net/jpg/02/62/24/31/240_F_262243135_q7xBjfg02gaeD1NVfIqHBLz3qrOMFYcw.jpg",
    MarketUrl: "https://www.vogue.com/shopping/womens/clothing"
  },
  {
    MarketName: "Fitness & Sports",
    ImageUrl: "https://t4.ftcdn.net/jpg/14/64/22/35/240_F_1464223544_8ZTKvmzQLImqD8d1p1Nng6y9LCsBIHRm.jpg",
    MarketUrl: "https://www.decathlon.co.ke/"
  },
  {
    MarketName: "Books & Media",
    ImageUrl: "https://t3.ftcdn.net/jpg/15/62/84/82/240_F_1562848239_AXK68hYry6PTFC4Vqz6fMx1vQjpHuE9V.jpg",
    MarketUrl: "https://bookstop.co.ke/"
  },
  {
    MarketName: "OneCart",
    ImageUrl: "https://t3.ftcdn.net/jpg/17/29/32/90/240_F_1729329063_O1ckxG5Odz4P8bOxWU0rlvIdlteXjpOf.jpg",
    MarketUrl: ""
  },
  
  
  {
    MarketName: "Phone Place Kenya ",
    ImageUrl: "https://t3.ftcdn.net/jpg/03/67/42/72/240_F_367427224_PaF49H83VmoIs47Fz1YU1n31PHiipg35.jpg",
    MarketUrl: "https://www.phoneplacekenya.com/shop/"
  }
  
];



    let FeaturedMarketsHolder = document.getElementById("featuredMarketsContainer");
    
    if (!FeaturedMarketsHolder) {
        console.error("Container element not found!");
        return;
    }




    FeaturedMarketsHolder.innerHTML = ``;
async function PopulateFeaturedMarkets(MarketsObjectsList) {
  if (!MarketsObjectsList || !MarketsObjectsList.length) return;

  for (let Market of MarketsObjectsList) {
    const FeaturedMarketCard = document.createElement("div");

    FeaturedMarketCard.className = `
      min-w-[60%] max-w-[60%] md:min-w-[20%] md:max-w-[20%] h-[220px]
      rounded-2xl overflow-hidden relative group cursor-pointer
      bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900
      border border-white/10
      shadow-[0_4px_15px_rgba(0,0,0,0.4)]
      hover:border-cyan-400/60
      hover:shadow-[0_0_35px_rgba(56,189,248,0.45)]
      hover:from-gray-800 hover:via-gray-900 hover:to-gray-800
      transition-all duration-500 ease-[cubic-bezier(0.4,0,0.2,1)]
      backdrop-blur-xl
    `;

    FeaturedMarketCard.innerHTML = `
      <!-- Glow background -->
      <span class="absolute inset-0 rounded-2xl bg-cyan-400/10 opacity-0 
                   group-hover:opacity-100 blur-2xl transition-opacity duration-700"></span>

      <!-- Market image -->
      <img src="${Market.ImageUrl}" alt="${Market.MarketName}"
           class="w-full h-full object-cover rounded-2xl
           opacity-80 group-hover:opacity-100 group-hover:scale-105
           transition-transform duration-700 ease-[cubic-bezier(0.4,0,0.2,1)]" />

      <!-- Overlay gradient -->
      <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/10 to-transparent"></div>

      <!-- Text content -->
      <div class="absolute bottom-4 left-6 text-white z-10">
        <h3 class="text-lg font-semibold tracking-wide drop-shadow-md group-hover:text-cyan-300 transition-colors duration-500">
          Explore The Best Deals on ${Market.MarketName}
        </h3>
        <p class="text-sm text-cyan-400/90">Curated by OneCart</p>
      </div>
    `;

    // Make whole card clickable
    FeaturedMarketCard.addEventListener("click", () => {
      window.location.href = Market.MarketUrl;
    });

    FeaturedMarketsHolder.appendChild(FeaturedMarketCard);
  }
}




function startSlideshow(container, interval = 4000) {
  let scrollAmount = 0;
  let cardWidth = container.children[0].offsetWidth + 16; // 16 = gap between cards
  let totalCards = container.children.length;

  setInterval(() => {
    scrollAmount += cardWidth;
    
    // Reset scroll if end is reached
    if (scrollAmount >= cardWidth * totalCards) {
      scrollAmount = 0;
    }

    container.scrollTo({
      left: scrollAmount,
      behavior: "smooth"
    });
  }, interval);
}





    async function GetFeaturedMarkets() {
        const url = "YOUR_API_ENDPOINT_HERE";
        try {
            let response = await fetch(url, { method: "GET" });
            if (response.ok) {
                let data = await response.json();
                localStorage.setItem("FeaturedMarketsObjetsArray", JSON.stringify(data));
                PopulateFeaturedMarkets(data);
            } else {
                console.error("Failed to fetch markets");
               PopulateFeaturedMarkets( placeholderMarketsObjectsList) 
              startSlideshow(FeaturedMarketsHolder);
            }
        } catch (error) {
            console.error("Fetch error:", error);
        }
    }


    let existing_list = localStorage.getItem("FeaturedMarketsObjetsArray");
    if (!existing_list) {
        GetFeaturedMarkets();
    } else {
        try {
            existing_list = JSON.parse(existing_list);
            PopulateFeaturedMarkets(existing_list);

        } catch {
            GetFeaturedMarkets();
        }
    }

}


document.addEventListener("DOMContentLoaded", () => {InitiateMarketsHandling();  });














  

  
// load selections-dynamic selection navigation options 

function LoadSelectionOption() {
  const mainSelectionsNav = document.getElementById("SelectionsNav");
  if (!mainSelectionsNav) return;

  const containerMainSelections = document.createElement("div");
  containerMainSelections.className = `
    py-2 px-3 bg-[transparent] gap-x-6 
    flex flex-row items-center justify-start overflow-x-auto scrollbar-hide
  `;

const selections = [
  {
    title: "Featured Products",
    selection_categorization: "featured",
    selection_id: "featured-products",
    description: "Top recommended products",
    icon: "🔥",
    market_url: null,
    scroll_or_load_url: null,
    action_type: "scroll",
    style: "highlighted",
    enabled: true
  },
  {
    title: "Top Deals",
    selection_categorization: "deals",
    selection_id: "top-deals",
    description: "Current sales and limited-time offers",
    icon: "💰",
    market_url: null,
    scroll_or_load_url: "/api/deals",
    action_type: "load",
    style: "sale",
    enabled: true
  },
  {
    title: "Local Markets",
    selection_categorization: "markets",
    selection_id: "local-markets",
    description: "Browse trusted local sellers",
    icon: "🛒",
    market_url: "https://example.com/markets",
    scroll_or_load_url: null,
    action_type: "link",
    style: "default",
    enabled: true
  },
  {
    title: "Fashion & Style",
    selection_categorization: "fashion",
    selection_id: "fashion-style",
    description: "Latest in fashion trends",
    icon: "👗",
    market_url: null,
    scroll_or_load_url: "/api/fashion",
    action_type: "load",
    style: "fashion",
    enabled: true
  },
  {
    title: "Electronics",
    selection_categorization: "electronics",
    selection_id: "electronics-section",
    description: "Smartphones, laptops, and gadgets",
    icon: "🔌",
    market_url: null,
    scroll_or_load_url: "/api/electronics",
    action_type: "load",
    style: "tech",
    enabled: true
  },
  {
    title: "Books & Media",
    selection_categorization: "books",
    selection_id: "books-media",
    description: "Books, audiobooks, and movies",
    icon: "📚",
    market_url: null,
    scroll_or_load_url: "/api/books",
    action_type: "load",
    style: "media",
    enabled: false
  },
  // New categories added below
  {
    title: "Home & Garden",
    selection_categorization: "home-garden",
    selection_id: "home-garden",
    description: "Furniture, decor, and outdoor essentials",
    icon: "🏡",
    market_url: null,
    scroll_or_load_url: "/api/home-garden",
    action_type: "load",
    style: "home",
    enabled: true
  },
  {
    title: "Health & Wellness",
    selection_categorization: "health-wellness",
    selection_id: "health-wellness",
    description: "Fitness, supplements, and personal care",
    icon: "💪",
    market_url: null,
    scroll_or_load_url: "/api/health-wellness",
    action_type: "load",
    style: "health",
    enabled: true
  },
  {
    title: "Sports & Outdoors",
    selection_categorization: "sports-outdoors",
    selection_id: "sports-outdoors",
    description: "Gear and apparel for active lifestyles",
    icon: "⚽",
    market_url: null,
    scroll_or_load_url: "/api/sports-outdoors",
    action_type: "load",
    style: "sports",
    enabled: true
  },
  {
    title: "Toys & Games",
    selection_categorization: "toys-games",
    selection_id: "toys-games",
    description: "Fun and games for all ages",
    icon: "🧸",
    market_url: null,
    scroll_or_load_url: "/api/toys-games",
    action_type: "load",
    style: "fun",
    enabled: true
  }
];



  for (let selection of selections) {
    if (!selection.enabled) continue;

    const selectionButton = document.createElement("button");
    selectionButton.className = `
      text-white px-4 py-4  rounded-full bg-orange-500 italic hover:bg-orange-600 
      transition-all duration-300 text-xs  whitespace-nowrap
    `;
    selectionButton.innerText = `${selection.icon ?? ""} ${selection.title}`;
    selectionButton.title = selection.description ?? "";

    // You can add a click handler here based on action_type if needed
    containerMainSelections.appendChild(selectionButton);
  }

  mainSelectionsNav.appendChild(containerMainSelections);

  // ✅ Now containerMainSelections is defined, so we can run the slideshow here
  setTimeout(() => {
    startSlideshow2(containerMainSelections);
  }, 2000);
}

function startSlideshow2(container, interval = 6000) {
  if (!container || container.children.length === 0) return;

  let scrollAmount = 0;
  let cardWidth = container.children[0].offsetWidth + 16;
  let totalCards = container.children.length;
  let maxScroll = (cardWidth * totalCards) - container.offsetWidth;

  setInterval(() => {
    scrollAmount += cardWidth;

    if (scrollAmount > maxScroll) {
      scrollAmount = 0;
    }

    container.scrollTo({
      left: scrollAmount,
      behavior: "smooth"
    });
  }, interval);
}

document.addEventListener("DOMContentLoaded", () => {
  LoadSelectionOption();
});



  






