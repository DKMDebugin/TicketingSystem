/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
document.querySelector('a.icon').addEventListener('click', () => {
  let navUl = document.querySelector('#myTopnav');
  if(navUl.className === 'topnav') {
    navUl.className += ' responsive';
  } else {
    navUl.className = 'nav';
  }
});
