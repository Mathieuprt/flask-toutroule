// MENU

const toggleMenu = document.querySelector('.toggle-menu');
const menu = document.querySelector('.main-menu');

toggleMenu.addEventListener('click', function () {
  const open = JSON.parse(toggleMenu.getAttribute('aria-expanded'));
  toggleMenu.setAttribute('aria-expanded', !open);
  toggleMenu.classList.toggle('active');
  menu.hidden = !menu.hidden;
  menu.classList.toggle('opened')
  document.body.classList.toggle('noscroll');

  if (!menu.hidden) {
    menu.querySelector('a').focus();
  }
});