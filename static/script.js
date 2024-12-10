        async function sendMessage() {
            const userInput = document.getElementById('user-input').value;

            // Append user message to the chat box
            const chatBox = document.getElementById('messages');
            chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

            // Send user input to the server
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `message=${encodeURIComponent(userInput)}`,
            });

            const data = await response.json();

            // Append AI response to the chat box
            chatBox.innerHTML += `<p><strong>AI:</strong> ${data.response}</p>`;

            // Clear the input field
            document.getElementById('user-input').value = '';
        }

        