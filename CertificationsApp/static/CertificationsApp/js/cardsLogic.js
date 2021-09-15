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
    //input.setAttribute('onchange','document.getElementById("image_' + i + '").style.backgroundColor = "yellow"');
    i++;
    
});

// setting preview images when uploading (hardcoded)

typesInfo = [
["1", "0", ["Cerramiento"], ["Debe verse el interior de la cabina"]], //Furgon
["2", "1", ["Caja aislada"], ["Debe verse la cabinada con material aislante"]],  //Furgon termico
["3", "1", ["Asientos"], ["Debe verse los cinturones"]],  //Furgon con asientos
["4", "0", [], []],  //Cabina simple
["5", "1", ["Vidros"], ["Deben verse los vidrios"]],  //Furgon vidriado
["6", "2", ["Asientos","Vidros"], ["Debe verse los cinturones","Deben verse los vidrios"]],  //Furgon vidriado con asientos
["7", "2", ["Asientos","interior"], ["Debe verse los cinturones","debe mostrarse el interior"]],  //Casa rodante motorizada
["8", "2", ["Equipo de frio", "Caja con equipo"], ["Debe verse la unidad exterior","Debe verse la unidad interior"]],  //Furgon termico con equipo de frio
["9", "2", ["Enganche mecanico", "Conexion electrica"], ["Debe verse el dispositivo de enganche mecanico","Debe verse el dispositivo de conexion electrica"]],  //Trailer
];

var finalType =  document.querySelector("#id_final_type");

finalType.addEventListener("change", function() {showCards()});

var cards = document.querySelectorAll(".card");

function showCards(){
    for(i=0; i<7; i++){
        console.log(i)
        try{
            cards[i].setAttribute('class','carta card my-2 border-secondary opacity-50 d-none')
        }
        catch{
            console.log("error")
        }
    }
    //cards.setAttribute('class','d-none')
    type_selected = finalType.value;
    typesInfo.forEach(type => {
        if(type_selected == type[0]){
            typeqt = parseInt(type[1]) + 4
            for(var i=0; i<=typeqt;i++){
                //CAMBIAR!! Usar .classList.add("d-none")
                cards[i].removeAttribute('class','d-none')
                cards[i].setAttribute('class','carta card my-2 border-secondary')
            }
        }
    });
};


showCards()

//block all inputs except those how need to be updated
var current_url = window.location.pathname

path_length = current_url.length
console.log(path_length)


//encontrar otra forma de hacer esto
if(path_length > 12 && path_length < 20){
    block_inputs()
} else {
    console.log("inputs not blocked")
}

text_inputs = document.querySelectorAll('input')
selects = document.querySelectorAll('select')

function block_inputs(){
    text_inputs.forEach(input => {
        input.setAttribute("disabled", true)
    });
    selects.forEach(input => {
        input.setAttribute("disabled", true)
    });

    cards.forEach(card => {
        card_src = card.querySelector('img').src
        card_src = card_src.split("/")
        card_src = card_src[card_src.length-1]

        if(card_src == "volver_a_subir.jpeg"){
            input = card.querySelector('input')
            input.removeAttribute("disabled")
        }
    });
}


