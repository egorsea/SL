const element = document.getElementsByClassName('toogleMenu')[0];
const aside = document.querySelector('aside');

element.addEventListener('click', function() {
  aside.style.display = aside.style.display === "block" ?  "none": "block";
});

document.addEventListener('click', function(event) {

    const asideList = aside.querySelector('ul');
    if (event.target != element){
        if (!asideList.contains(event.target) && aside.style.display === "block") {
            event.preventDefault();

            aside.style.display = "none";
        }
    }

});
