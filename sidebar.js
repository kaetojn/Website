/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidebar").style.width = "20vh";
  document.getElementById("main").style.marginLeft = "20vh";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

function toggleNav() {
	if (document.getElementById("mySidebar").style.width === "0px") {
		openNav();
	}
	else{
		closeNav();
	}
}