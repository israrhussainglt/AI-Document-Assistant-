import { useState, useEffect, useRef } from 'react';
import { sendChat } from '../services/api';

function ChatBox({ selectedDocument, summaryMessage }) {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  // Add summary to messages when it changes
  useEffect(() => {
    if (summaryMessage) {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: summaryMessage,
          isSummary: true,
        },
      ]);
    }
  }, [summaryMessage]);

  const handleSend = async () => {
    if (!inputValue.trim()) return;

    if (!selectedDocument) {
      alert('Please select a document first');
      return;
    }

    const userMessage = inputValue;
    setInputValue('');
    setMessages((prev) => [
      ...prev,
      { role: 'user', content: userMessage },
    ]);

    setIsLoading(true);
    try {
      const response = await sendChat(userMessage, selectedDocument);
      setMessages((prev) => [
        ...prev,
        { role: 'assistant', content: response.answer || response.message },
      ]);
    } catch (error) {
      console.error('Chat error:', error);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: `⚠️ Error: ${error.message}`,
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-box">
      <div className="chat-header">
        <h2>💬 Document Chat</h2>
        <p>
          {selectedDocument
            ? `📄 Chatting about: ${selectedDocument}`
            : 'Select a document to start chatting'}
        </p>
      </div>

      <div className="chat-messages">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <h3>Welcome 👋</h3>
            <p>Upload a PDF and start asking questions about your document.</p>
            <p style={{ marginTop: '16px', fontSize: '12px', color: '#9ca3af' }}>
              💡 Tip: Use the "Summarize" button to get a professional overview of the document.
            </p>
          </div>
        ) : (
          <>
            <div className="messages-list">
              {messages.map((msg, index) => (
                <div key={index} className={`message ${msg.role} ${msg.isSummary ? 'summary' : ''}`}>
                  <div className="message-content">{msg.content}</div>
                </div>
              ))}
            </div>
            {isLoading && (
              <div className="message assistant">
                <div className="message-content typing">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </>
        )}
      </div>

      <div className="chat-input">
        <input
          type="text"
          placeholder="Ask something about your document..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          disabled={!selectedDocument || isLoading}
        />
        <button onClick={handleSend} disabled={!selectedDocument || isLoading}>
          {isLoading ? '⏳' : '➤'}
        </button>
      </div>
    </div>
  );
}

export default ChatBox;