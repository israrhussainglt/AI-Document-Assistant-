import { useState } from 'react';
import { summarizeDocument } from '../services/api';

function SummarizeButton({ selectedDocument, onSummarize }) {
  const [isLoading, setIsLoading] = useState(false);

  const handleSummarize = async () => {
    if (!selectedDocument) {
      alert('Please select a document first');
      return;
    }

    setIsLoading(true);
    try {
      const response = await summarizeDocument(selectedDocument);
      onSummarize?.(response.summary);
    } catch (error) {
      console.error('Summarize failed:', error);
      alert(`Failed to summarize: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <button
      className="summarize-button"
      onClick={handleSummarize}
      disabled={!selectedDocument || isLoading}
      title="Generate a professional summary of the selected document"
    >
      {isLoading ? '⏳ Summarizing...' : '📋 Summarize'}
    </button>
  );
}

export default SummarizeButton;
