function boton(){
    for(var i = 0; i < 20; i++){
        if(cat_fact()==true){
            break;
        }
    }
}

function cat_fact(){
    $.get("https://cat-fact.herokuapp.com/facts/random", function(data, status){
        console.log(data.status.verified);
        if(data.status.verified){
            document.getElementById("cat_fact").innerHTML=data.text;
            return true;
        }
        else{
            return false;
        }
    })
}