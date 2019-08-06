/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
document.querySelector('a.icon').addEventListener('click', () => {
  let navUl = document.querySelector('#myTopnav');
  let sidebar = document.querySelector('#mySidebar');
  if(navUl.className === 'topnav' & sidebar.className === 'sidebar') {
    navUl.className += ' responsive';
    sidebar.className += ' responsive';
  } else {
    navUl.className = 'topnav';
    sidebar.className = 'sidebar';
  }
});

let sidebarLinks = document.querySelectorAll('.sidebar a')
// when the cursor is moved over thr links of the sidebar, a small text pop up
Array.from(sidebarLinks).forEach( a => {
  a.onmouseover = event => {
    event.preventDefault();
    if (!document.querySelector('body span')){
      let span = document.createElement('span');
      span.textContent = a.getAttribute('data-text');
      span.className = 'show-text';
      span.style.left = `${event.x + 21}px`;
      span.style.top = `${event.y + 21}px`;
      document.body.appendChild(span);
    };
  };
});
// AFter the cursor is moved over thr links of the sidebar, a small text is removed
Array.from(sidebarLinks).forEach( a => {
  a.onmouseout = event => {
    event.preventDefault();
    let span = document.querySelector('body span');
    if (span){
      document.body.removeChild(span);
    };
  };
});
