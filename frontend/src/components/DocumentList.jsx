function DocumentList({ documents = [], selectedDocument, onSelectDocument }) {
  if (!documents || documents.length === 0) {
    return (
      <div className="document-list">
        <p>No documents uploaded yet.</p>
      </div>
    );
  }

  return (
    <div className="document-list">
      <ul>
        {documents.map((doc) => (
          <li 
            key={doc.filename}
            className={selectedDocument === doc.filename ? 'selected' : ''}
            onClick={() => onSelectDocument?.(doc.filename)}
          >
            <div className="doc-name">{doc.filename}</div>
            <div className="doc-pages">{doc.pages} page(s)</div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DocumentList;