
botonEnviar = document.querySelector("#submit")

message = "Gracias por completar el formulario."
speech = new SpeechSynthesisUtterance(message);
speech.rate = 0.7;
speech.pitch = 1;

/*
let list_voices = window.speechSynthesis.getVoices();
setTimeout (()=>{
    alert(list_voices)
    for(var i = 0; i < list_voices.length; i++) {
        console.log(i)
    }
}, 5000);
*/

window.speechSynthesis.onvoiceschanged = function() {
    list_voices = window.speechSynthesis.getVoices();
    // alert(list_voices)
    // for(var i = 0; i < list_voices.length; i++) {
    //     console.log(list_voices[i])
    // }
    speech.voice = list_voices[1]
};

//message.voice = list_voices[1]
const thanks = (message) =>
    //window.SpeechSynthesis.speak(new SpeechSynthesisUtterance(message))

    //speech = new SpeechSynthesisUtterance(message);

    //window.SpeechSynthesis.speak(speech);
    //window.speechSynthesis.speak(speech);
    //speechSynthesis.speak(speech);

    window.speechSynthesis.speak(speech);

//botonEnviar.addEventListener("click", thanks(message));
