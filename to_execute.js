var comments = document.getElementsByTagName("ul")[0];
var i = comments.childNodes.length;
while (i--)
    comments.appendChild(comments.childNodes[i]);