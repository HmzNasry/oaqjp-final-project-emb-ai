let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value.trim(); 

    if (!textToAnalyze) { 
        document.getElementById("system_response").innerHTML = "Invalid text! Please try again!";
        return;
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else if (this.status == 400) {
                document.getElementById("system_response").innerHTML = "Invalid text! Please try again!";
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
