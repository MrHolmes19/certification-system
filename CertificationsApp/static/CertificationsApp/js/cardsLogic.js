
// giving id to cards

var images = document.querySelectorAll(".card img");

i = 1;

images.forEach(image => {
    image.setAttribute('id','image_' + i);
    i++;   
});

// giving id to input labels

var inputLabels = document.querySelectorAll(".card .container label");

i = 1;

inputLabels.forEach(inputLabel => {
    inputLabel.setAttribute('id','label_' + i);
    i++; 
});

// giving id to card's overlay

var overlays = document.querySelectorAll(".card .container .overlay");

i = 1;

overlays.forEach(overlay => {
    overlay.setAttribute('id','overlay_' + i);
    i++; 
});


// List of types for cards descriptions (hardcoded)

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
    
// Showing cards depending on client type selection OR when the client comes back after rejected

var finalType =  document.querySelector("#id_final_type");
finalType.setAttribute("disabled", true)
var originalType =  document.querySelector("#id_original_type");

finalType.addEventListener("change", function() {showCards()});
originalType.addEventListener("change", function() {enableFinal()});

function enableFinal(){
    finalType.removeAttribute("disabled")
    finalType.getElementsByTagName('option')[0].selected = 'selected'
    showCards()
    block_same_type(originalType.value)
}

var cards = document.querySelectorAll(".card");
var inputLabels = document.querySelectorAll(".card .container label");
/* Si se quiere cambiar el label al boton usar:
var inputLabels = document.querySelectorAll(".card .card-body .container label");
*/

function block_same_type(type){
    options = finalType.getElementsByTagName('option')
    Array.from(options).forEach(opt => {
        opt.disabled = false;
    });

    finalType.getElementsByTagName('option')[type].disabled = true
}
function showCards(){
    for(i=0; i<8; i++){
        try{
            cards[i].setAttribute('class','card my-2 border-secondary d-none')
        }
        catch{
            console.log("error")
        }
    }
    //cards.setAttribute('class','d-none')
    type_selected = finalType.value;
    typesInfo.forEach(type => {
        if(type_selected == type[0]){
            typeqt = parseInt(type[1]) + 5
            for(var i=0; i<=typeqt;i++){
                cards[i].classList.remove('d-none')
                cards[i].setAttribute('class','card my-2 border-secondary')
                inputLabels[i].setAttribute('for','id_image'+ (i+1) +'_uploaded') //Meter condicional en funcion de la URL
            }
        }
    });
};

showCards()
    

// setting preview images when uploading

var imageInputs = document.querySelectorAll(".card input");

i = 1;
imageInputs.forEach(input => {
    input.setAttribute('onchange','document.getElementById("image_' + i + '").src = window.URL.createObjectURL(this.files[0])');
    i++;  
});

// Changing format when uploading

var labelInputs = document.querySelectorAll(".card .container label");

i = 1;
labelInputs.forEach(label => {
    label.setAttribute('onclick','document.getElementById("label_' + i + '").classList.add("inactive")');
    i++;  
});


// INTENTO 1 - FUNCIONES POR SEPARADO (SUPUESTAMENTE DEBERIA ANDAR) 

/*
function hiddeLabel(i){
    document.getElementById('label_' + i).classList.add("inactive");
}

function showPreview(i){
    document.getElementById('image_' + i).src = window.URL.createObjectURL(files[0]);
}

function allInOne(i){
    hiddeLabel(i);
    showPreview(i);
}

imageInputs.forEach(input => {
    input.setAttribute(
        'onchange',
        'document.getElementById("image_' + i + '").src = window.URL.createObjectURL(this.files[0])',
        'document.getElementById("label_' + i + '").classList.add("inactive")'
    );
    
    //input.setAttribute('onchange',this.hiddeLabel(i), this.showPreview(i));
    //input.setAttribute('onchange',function() {hiddeLabel(i),showPreview(i)});
    input.setAttribute('onchange',(function() {allInOne(i)})());
    i++;  
});


// INTENTO 2 - Con un EventListener pasandole parametros via funciones

/*
var alcambio = function(){
    document.getElementById("label_"+ i).classList.add("inactive");
    document.getElementById("overlay_" + i).classList.add("inactive2");
}

var labelInputs = document.querySelectorAll(".card .container label");

i = 1;

labelInputs.forEach(label => {
    label.addEventListener("click", alcambio(i));
    i++;
});

*/

//block all inputs except those how need to be updated

text_inputs = document.querySelectorAll('input:not([type="hidden"])');

selects = document.querySelectorAll('select');

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
            input.setAttribute("required", true)
        } else {
            card.querySelector("label").classList.add("inactive");
            card.querySelector(".overlay").classList.remove("overlay");
        }
    });
}

var current_url = window.location.pathname

path_length = current_url.length
//console.log(path_length)


//encontrar otra forma de hacer esto
if(path_length > 12 && path_length < 15){
    block_inputs()  
} else {
    //alert("is not a number")
}
