var toggle = true;

function toggleClass(target, classToToggle) {
  if (toggle) {
    target.addClass(classToToggle);
    toggle = false;
  }
  else {
    target.removeClass(classToToggle);
    toggle = true;
  }
}

$(document).ready(function() {
  console.log("ready!");

// Adds a color to the dropdown menu button when clicked...

  $("#drop-down-btn").click(function() {
    $(".menu-list").slideToggle();
    toggleClass($(this), "color-dropdown-btn");
  });

// Fades out any messages that are being displayed when the butoon of that message is clicked...

  $("#continue").click(function() {
    $(".continue").fadeOut(2000);
  });

// Fades out any messages that need to be temporarily displayed during gameplay...

  setTimeout(function() {
    $(".fade-out").fadeOut(2000);
  }, 5000);


// Scrolls directly to welcome message on home page if player is logged in...

  document.getElementById('home-header').scrollIntoView();

});
