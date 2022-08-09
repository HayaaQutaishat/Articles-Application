document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', changeBg);

})

function changeBg() {
    var x = window.scrollY;
    console.log(x);
}