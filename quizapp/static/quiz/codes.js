const scores = []
sum=0

const dscore = []

function myf(value,right, id){
    nid = parseInt(id)
    if(value===right){
        scores[nid]=1
    }
    else{
        scores[nid]=0
    }
}
  
function finale1(total){
    for(x of scores){
        
        if(x!=null){
            sum+=x
        }
    }
    console.log("You scored "+sum);
    //document.getElementById('score').innerHTML= "Your score is " + sum +" out of "+ total
    DisplaywrongAnswers(sum,total)
    return sum
}



function DisplaywrongAnswers(s,t){
    let divforanswers = document.createElement('label');
    document.getElementById('myscore').appendChild(divforanswers)
    divforanswers.appendChild(document.createTextNode( s + " out of "+t))
    
  
}


