var java = document.getElementsByClassName('java');
var py = document.getElementsByClassName('python');
for (let i = 0; i < java.length; i++) {
    java[i].addEventListener('click', () => {
        for (let j = 0; j < java.length; j++) {
            java[j].style.animationPlayState = 'running';
        }
        for (let j = 0; j < py.length; j++) {
            py[j].style.display = 'none';
        }
    });
}

for (let i = 0; i < py.length; i++) {
    py[i].addEventListener('click', () => {
        for (let j = 0; j < py.length; j++) {
            py[j].style.animationPlayState = 'running';
        }
        for (let j = 0; j < java.length; j++) {
            java[j].style.display = 'none';
        }
    });
}