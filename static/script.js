

let uploadedFileName = '';

// Handle file upload
document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();

        if (response.ok) {
            uploadedFileName = data.filename;
            document.getElementById('uploadMessage').textContent = data.message;
            document.getElementById('fileName').textContent = `Uploaded File: ${data.filename}`;
            document.getElementById('extractTextButton').style.display = 'block';
        } else {
            document.getElementById('uploadMessage').textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        document.getElementById('uploadMessage').textContent = `Error: ${error.message}`;
    }
});

// Handle entity extraction
document.getElementById('extractTextButton').addEventListener('click', async () => {
    try {
        const response = await fetch('/extract_text', {
            method: 'POST',
        });

        const data = await response.json();

        if (response.ok) {
            // Create dynamic table
            let tableHTML = `
                <h2>Extracted Entities:</h2>
                <table class="entities-table">
                    <thead>
                        <tr>
                            <th>Label</th>
                            <th>Entity</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            data.entities.forEach(ent => {
                tableHTML += `
                    <tr>
                        <td>${ent.label}</td>
                        <td>${ent.entity}</td>
                    </tr>
                `;
            });

            tableHTML += `
                    </tbody>
                </table>
            `;

            document.getElementById('extractedContent').innerHTML = tableHTML;
        } else {
            document.getElementById('extractedContent').innerHTML = `<p>Error: ${data.error}</p>`;
        }
    } catch (error) {
        document.getElementById('extractedContent').innerHTML = `<p>Error: ${error.message}</p>`;
    }
});
