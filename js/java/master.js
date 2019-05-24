sw = screen.width;
sh = screen.height;

// Brainy Things
brain = document.getElementById('brainyThings');
// 60% screen width and width of text is 5 times its height
brain.style.fontSize = sw * 0.6 / 5 + 'px';
brain.style.margin = '0px ' + sw * 0.03 + 'px';
brain.style.lineHeight = sw * 0.2 + 'px';

// Logo image
logo = document.getElementById('logo');
logo.style.height = sw * 0.2 + 'px';
logo.style.width = sw * 0.2 + 'px';
logo.style.margin = '0px ' + sw * 0.03 + 'px';

// Class Name
cls = document.getElementById('clsName');
clsSpan = document.querySelector('#clsName span');
clsSpanLen = clsSpan.innerHTML.length;
if (clsSpanLen < 20) {
  cls.style.fontSize = (sw * 0.6 / Math.max(10, clsSpanLen) * 2) + 'px';
} else {
  cls.style.fontSize = (sw * 0.8 / clsSpanLen * 2) + 'px';
}

// Package Name
pkg = document.getElementById('pkgName');
pkgSpan = document.querySelector('#pkgName span');
pkgSpanIn = pkgSpan.innerHTML.trim();
pkgSpanLen = 9;
for (i = 0; i < pkgSpanIn.length; i++) {
  if (pkgSpanIn[i] == '<') {
    while (pkgSpanIn[++i] != '>');
    i++;
  }
  pkgSpanLen++;
}
if (pkgSpanLen < 20) {
  pkg.style.fontSize = (sw * 0.6 / Math.max(10, pkgSpanLen) * 2) + 'px';
} else {
  pkg.style.fontSize = (sw * 0.8 / pkgSpanLen * 2) + 'px';
}

// Extends
ext = document.getElementById('extends');
ext.style.fontSize = pkg.style.fontSize;

function changeArrow(e, x) {
  s = e.parentNode.childNodes[1].innerHTML; //childNodes[0] is text between tags
  if (s[0] == '\u25be' || s[0] == '\u25b4') {
    e.parentNode.childNodes[1].innerHTML = '&#' + x + ';' + s.slice(1, s.length);
  } else {
    e.parentNode.childNodes[1].innerHTML = s.slice(0, -1) + '&#' + x + ';';
  }
}

// Visible Invisible Toggle
vis = document.getElementsByClassName('visible');
for (var i = 0; i < vis.length; i++) {
  vis[i].onclick = function makeVis(){
    this.nextSibling/*text b/w tags*/.nextSibling.style.display = "block";
    changeArrow(this, 9652);
    this.onclick = function makeInv() {
      this.nextSibling.nextSibling.style.display = "none";
      changeArrow(this, 9662);
      this.onclick = makeVis;
    };
  };
}