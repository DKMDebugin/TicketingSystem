'use strict';

let navUl = document.querySelector('#myTopnav');
let sidebar = document.querySelector('#mySidebar');
let sidebarLinks = document.querySelectorAll('.sidebar a');

// Reposition the sidebar when the nav bar resizes
// a custome event for heightChange
$('#myTopnav').bind('heightChange', () => {
  let height = getComputedStyle(navUl).height;
  sidebar.style.top = `${height}`;
});

/* Toggle between adding and removing the "responsive" class to
topnav when the user clicks on the icon */
document.querySelector('a.icon').addEventListener('click', () => {
  if(navUl.className === 'topnav' & sidebar.className === 'sidebar') {
    navUl.className += ' responsive';
    // navUl.style['max-width'] = window.innerWidth;
    sidebar.className += ' responsive';
  } else {
    navUl.className = 'topnav';
    sidebar.className = 'sidebar';
  }
  // trigger heightChange event
  $('#myTopnav').trigger('heightChange');
});

// when the cursor is moved over thr links of the sidebar, a small text pop up
// Ti limit the functionality to pcs
if (window.innerWidth >= 960) {
  Array.from(sidebarLinks).forEach( a => {
    a.onmouseover = event => {
      // get location of the element
      let linkPos = a.getBoundingClientRect()

      if (!document.querySelector('body span')){
        let span = document.createElement('span');
        span.textContent = a.getAttribute('data-text');
        span.className = 'show-text';
        span.style.left = `${linkPos.x + 30}px`;
        span.style.top = `${linkPos.y + 30}px`;
        document.body.appendChild(span);
      };
    };
  });

  // After the cursor is moved over thr links of the sidebar, a small text is removed
  Array.from(sidebarLinks).forEach( a => {
    a.onmouseout = event => {
      // event.preventDefault();
      let span = document.querySelector('body span');
      if (span){
        document.body.removeChild(span);
      };
    };
  });
}
