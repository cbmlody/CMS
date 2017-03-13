function play_sound() {
    var audio = document.createElement('audio');
    audio.src = 'js/oja.mp3';
    audio.volume = '0.4';
    audio.play();
}

function roll() {
    var roll = Math.floor((Math.random() * 10) + 1);
    return roll
}

function game(guess) {
    var rolled = roll()
    if (guess == rolled) {
        document.getElementById("roll").innerHTML ="<h2 style='text-align:center'>Zgadłeś!</h2>"
        
    } else {
        document.getElementById("roll").innerHTML = "<h2 style='text-align:center'>Nie zgadłeś!!</h2><h6><h4 style='text-align:center'>Wylosowano " + rolled + "</h4>";

    }
}
