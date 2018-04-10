var popup = document.getElementsByClassName('_2pnef');

try {
    popup[0].style.visibility = 'hidden';
} catch (e) {
    console.log(e);
}

var comments = document.getElementsByTagName('ul')[0];
var i = comments.childNodes.length;
while (i--) {
    comments.appendChild(comments.childNodes[i]);
}