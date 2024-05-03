let coord;
navigator.geolocation.getCurrentPosition((val => {
coord = [val.coords.latitude, val.coords.longitude];
        
// click button callback:
let clickcb = () => {
    console.log("clicked");
}
}))