import React, { useRef } from "react";

export default function ChatForm({ setChatHistory, addBotResponse }) {
  const inputRef = useRef();

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    const userMessage = inputRef.current.value.trim();
    if (!userMessage) return;

    // Add user message to chat
    setChatHistory((prev) => [...prev, { sender: "user", text: userMessage }]);

    // Clear input
    inputRef.current.value = "";
    inputRef.current.focus();

    // Call bot response
    addBotResponse(userMessage);
  };

  return (
    <form className="chat-form" onSubmit={handleFormSubmit}>
      <input
        ref={inputRef}
        type="text"
        placeholder="Ask anything..."
        className="message-input"
        required
      />
      <button type="submit" className="material-symbols-outlined">
        arrow_upward
      </button>
    </form>
  );
}
