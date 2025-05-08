document.addEventListener('DOMContentLoaded', function() {
    // Handle image deletion
    document.querySelectorAll('.delete-image').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const imageId = this.dataset.imageId;
            
            if (confirm('Are you sure you want to delete this image?')) {
                fetch(`/destinations/api/images/${imageId}/`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => {
                    if (response.ok) {
                        this.parentElement.remove();
                    } else {
                        alert('Failed to delete image');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Failed to delete image');
                });
            }
        });
    });
});

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}