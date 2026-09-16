import { useRef, useState } from 'react';
import { uploadPDF } from '../services/api';

function FileUpload({ onUploadSuccess }) {
  const fileInputRef = useRef(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleButtonClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = async (event) => {
    const file = event.target.files?.[0];
    if (!file) return;

    if (!file.name.toLowerCase().endsWith('.pdf')) {
      alert('Please select a PDF file');
      return;
    }

    setIsLoading(true);
    try {
      const response = await uploadPDF(file);
      onUploadSuccess?.(response);
      // Reset input
      event.target.value = '';
    } catch (error) {
      console.error('Upload failed:', error);
      alert(`Failed to upload PDF: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="file-upload">
      <button 
        onClick={handleButtonClick}
        disabled={isLoading}
      >
        {isLoading ? '⏳ Uploading...' : '📤 Upload PDF'}
      </button>
      <input
        ref={fileInputRef}
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
        style={{ display: 'none' }}
      />
    </div>
  );
}

export default FileUpload;