

// let uploadedFileName = '';

// // Handle file upload
// document.getElementById('uploadForm').addEventListener('submit', async (e) => {
//     e.preventDefault();

//     const fileInput = document.getElementById('fileInput');
//     const formData = new FormData();
//     formData.append('file', fileInput.files[0]);

//     try {
//         const response = await fetch('/upload', {
//             method: 'POST',
//             body: formData,
//         });

//         const data = await response.json();

//         if (response.ok) {
//             uploadedFileName = data.filename;
//             document.getElementById('uploadMessage').textContent = data.message;
//             document.getElementById('fileName').textContent = `Uploaded File: ${data.filename}`;
//             document.getElementById('extractTextButton').style.display = 'block';
//         } else {
//             document.getElementById('uploadMessage').textContent = `Error: ${data.error}`;
//         }
//     } catch (error) {
//         document.getElementById('uploadMessage').textContent = `Error: ${error.message}`;
//     }
// });

// // Handle entity extraction
// document.getElementById('extractTextButton').addEventListener('click', async () => {
//     try {
//         const response = await fetch('/extract_text', {
//             method: 'POST',
//         });

//         const data = await response.json();

//         if (response.ok) {
//             let tableHTML = `
//                 <h2>Extracted Entities:</h2>
//                 <table class="entities-table">
//                     <thead>
//                         <tr>
//                             <th>Label</th>
//                             <th>Entity</th>
//                         </tr>
//                     </thead>
//                     <tbody>
//             `;

//             data.entities.forEach(ent => {
//                 tableHTML += `
//                     <tr>
//                         <td>${ent.label}</td>
//                         <td>${ent.entity}</td>
//                     </tr>
//                 `;
//             });

//             tableHTML += `</tbody></table>`;
//             document.getElementById('extractedContent').innerHTML = tableHTML;
//             document.getElementById('saveEntitiesButton').style.display = 'block';
//         } else {
//             document.getElementById('extractedContent').innerHTML = `<p>Error: ${data.error}</p>`;
//         }
//     } catch (error) {
//         document.getElementById('extractedContent').innerHTML = `<p>Error: ${error.message}</p>`;
//     }
// });

// // Handle saving entities
// document.getElementById('saveEntitiesButton').addEventListener('click', async () => {
//     try {
//         const response = await fetch('/save', {
//             method: 'POST',
//         });

//         const data = await response.json();

//         if (response.ok) {
//             document.getElementById('extractedContent').innerHTML += `
//                 <p style="color: green;">${data.message}</p>
//             `;
//         } else {
//             document.getElementById('extractedContent').innerHTML += `
//                 <p style="color: red;">Error: ${data.error}</p>
//             `;
//         }
//     } catch (error) {
//         document.getElementById('extractedContent').innerHTML += `
//             <p style="color: red;">Error: ${error.message}</p>
//         `;
//     }
// });

let uploadedFileName = [];

// Function to show the waiting screen
function showExtractingScreen() {
    document.getElementById('extracting-screen').style.display = 'flex';
}

// Function to hide the waiting screen
function hideExtractingScreen() {
    document.getElementById('extracting-screen').style.display = 'none';
}

function showUploadingScreen() {
    document.getElementById('uploading-screen').style.display = 'flex';
}

// Function to hide the waiting screen
function hideUploadingScreen() {
    document.getElementById('uploading-screen').style.display = 'none';
}


hideExtractingScreen();
hideUploadingScreen();
// Handle file upload

document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        document.getElementById('uploadMessage').textContent = 'Please select a file to upload.';
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        // Optionally, show waiting screen during upload if desired
        // Uncomment the next two lines if you want to show the splash screen during upload
        showUploadingScreen();

        const response = await fetch('/upload', {
            method: 'POST',
            body: formData,
        });
        hideUploadingScreen();

        const data = await response.json();

        // Optionally, hide waiting screen after upload
        // Uncomment the next line if you showed the waiting screen during upload
        // hideWaitingScreen();

        if (response.ok) {
            uploadedFileName = data.filename;
            document.getElementById('uploadMessage').textContent = data.message;
            document.getElementById('fileName').textContent = `Uploaded File: ${data.filename}`;
            document.getElementById('extractTextButton').style.display = 'block';
        } else {
            document.getElementById('uploadMessage').textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        // Ensure waiting screen is hidden in case of error if you showed it
        // hideWaitingScreen();

        document.getElementById('uploadMessage').textContent = `Error: ${error.message}`;
    }
});

// Handle entity extraction
document.getElementById('extractTextButton').addEventListener('click', async () => {
    try {
        showExtractingScreen(); // Show waiting screen during extraction

        const response = await fetch('/extract_text', {
            method: 'POST',
        });

        const data = await response.json();

        hideExtractingScreen(); // Hide waiting screen after extraction

        if (response.ok) {
            if (!data.entities || data.entities.length === 0) {
                document.getElementById('extractedContent').innerHTML = `<p>No entities found.</p>`;
                document.getElementById('saveEntitiesButton').style.display = 'none';
                return;
            }

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

            tableHTML += `</tbody></table>`;
            document.getElementById('extractedContent').innerHTML = tableHTML;
            document.getElementById('saveEntitiesButton').style.display = 'block';
        } else {
            document.getElementById('extractedContent').innerHTML = `<p>Error: ${data.error}</p>`;
        }
    } catch (error) {
        hideWaitingScreen(); // Ensure waiting screen is hidden in case of error
        document.getElementById('extractedContent').innerHTML = `<p>Error: ${error.message}</p>`;
    }
});

// Handle saving entities
document.getElementById('saveEntitiesButton').addEventListener('click', async () => {
    try {
        showWaitingScreen(); // Show waiting screen during saving

        const response = await fetch('/save', {
            method: 'POST',
        });

        const data = await response.json();

        hideWaitingScreen(); // Hide waiting screen after saving

        if (response.ok) {
            document.getElementById('extractedContent').innerHTML += `
                <p style="color: green;">${data.message}</p>
            `;
        } else {
            document.getElementById('extractedContent').innerHTML += `
                <p style="color: red;">Error: ${data.error}</p>
            `;
        }
    } catch (error) {
        hideWaitingScreen(); // Ensure waiting screen is hidden in case of error
        document.getElementById('extractedContent').innerHTML += `
            <p style="color: red;">Error: ${error.message}</p>
        `;
    }
});

