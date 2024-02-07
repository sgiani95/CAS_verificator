function queryNumber() {
    var number = document.getElementById("numberInput").value;
    // Send the number to the backend API for querying (we'll implement this later)
    // For now, let's just display a placeholder result
    var resultDiv = document.getElementById("result");
    resultDiv.innerText = "Querying number: " + number;
    resultDiv.style.display = "block";
}
