






/* ==========================================================================
   PAGE SESSION MANAGEMENT
   ========================================================================== */

let activeSession = sessionStorage.getItem("ai-pageSession") || "MainPageHeroPage";
sessionStorage.setItem("ai-pageSession", activeSession);

const freshPage = document.getElementById("LoadMainPageFresh");

function manageSession() {
  // Hide all pages
  freshPage.classList.add("hidden");
  document.querySelectorAll(".page").forEach(page => {
    page.classList.add("hidden");
    page.classList.remove("active");
  });

}














/* ==========================================================================
   SEARCH FUNCTIONALITY & RESULTS RENDERING
   ========================================================================== */

const searchBtn = document.getElementById("searchBtn");
const searchInput = document.getElementById("searchInput");
const resultsContainer = document.getElementById("MainResultsPage");
const heroPage = document.getElementById("MainPageHeroPage");


// Sample fallback data
const sampleProducts = [
  { name: "Wireless Headphones", price: "$99", market: "Amazon", image: "https://via.placeholder.com/150" },
  { name: "Smart Watch", price: "$149", market: "Etsy", image: "https://via.placeholder.com/150" },
  { name: "Bluetooth Speaker", price: "$79", market: "Jiji", image: "https://via.placeholder.com/150" }
];



// --- Helper: Star Renderer ---
function renderStars(rating) {
  const full = Math.floor(rating);
  const half = rating % 1 >= 0.5;
  let stars = "★".repeat(full);
  if (half) stars += "½";
  while (stars.length < 5) stars += "☆";
  return `<span class="text-yellow-400 text-sm">${stars}</span>`;
}



// --- Render Product Cards ---
function renderProducts(products, query = "") {
  activeSession = "MainResultsPage";
  sessionStorage.setItem("ai-pageSession", activeSession);

  // Page visibility control
  freshPage.classList.remove("hidden");
  resultsContainer.classList.remove("hidden");
  heroPage.classList.add("hidden");
  DisplaysSection.classList.add("hidden");
  DisplaysSection2.classList.add("hidden");
  selectionNav.classList.add("hidden"); 
  
  

  resultsContainer.innerHTML = "";

  // Query header
  const responseHeader = document.createElement("p");
  responseHeader.className = `
    min-w-fit  overflow-x-auto
    float-left text-sm text-[#1E90FF] font-medium tracking-wide 
    w-full mb-2 px-1 py-3 rounded-xl bg-[#1E90FF1A] border border-[#1E90FF33]
    shadow-lg shadow-[#1E90FF33] hover:shadow-[#1E90FF66] transition-all duration-300
  `.trim();
  responseHeader.innerHTML = `
    🤖 Results For: 
    <span class="text-xs min-w-[fit-content] overflow-x-auto  text-[#FFA500] font-medium  tracking-wide px-4 py-2 rounded-xl bg-[#FFA5001A] border border-[#FFA50033]">
      "${query}"
    </span>
  `;
  resultsContainer.appendChild(responseHeader);

  // Container for cards
  const cardsContainer = document.createElement("div");
  cardsContainer.className = `
    relative flex flex-wrap justify-center items-start gap-8 px-6 py-12 mx-auto md:mx-2 
    bg-[orange]/30 
    backdrop-blur-xl rounded-b-3xl border border-white/10 shadow-inner shadow-cyan-500/10
    overflow-y-auto transition-all duration-500 max-w-8xl min-w-8xl  max-h-[95vh] md:max-h-[82vh]
  `.trim();

  resultsContainer.appendChild(cardsContainer);

  // Render cards
  products.forEach((product, idx) => {
    setTimeout(() => {
      const card = document.createElement("div");
      card.className = `
        ITEMCARD opacity-1 animate-fade-in-up relative overflow-hidden
        bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl
        shadow-[0_0_20px_rgba(56,189,248,0.15)] hover:shadow-[0_0_35px_rgba(56,189,248,0.35)]
        hover:scale-[1.04] hover:border-cyan-400/40 transition-all duration-500 ease-in-out
        p-5 flex flex-col justify-between cursor-pointer group min-h-[360px] max-w-[300px] w-full
      `.trim();

      const img = product.image || product.images?.[0] || "https://via.placeholder.com/150";
      const desc = product.description ? 
        (product.description.length > 80 ? product.description.slice(0, 80) + "..." : product.description) 
        : "No description available.";

      card.innerHTML = `
        <div class="w-full h-[180px] flex items-center justify-center overflow-hidden rounded-md bg-gray-100">
          <img src="${img}" alt="${product.title}" class="object-contain h-full w-full" loading="lazy" />
        </div>
        <div class="mt-4 flex flex-col gap-2 flex-1">
          <h2 class="text-base font-semibold text-[dodgerblue] line-clamp-1">${product.title}</h2>
          <p class="text-sm text-gray-600 line-clamp-2">${desc}</p>
          <p class="text-md font-bold text-green-600 mt-auto">$${product.price?.toFixed?.(2) || product.price || "N/A"}</p>
        </div>
        <button class="mt-4 w-full bg-blue-500 hover:bg-blue-600 text-white text-sm font-medium py-2 px-4 rounded-md transition">
          View Product
        </button>
      `;
      cardsContainer.appendChild(card);
    }, idx * 200);
  });
}











