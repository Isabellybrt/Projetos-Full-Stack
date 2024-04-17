var sidebar = document.getElementById("sidebar");
var openButton = document.getElementById("abrirmenu");
sidebar.style.display = "none";
openButton.style.display = "block";

function show() {
    sidebar.style.display = "block";
    openButton.style.display = "none";
  }
  
  function hide() {
    sidebar.style.display = "none";
    openButton.style.display = "block";
  }