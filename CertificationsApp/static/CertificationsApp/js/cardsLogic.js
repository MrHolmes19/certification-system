//var cards = document.getElementsByClassName("card")

// giving id to cards

var images = document.querySelectorAll(".card img");

i = 1;

images.forEach(image => {
    image.setAttribute('id','image_' + i);
    i++;
    
});

// setting preview images when uploading

var imageInputs = document.querySelectorAll(".card input");

i = 1;

imageInputs.forEach(input => {
    input.setAttribute('onchange','document.getElementById("image_' + i + '").src = window.URL.createObjectURL(this.files[0])');
    i++;
    
});

// setting preview images when uploading

typesInfo = [
["1", "0", [], []],
["2", "2", ["Equipo de frio", "Caja con equipo"], ["Debe verse la unidad exterior","Debe verse la unidad interior"]],
["3", "1", ["Asientos"], ["Debe verse los cinturones"]],
];

var finalType =  document.querySelector("#id_final_type");

finalType.addEventListener("change", function() {showCards()});

var cards = document.querySelectorAll(".card");

function showCards(){
    for(i=0; i<7; i++){
        cards[i].setAttribute('class','d-none')
    }
    //cards.setAttribute('class','d-none')
    type_selected = finalType.value;
    typesInfo.forEach(type => {
        if(type_selected == type[0]){
            typeqt = parseInt(type[1]) + 4
            for(var i=0; i<=typeqt;i++){
                cards[i].removeAttribute('class','d-none')
            }
        }
    });
};