/* ==========================================================================
   MODAL HANDLING (LOADER)
   ========================================================================== */

const modal = document.createElement("div");
modal.className = `
  search-modal fixed top-0 left-0 w-full h-full bg-black/60 flex items-center justify-center z-50
`.trim();

modal.innerHTML = `
  <div class="search-loading bg-transparent mx-2 rounded-lg text-center relative">
    <button id="EXITMODAL" class="hidden absolute top-2 right-2 text-xs bg-red-100 text-red-600 px-3 py-1 rounded-md hover:bg-red-600 hover:text-white transition">
      ✕ Close
    </button>
    <div class="loader-container bg-gray-900 rounded-lg">
      <div class="ai-loader mb-4"><span></span><span></span><span></span><span></span></div>
      <p id="modalMessage" class="loading-text text-xs text-[aliceblue] font-bold py-8 px-6 rounded-3xl">
        Working on your request... please wait
      </p>
    </div>
  </div>
`;
document.body.appendChild(modal);
modal.style.display = "none";

const modalMessage = modal.querySelector("#modalMessage");
const exitModalBtn = modal.querySelector("#EXITMODAL");

function showModal(message = "Working on your request... please wait", showClose = false) {
  modalMessage.textContent = message;
  exitModalBtn.classList.toggle("hidden", !showClose);
  modal.style.display = "flex";
}

function hideModal(delay = 0) {
  setTimeout(() => modal.style.display = "none", delay);
}

exitModalBtn.addEventListener("click", () => hideModal(0));

/* ==========================================================================
   SEARCH LOGIC
   ========================================================================== */

async function makeRequest(query) {
  showModal();

  try {
    const response = await fetch("/core/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });

    if (!response.ok) {
      console.error(`HTTP Error: ${response.status}`);
      showModal("⚠️ Failed to fetch results. Try again later.", true);
      hideModal(2000);
      return;
    }

    const data = await response.json();
    if (data?.aa?.length) {
      renderProducts(data.aa, query);
      window.scrollTo({ top: 250, behavior: "smooth" });
      hideModal();
      searchInput.value = "";
    } else {
      showModal("😕 No matching results found for your query.", true);
      hideModal(2000);
    }

  } catch (err) {
    console.error("Error making request:", err);
    showModal("🚨 An error occurred while searching.", true);
    hideModal(2000);
  }
}

// Trigger search
searchBtn.addEventListener("click", () => {
  const query = searchInput.value.trim().toLowerCase();
  if (!query) return alert("Please enter a search term.");
  makeRequest(query);
});

/* ==========================================================================
   PAGE NAVIGATION
   ========================================================================== */

function navigateTo(pageId) {
  activeSession = pageId;
  sessionStorage.setItem("ai-pageSession", activeSession);

  if (pageId === "MainResultsPage") {
    renderProducts(sampleProducts);
    DisplaysSection.classList.add("hidden");
    freshPage.classList.remove("hidden");
  } else {
    manageSession();
    freshPage.classList.add("hidden");
    DisplaysSection.classList.remove("hidden");
    DisplaysSection2.classList.remove("hidden");
    selectionNav.classList.remove("hidden")
  }
}

/* ==========================================================================
   INITIAL LOAD
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  const sessionPage = sessionStorage.getItem("ai-pageSession");

  if (sessionPage === "MainResultsPage") {
    navigateTo("MainPageHeroPage");
  } else {
    manageSession();
    freshPage.classList.add("hidden");
  }
});
