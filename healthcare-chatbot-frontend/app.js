const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chatContainer = document.getElementById('chat-container');
const loadingIndicator = document.getElementById('loading-indicator');
const resetBtn = document.getElementById('reset-btn');

// Include the Marked library (if not already in your HTML)
const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/marked/marked.min.js';
document.head.appendChild(script);

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const userText = input.value.trim();
  if (!userText) return;

  appendMessage(userText, 'user');
  input.value = '';
  loadingIndicator.classList.remove('hidden');

  try {
    const res = await fetch('https://ai-health-assistant-nkek.onrender.com', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: userText }),
    });

    const data = await res.json();
    appendMessage(data.response || "Sorry, I couldn't find any relevant information.", 'bot');
  } catch (err) {
    console.error(err);
    appendMessage("An error occurred while contacting the server.", 'bot');
  } finally {
    loadingIndicator.classList.add('hidden');
  }
});

resetBtn.addEventListener('click', () => {
  chatContainer.innerHTML = '';
});

function appendMessage(text, sender) {
  const msg = document.createElement('div');
  msg.className = `message ${sender}`;
  msg.innerHTML = marked.parse(text); // Use marked.parse to render Markdown
  chatContainer.appendChild(msg);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}