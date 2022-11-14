function updateCaffeineIntake() {
    // TODO Add ability to modify the time stamp
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

        document.getElementById("historyList").innerHTML = currentList + "<li class=\"enteredItem\">[" + 
                currentDate + "] <b>" + inputtedCaffeine + "mg</b></li>";
    }    
}

function updateEstimatedCaffeineLeft() {
    // Half Life Formula: T(1/2) = [R]0/2k
    let caffeineHistory = document.getElementsByClassName("enteredItem");

    let currentDate = new Date();
    let currentMinute = parseInt(currentDate.getMinutes()) / 60;
    let currentTime = parseInt(currentDate.getHours()) + currentMinute;
    
    let caffeineMinute;
    let caffeineTime;
    let timeSinceIngestion;
   
    let time;
    let totalCaffeine;

    let caffeineLeft = 0;

    for (let i = 0; i < caffeineHistory.length; i++) {
        let caffeineHistorySplit = caffeineHistory[i].innerHTML.split(" ");
        time = caffeineHistorySplit[1]
        time = time.substring(0, time.length - 1).split(":");

        caffeineMinute = parseInt(time[1]) / 60;
        caffeineTime = parseInt(time[0]) + caffeineMinute;

        timeSinceIngestion = currentTime - caffeineTime;

        totalCaffeine = caffeineHistorySplit[2];
        totalCaffeine = totalCaffeine.substring(3, totalCaffeine.length - 6);

        caffeineLeft += parseInt(totalCaffeine) * Math.pow(0.5, timeSinceIngestion/6);
        
    }
    document.getElementById("estimatedCaffeine").innerHTML = Math.round(caffeineLeft);
}
