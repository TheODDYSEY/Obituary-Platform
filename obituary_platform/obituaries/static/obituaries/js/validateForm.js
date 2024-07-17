// obituaries/static/obituaries/js/validateForm.js
document.getElementById('obituaryForm').addEventListener('submit', function(event) {
    let formIsValid = true;

    // Custom validation logic here
    // Check if the content is at least 20 characters
    const content = document.getElementById('content').value;
    if (content.length < 20) {
        formIsValid = false;
        alert('Content must be at least 20 characters long.');
    }

    if (!formIsValid) {
        event.preventDefault();
    }
});
