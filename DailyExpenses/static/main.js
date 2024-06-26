 document.addEventListener("DOMContentLoaded", function (event) {
     const showNavbar = (toggleId, navId, bodyId, headerId) => {
         const toggle = document.getElementById(toggleId),
         nav = document.getElementById(navId),
         bodypd = document.getElementById(bodyId),
         headerpd = document.getElementById(headerId)

             // Validate that all variables exist
             if (toggle && nav && bodypd && headerpd) {
                 toggle.addEventListener('click', () => {
                     // show navbar
                     nav.classList.toggle('show')
                     // change icon
                     toggle.classList.toggle('bx-x')
                     // add padding to body
                     bodypd.classList.toggle('body-pd')
                     // add padding to header
                     headerpd.classList.toggle('body-pd')
                 })
             }
     }

     showNavbar('header-toggle', 'nav-bar', 'body-pd', 'header')

     /*===== LINK ACTIVE =====*/
     const linkColor = document.querySelectorAll('.nav_link')
     var selectedLink = (location.pathname+location.search).substr(1);
     selectedLink = selectedLink.trim()==""?"home":selectedLink;
     function colorLink() {
         if (linkColor) {
             linkColor.forEach(l => l.classList.remove('active'))
             $("."+selectedLink).addClass('active');
         }
     }
     colorLink();
//     linkColor.forEach(l => l.addEventListener('click', colorLink))

     // Your code to run since DOM is loaded and ready


     var myLink = document.querySelectorAll('a[href="#"]');
     myLink.forEach(function (link) {
         link.addEventListener('click', function (e) {
             e.preventDefault();
         });
     });

    var timeout_id = 0,
    hold_time = 1000,
    hold_trigger = $('article');

    hold_trigger.mousedown(function() {
     timeout_id = setTimeout(triggerDelete, hold_time);
    }).bind('mouseup mouseleave', function() {
     clearTimeout(timeout_id);
    });

    function triggerDelete() {
    // location.replace("https://www.w3schools.com");
    }

    });