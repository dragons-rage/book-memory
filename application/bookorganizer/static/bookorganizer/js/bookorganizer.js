// JavaScript for bookorganizer app

/**
 * Refresh the authors dropdown field with fresh data from the server
 */
function refreshAuthors() {
    const refreshButton = document.getElementById('refresh-authors');
    const authorsField = document.getElementById('id_authors'); // Django typically uses 'id_' prefix for form fields
    
    if (!refreshButton || !authorsField) {
        console.error('Refresh authors button or authors field not found');
        return;
    }

    // Show loading state
    const originalText = refreshButton.innerHTML;
    refreshButton.innerHTML = '❌';
    refreshButton.disabled = true;

    // Make AJAX request to get fresh author data
    fetch('/authors/json', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Clear existing options
        authorsField.innerHTML = '';
        
        // Add new options from the server response
        data.authors.forEach(author => {
            const option = document.createElement('option');
            option.value = author.id;
            option.textContent = author.full_name;
            authorsField.appendChild(option);
        });
        
        console.log(`Refreshed ${data.authors.length} authors`);
        
        // Show success feedback briefly
        refreshButton.innerHTML = '✅';
        setTimeout(() => {
            refreshButton.innerHTML = originalText;
        }, 2000);
    })
    .catch(error => {
        console.error('Error refreshing authors:', error);
        
        // Show error feedback
        refreshButton.innerHTML = '❌ Error';
        setTimeout(() => {
            refreshButton.innerHTML = originalText;
        }, 3000);
    })
    .finally(() => {
        // Re-enable the button
        refreshButton.disabled = false;
    });
}

/**
 * Initialize the book organizer functionality when DOM is loaded
 */
function initializeBookOrganizer() {
    console.log('Book Organizer app initialized');
    
    // Attach refresh functionality to the refresh authors button
    const refreshAuthorsButton = document.getElementById('refresh-authors');
    if (refreshAuthorsButton) {
        refreshAuthorsButton.addEventListener('click', refreshAuthors);
        console.log('Refresh authors button initialized');
    }
}

// Initialize when the DOM is loaded
document.addEventListener('DOMContentLoaded', initializeBookOrganizer);
