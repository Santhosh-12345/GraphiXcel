const fileInput = document.getElementById('file-upload');
const browseFileButton = document.getElementById('browse-file');
const dropArea = document.getElementById('drop-area');

// Open file browser when clicking "Browse File"
browseFileButton.addEventListener('click', function() {
    fileInput.click();
});

// Add change event listener to handle file selection
fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        console.log('File selected:', file.name);
        // Add any additional logic to handle the selected file here
        uploadFile(file);
    }
});

// Prevent default behavior for drag events
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

// Highlight drop area when dragging files over it
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => dropArea.classList.add('highlight'), false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => dropArea.classList.remove('highlight'), false);
});

// Handle file drop
dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;

    handleFiles(files);
}

function handleFiles(files) {
    [...files].forEach(uploadFile);
}

function uploadFile(file) {
    console.log('Dropped file:', file.name);
    // Logic for uploading the file to a server or handling it locally
    // For example, you can read the file or send it to a server
    const reader = new FileReader();
    reader.onload = function(e) {
        const fileContent = e.target.result;
        // Process the file content here
        console.log('File content:', fileContent);
    };
    reader.readAsText(file);
// Read as binary string (or use readAsArrayBuffer, readAsText as needed)
}
