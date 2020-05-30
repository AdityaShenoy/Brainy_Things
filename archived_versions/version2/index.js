var compScreen = document.getElementById('compScreen');
var logo = document.getElementById('logo');
compScreen.addEventListener('click', () => {
    compScreen.style.animationPlayState = "running";
    logo.style.animationName = "shrinkLogo";
    logo.style.animationDuration = "2s";
    setTimeout(() => {
        window.location = "programming/programming.html";
    }, 2000);
});