// Get the input field
var input = document.getElementById("message");

// Execute a function when the user presses a key on the keyboard
input.addEventListener("keypress", function(event) {
// If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        document.getElementById("sendBtn").click();
    }
});

$(document).ready(function() {
    var socket = io.connect("http://localhost:5000")
    socket.on('connect', function() {
        socket.send("User connected!");
    });

    socket.on('message', function(data) {
        $('#messages').append($('<p>').text(data));
    });

    $('#sendBtn').on('click', function() {
        socket.send($('#username').val() + ': ' + $('#message').val());
        $('#message').val('');
    })

});