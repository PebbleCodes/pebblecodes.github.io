const ACTIVE = "&starf;";
const INACTIVE = "&star;";
const ratingStars = [...document.getElementsByClassName("star")];

function executeRating(stars) {
    const starClassActive = "star active";
    const starClassInactive = "star inactive";
    const starsLength = stars.legnth;
    let previousRating;
    let rating;

    stars.map((star) => {
        star.onclick = () =>{
            selected = stars.indexOf(star);
            previousRating = document.getElementById("rating").innerText;
            if (previousRating <= 0) {
                previousRating = 0;
            }
            rating = selected + 1;

            for (let i = 0; i < 5; ++i) {
                if (i < rating) {
                    stars[i].className = starClassActive;
                    document.getElementsByClassName("star")[i].innerHTML = ACTIVE;
                } else {
                    stars[i].className = starClassInactive;
                    document.getElementsByClassName("star")[i].innerHTML = INACTIVE;
                }
            }
            document.getElementById("rating").innerHTML = rating;
            document.getElementById("previousRating").innerHTML = previousRating;
        };
    });
}

executeRating(ratingStars);

function fillStar(star) {
    let currentRating = parseInt(document.getElementById("rating").innerHTML);
    if (isNaN(currentRating)) {
        currentRating = 0;
    }
    let currentIndex = ratingStars.indexOf(star);
    for (let i = currentRating; i <= currentIndex; ++i) {
        document.getElementsByClassName("star")[i].innerHTML = ACTIVE;
    }
}

function emptyStar(star) {
    let currentRating = parseInt(document.getElementById("rating").innerHTML);
    if (isNaN(currentRating)) {
        currentRating = 0;
    }
    for (currentRating; currentRating < 5; ++currentRating) {
        document.getElementsByClassName("star")[currentRating].innerHTML = INACTIVE;
    }
}

function submitForm() {
    let currentRating = parseInt(document.getElementById("rating").innerText);
    if (isNaN(currentRating)) {
        currentRating = 0;
    }
    document.getElementById("status").innerText = "Submitted!";
}