var popup = document.getElementsByClassName('_2pnef');
if (popup !== null) {
    popup[0].style.visibility = 'hidden';
}

var comments = document.getElementsByTagName('ul')[0];
var i = comments.childNodes.length;
while (i--) {
    comments.appendChild(comments.childNodes[i]);
}