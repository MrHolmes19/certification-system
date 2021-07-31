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
["2", "1", ["Asientos"], ["Debe verse los cinturones"]],
["3", "2", ["Equipo de frio", "Caja con equipo"], ["Debe verse la unidad exterior","Debe verse la unidad interior"]],
];

var finalType =  document.querySelector("#id_final_type");

finalType.addEventListener("change", function() {showCards()});

var cards = document.querySelectorAll(".card");

function showCards(){
    type_selected = finalType.value;
    typesInfo.forEach(type => {
        if(type_selected == type[0]){
            for(i=1; i<=5+type[1];i++){
                cards[i].removeAttribute('class','d-none')
            }
        }
    });
};