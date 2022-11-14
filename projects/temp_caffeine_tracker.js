function updateCaffeineIntake() {
    let currentCaffieneIntake = parseInt(document.getElementById("intake").innerText);
    let inputtedCaffeine = parseInt(document.getElementsByClassName("intakeClass")[0].value);
    let currentList = document.getElementById("historyList").innerHTML;
    let date = new Date();
    let currentDate = date.getMonth() + "/" + date.getDate() + "/" + date.getFullYear()
            + " " + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
    let updatedCaffeineIntake = 0;

    if (!isNaN(currentCaffieneIntake) && !isNaN(inputtedCaffeine)) {
        updatedCaffeineIntake = currentCaffieneIntake + inputtedCaffeine;
        document.getElementById("intake").innerHTML = updatedCaffeineIntake;

        document.getElementById("historyList").innerHTML = currentList + "<li>[" + 
                currentDate + "] <b>" + inputtedCaffeine + "mg</b></li>";
    }

    
}
