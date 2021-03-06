
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


// List of type id, amount of photos, title and descriptions for cards (hardcoded)

typesInfo = [
    ["1", "0", CABINA_SIMPLE],
    ["2", "1", FURGON], 
    ["3", "1", FURGON_VIDRIADO],
    ["4", "2", FURGON_VIDRIADO_ASIENTOS],
    ["5", "2", MOTORHOME],
    ["6", "1", FURGON_TERMICO],
    ["7", "2", FURGON_FRIGORIFICO],
    ["8", "2", TRAILER],
];
    
    
// Showing cards depending on client type selection OR when the client comes back after rejected
// select/option logic
var finalType =  document.querySelector("#id_final_type");
finalType.setAttribute("disabled", true)
var originalType =  document.querySelector("#id_original_type");

finalType.addEventListener("change", function() {showCards()});
originalType.addEventListener("change", function() {enableFinal()});

function enableFinal(){
    originalType.getElementsByTagName('option')[0].disabled = true
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
    for(i=0; i<9; i++){
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
            // loop all visible cards and set properties
            for(var i=0; i<=typeqt;i++){
                cards[i].classList.remove('d-none')
                cards[i].setAttribute('class','card my-2 border-secondary')
                inputLabels[i].setAttribute('for','id_image'+ (i+1) +'_uploaded') //Meter condicional en funcion de la URL

                if(i>5){
                    let title = cards[i].querySelector(".card-title")
                    let caption = cards[i].querySelector(".card-text")
                    title.innerHTML = type[2][`picture${i-5}`].title
                    caption.innerHTML = type[2][`picture${i-5}`].caption
                }
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

//encontrar otra forma de hacer esto
if(path_length > 12 && path_length < 15){
    block_inputs()  
} else {
    //alert("is not a number")
}
