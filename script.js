function queryNumber() {
    var number = document.getElementById("numberInput").value;
    // Send the number to the backend server for querying
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/query", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var result = xhr.responseText;
                document.getElementById("result").innerText = result;
            } else {
                console.error('Error:', xhr.status);
            }
        }
    };
    xhr.send("number=" + encodeURIComponent(number));
}
