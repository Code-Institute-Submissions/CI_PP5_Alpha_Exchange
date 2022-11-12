/**
 * The theme.js file controls the theme switch mode selector.
 */

function isLight() {
    return localStorage.getItem("light-mode"); // Return storage of current of the theme.
  }
  
function toggleRootClass() {
  document.querySelector(":root").classList.toggle("light"); // Toggles current theme.
}
  
// Toggles current local storage variable.
function toggleLocalStorageItem() {
  if (isLight()) {
    localStorage.removeItem("light-mode");
  } else {
    localStorage.setItem("light-mode", "set");
  }
}
  
if (isLight()) {
  toggleRootClass();
}

document.querySelector(".switch").addEventListener("click", () => {
  toggleLocalStorageItem();
  toggleRootClass();
});