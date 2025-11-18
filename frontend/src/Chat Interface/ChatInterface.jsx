import React, { useState, useEffect, useRef } from "react";
import { v4 as uuidv4 } from "uuid"; 
import ChatBotIcon from "./components/ChatBotIcon";
import ChatForm from "./components/ChatForm";
import ChatBotImage from "./components/ChatBotImage";

export default function ChatInterface() {
  const [chatHistory, setChatHistory] = useState([
    {
      sender: "bot",
      text: "Hello, Welcome to Lifecare Medical Center! How can I help you today?"
    }
  ]);

  const [isBotTyping, setIsBotTyping] = useState(false);
  const [typingText, setTypingText] = useState("Bot is typing");
  const lastMessageRef = useRef();

  // Generate a unique session ID per user session
  const [sessionId] = useState(uuidv4());

  // Scroll to latest message
  useEffect(() => {
    lastMessageRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatHistory, isBotTyping]);

  // Animate the typing dots
  useEffect(() => {
    let interval;
    if (isBotTyping) {
      let dotCount = 0;
      interval = setInterval(() => {
        dotCount = (dotCount + 1) % 4; 
        setTypingText("Bot is typing" + ".".repeat(dotCount));
      }, 500);
    } else {
      setTypingText("Bot is typing");
    }
    return () => clearInterval(interval);
  }, [isBotTyping]);

  // Function to add bot response
  const addBotResponse = async (userMessage) => {
    setIsBotTyping(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          message: userMessage,
          session_id: sessionId 
        })
      });

      const data = await response.json();

      setTimeout(() => {
        setChatHistory((prev) => [
          ...prev,
          { sender: "bot", text: data.response }
        ]);
        setIsBotTyping(false);
      }, 1000); 
    } catch (err) {
      console.error("Error sending message:", err);
      setIsBotTyping(false);
    }
  };

  return (
    <div className="container">
      <ChatBotImage />

      <div className="chatbot-popup">
        
        <div className="chat-header">
          <div className="header-info">
            <ChatBotIcon />
            <h2 className="logo-text">ChatBot</h2>
          </div>
        </div>

        <div className="chat-body">
          {chatHistory.map((msg, index) => {
            const isLastMessage = index === chatHistory.length - 1;
            return (
              <div
                key={index}
                ref={isLastMessage ? lastMessageRef : null}
                className={`message ${
                  msg.sender === "bot" ? "bot-message" : "user-message"
                }`}
              >
                {msg.sender === "bot" && <ChatBotIcon />}
                <p className="message-text" style={{ whiteSpace: "pre-wrap" }}>
                  {msg.text}
                </p>
              </div>
            );
          })}

          
          {isBotTyping && (
            <div className="message bot-message" ref={lastMessageRef}>
              <ChatBotIcon />
              <p className="message-text" style={{ whiteSpace: "pre-wrap" }}>
                {typingText}
              </p>
            </div>
          )}
        </div>

      
        <div className="chat-footer">
          <ChatForm setChatHistory={setChatHistory} addBotResponse={addBotResponse} sessionId={sessionId} />
        </div>
      </div>
    </div>
  );
}
