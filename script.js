const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

function addMessage(sender, text) {
  const msg = document.createElement("div");
  msg.classList.add("message", sender);
  msg.textContent = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

sendBtn.addEventListener("click", async () => {
  const text = userInput.value.trim();
  if (!text) return;
  
  addMessage("user", text);
  userInput.value = "";

  addMessage("bot", "Thinking...");

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    chatBox.lastChild.textContent = data.reply;
  } catch (error) {
    chatBox.lastChild.textContent = "⚠️ Error: Could not connect to server.";
  }
});

userInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") sendBtn.click();
});
