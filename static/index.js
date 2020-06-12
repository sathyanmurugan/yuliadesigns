
const logoAnimation = anime.timeline({
  autoplay: true,
  delay: 200
});

logoAnimation.add({
  targets: '#img-group',
  translateY: [-100, 0],
  opacity: [0, 1],
  elasticity: 800,
  duration: 1600
}).add({
  targets: '#img-portfolio',
  rotate: [-20, 0],
  duration: 1600,
  elasticity: 800,
  offset: 100
})


$(".nav-link").click(function() {
    $('html,body').animate({
        scrollTop: $(".page-footer").offset().top},
        'slow');
});

$(".img-arrow").click(function() {
    $('html,body').animate({
        scrollTop: $(".folio-start").offset().top -300},
        'slow');
});
//
// const span = document.querySelector(".font-awesome");
//
// span.onclick = function() {
//   document.execCommand("copy");
// }
//
// span.addEventListener("copy", function(event) {
//   event.preventDefault();
//   if (event.clipboardData) {
//     event.clipboardData.setData("text/plain", span.textContent);
//     console.log(event.clipboardData.getData("text"))
//   }
// });
