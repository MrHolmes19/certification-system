// Getting the URL's paramethers from Calendar and extract date and email

var current_url = window.location.href;

var fullname = document.getElementById('name')
var date = document.getElementById('date')
var time = document.getElementById('time')
var email = document.getElementById('email')

function CatchParams(url) {
    if (typeof url != 'string') {
        throw TypeError('El argumento debe ser una cadena de caracteres.');
    }

    // Pendiente: validar si una cadena de caracteres corresponde con una URL.
    shift_info = (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce((a, p) => ((a[p.slice(0, p.indexOf('='))] = p.slice(p.indexOf('=') + 1)), a), {});
    return shift_info;
}

try {
    console.log(CatchParams(current_url));
    // {prop1: v1, prop2: v2, prop3: v3}
} catch (e) {
    console.log(`Error: ${e.message}`);
}

fullname.innerHTML = CatchParams(current_url).invitee_full_name;
date.innerHTML = CatchParams(current_url).event_start_time;
time.innerHTML = CatchParams(current_url).event_start_time;
email.innerHTML = CatchParams(current_url).invitee_email;
