
var successful = true;
let form = document.querySelector('form');
let main = document.querySelector('.container')
let btn = document.querySelector('.submit')

function formSubmit(){
    if (successful) {
         console.log(form)
         form.style.visibility = 'hidden'
         main.innerHTML = '<div class="container-2"><p class="success">Form Submited</p></div>'
        
    }
};


btn.addEventListener('click', formSubmit);
