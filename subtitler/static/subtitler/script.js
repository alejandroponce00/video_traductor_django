document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.querySelector('form');
    const progressDiv = document.getElementById('progress');
    const progressBar = document.querySelector('.progress-bar');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        
        progressDiv.style.display  = 'block';
        progressBar.style.width = '0%';

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => {
            if (response.ok) {
                return response.blob();
            }
            throw new Error('Network response was not ok.');
        })
        .then(blob => {
            progressBar.style.width = '100%';
            
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'video_subtitulado.mp4';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Hubo un error al procesar el video. Por favor, inténtalo de nuevo.');
        })
        .finally(() => {
            setTimeout(() => {
                progressDiv.style.display = 'none';
                progressBar.style.width = '0%';
            }, 1000);
        });
    });
});