import { useState } from 'react';
import FileUpload from "../components/FileUpload";
import DocumentList from "../components/DocumentList";
import ChatBox from "../components/ChatBox";
import SummarizeButton from "../components/SummarizeButton";

function Dashboard() {
  const [documents, setDocuments] = useState([]);
  const [selectedDocument, setSelectedDocument] = useState(null);
  const [summaryMessage, setSummaryMessage] = useState(null);

  const handleUploadSuccess = (response) => {
    // Add the uploaded document to the list
    const newDoc = {
      filename: response.filename,
      pages: response.pages,
      chunks: response.chunks,
    };
    setDocuments([...documents, newDoc]);
    setSelectedDocument(newDoc.filename);
  };

  const handleSummarize = (summary) => {
    setSummaryMessage(summary);
  };

  return (
    <div className="dashboard">

      <header className="dashboard-header">
        <div>
          <h1>AI Document Intelligence</h1>
          <p>Upload documents and ask questions using AI.</p>
        </div>
      </header>

      <div className="dashboard-content">

        <aside className="sidebar">

          <div className="sidebar-section">
            <h2>Documents</h2>

            <FileUpload onUploadSuccess={handleUploadSuccess} />

            <SummarizeButton 
              selectedDocument={selectedDocument}
              onSummarize={handleSummarize}
            />

            <DocumentList 
              documents={documents} 
              selectedDocument={selectedDocument} 
              onSelectDocument={setSelectedDocument} 
            />
          </div>

        </aside>

        <main className="chat-section">
          <ChatBox 
            selectedDocument={selectedDocument}
            summaryMessage={summaryMessage}
          />
        </main>

      </div>

    </div>
  );
}

export default Dashboard;