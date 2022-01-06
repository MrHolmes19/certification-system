
const picker = document.getElementById('day');
picker.addEventListener('input', function(e){
    var day = new Date(this.value).getUTCDay();
    if([6,0].includes(day)){
        e.preventDefault();
        this.value = '';
    }
});

day_input = document.getElementById('day')

day_input.addEventListener('change', (event) => {
    block_radios(day_input.value)
    picker.classList.add("active")
});

function block_radios(day_value){
    all_radios = document.getElementsByName("schedule");

    all_radios.forEach(element => {
        element.removeAttribute("disabled");
    });

    if(day_value == ""){
        all_radios.forEach(element => {
        element.setAttribute("disabled", "true");
        });
    }


    for(i = 0; i < mylist.length; i++){
        try{
            element_day = mylist[i].split("T")[0];
            element_time = mylist[i].split("T")[1];

            if(element_day == day_input.value){
                time = element_time.substr(0, 5);
                if(time.charAt(0) == "0"){
                    time = time.substr(1, time.length)
                }
                let radio_id = "radio_" + time;
                document.getElementById(radio_id).setAttribute("disabled", "true");  
            }
        }
        catch{
            a = 0;
        }
    };
}

// set min date = today
var today = new Date();
var dd = today.getDate();
var maxday = dd+30;
var mm = today.getMonth()+1; //January is 0 so need to add 1 to make it 1!
var yyyy = today.getFullYear();

if(dd<10){
    dd='0'+dd
} 
if(mm<10){
    mm='0'+mm
} 

today = yyyy+'-'+mm+'-'+dd;
day_input.setAttribute("min", today);

// set max date

var not_today = new Date();
not_today.setDate(maxday);

var m_dd = not_today.getDate();
var m_mm = not_today.getMonth()+1;
var m_yyyy = not_today.getFullYear();

if(m_dd<10){
    m_dd='0'+dd
} 
if(m_mm<10){
    m_mm='0'+m_mm
} 

max_date = m_yyyy+'-'+m_mm+'-'+m_dd;
day_input.setAttribute("max", max_date);