
alert("Hello world ? ")


// <!-- SIDEBAR TOGGLE  -->

const toggleBtn = document.getElementById('filterToggle');
const sidebar = document.getElementById('filterSidebar');
const overlay = document.getElementById('filterOverlay');
const closeBtn = document.getElementById('closeFilter');


// Menu Sidebar Controls
const menuToggle = document.getElementById('menuToggle');
const menuSidebar = document.getElementById('menuSidebar');
const menuOverlay = document.getElementById('menuOverlay');
const closeMenu = document.getElementById('closeMenu');



toggleBtn.addEventListener('click', () => {
    sidebar.classList.remove('-translate-x-full');
    overlay.classList.remove('hidden');
    menuSidebar.classList.add('translate-x-full');
    menuOverlay.classList.add('hidden');
});







menuToggle.addEventListener('click', () => {
    menuSidebar.classList.remove('translate-x-full');
    menuOverlay.classList.remove('hidden');
    sidebar.classList.add('-translate-x-full');
    overlay.classList.add('hidden');
});


//close menu 
closeMenu.addEventListener('click', () => {
    menuSidebar.classList.add('translate-x-full');
    menuOverlay.classList.add('hidden');
});

menuOverlay.addEventListener('click', () => {
    menuSidebar.classList.add('translate-x-full');
    menuOverlay.classList.add('hidden');
});


//close sidebar 
closeBtn.addEventListener('click', () => {
    sidebar.classList.add('-translate-x-full');
    overlay.classList.add('hidden');
});

overlay.addEventListener('click', () => {
    sidebar.classList.add('-translate-x-full');
    overlay.classList.add('hidden');
});









