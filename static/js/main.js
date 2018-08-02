var toggle = true;

function toggleClass(target, classToToggle){
  if (toggle){
    target.addClass(classToToggle);
    toggle = false;
  } else {
    target.removeClass(classToToggle);
    toggle = true;
  }
}

$(document).ready(function() {
  console.log("ready!");

  $("#drop-down-btn").click(function() {
    $(".menu-list").slideToggle();
    toggleClass($(this), "test");
  });

  document.getElementById('home-header').scrollIntoView();

});
