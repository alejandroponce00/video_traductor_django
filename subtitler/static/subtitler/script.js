document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.getElementById('videoForm');
    const progressDiv = document.getElementById('progress');
    const progressBar = document.querySelector('.progress-bar');
    const videoContainer = document.getElementById('videoContainer');
    const videoPlayer = document.getElementById('videoPlayer');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        
        progressDiv.style.display = 'block';
        progressBar.style.width = '0%';

        fetch('/process/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            progressBar.style.width = '100%';
            
            // Mostrar el video
            videoContainer.style.display = 'block';
            videoPlayer.src = URL.createObjectURL(formData.get('file'));

            // Añadir pistas de texto al video
            const track = videoPlayer.addTextTrack("captions", "Español", "es");
            track.mode = "showing";
            data.subtitles.forEach(subtitle => {
                const cue = new VTTCue(subtitle.start, subtitle.end, subtitle.text);
                track.addCue(cue);
            });
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
