async function sendMessage() {
    const input = document.getElementById("userInput").value;
    const responseDiv = document.getElementById("response");

    responseDiv.innerHTML = "⏳ Thinking...";
    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: input }),
        });

        const data = await res.json();
        if (data.response) {
            responseDiv.innerHTML = `<b>AI:</b> ${data.response}`;
        } else {
            responseDiv.innerHTML = `<b>Error:</b> ${data.error}`;
        }
    } catch (err) {
        responseDiv.innerHTML = "⚠️ Connection error!";
    }
}
