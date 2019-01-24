function hello(id){
    let links=document.links;
    for (var i=0; i<links.length; i++){
        if (links[i].id == id){
            break;
        }
        if ((links[i].id != "") && !(links[i].classList.contains("Interested") || links[i].classList.contains("Satisfied"))) {
            url = "http://www.josh-moses.com/not-interested/" + links[i].href.slice("http://www.josh-moses.com/wiki/".length).split('#')[0];
            fetch(url);
        }
    }
}

function satisfied() {
    let links=document.links;
    for (var i=0; i<links.length; i++){
        // Todo: Need to refresh first!
        if ((links[i].id != "") && !(links[i].classList.contains("Interested") || links[i].classList.contains("Satisfied"))) {
            url = "http://www.josh-moses.com/not-interested/" + links[i].href.slice("http://www.josh-moses.com/wiki/".length).split('#')[0];
            fetch(url);
        }
    }

    url = "http://www.josh-moses.com/satisfied/" + window.location.href.slice("http://www.josh-moses.com/wiki/".length).split('#')[0];
    fetch(url);
}
  