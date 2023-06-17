function boton(){
    for(var i = 0; i < 9; i++){
        cat_fact();
    }
}

function cat_fact(){
    $.get("https://cat-fact.herokuapp.com/facts/random", function(data, status){
        if(data.status.verified){
            document.getElementById("cat_fact").innerHTML=data.text;
        }
        console.log(data.status.verified);
    });
}