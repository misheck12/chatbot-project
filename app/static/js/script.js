function sendMessage() {
    var userInput = document.getElementById("userInput").value;
    var chatLog = document.getElementById("chat-log");

    // Add user message to chat log
    chatLog.innerHTML += "<p><strong>You:</strong> " + userInput + "</p>";

    // Send user message to the server and get bot response
    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: "msg=" + userInput
    })
    .then(response => response.text())
    .then(data => {
        // Add bot response to chat log
        chatLog.innerHTML += "<p><strong>Bot:</strong> " + data + "</p>";
    });

    // Clear the input field
    document.getElementById("userInput").value = "";
}
