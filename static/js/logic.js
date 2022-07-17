console.log("Ecommerce site Project");

// logic for counter section

document.addEventListener('DOMContentLoaded', ()=>{
    function counter(id, start, end, duration){
        let obj = document.getElementById(id), current = start, range= end - start, increment = end > start ? 1: -1,
        step = Math.abs(Math.floor(duration/range)),
        timer = setInterval(()=>{
            current += increment;
            obj.textContent = current;
            if(current == end){
                clearInterval(timer)
            }
        }, step);
    }

    counter("count1", 0 , 604, 3500);
    counter("count2", 100 , 1124, 3500);
    counter("count3", 0 , 41, 3500);

});

// function closeNav(){
//     document.getElementById('hideNav').style.width = "0px"

//     document.getElementById("hero-container").style.backgroundColor= "#ffffff";

// }

function openNav(){
   const explore =  document.getElementById('socialMedia');
    // document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
    // document.getElementById("hero-container").style.backgroundColor= "#f6f7fb";



}