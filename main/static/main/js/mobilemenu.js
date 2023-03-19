const element = document.getElementsByClassName('toogleMenu')[0];
element.addEventListener('click', function() {
  const aside = document.querySelector('aside');
//   console.log(aside.style.display)
  if (aside.style.display === "block") {
    aside.style.display = "none";
  }
  else {
    aside.style.display = "block";
  }

});

// document.addEventListener('click', function(event) {
//     const aside = document.querySelector('aside');
//     const asideList = aside.querySelector('ul');
//     if (event.target != element){
//         if (!asideList.contains(event.target) && aside.style.display === "block") {
//             aside.style.display = "none";
//         }
//     }

// });
