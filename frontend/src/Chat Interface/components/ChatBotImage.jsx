import React from 'react'
import chatbot from "../../assets/chatbot.png"
import "./ChatBotImage.css";

export default function ChatBotImage() {
  return (
    <div>
      <div className="chatbot-image-container">
        <img src={chatbot} alt="App Logo" />
      </div>
    </div>
  )
}
