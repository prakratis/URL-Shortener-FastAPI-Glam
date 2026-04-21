async function shortenUrl() {
    const urlInput = document.getElementById('longUrl');
    const resultDiv = document.getElementById('result');
    const url = urlInput.value;

    if (!url) {
        resultDiv.innerHTML = "✨ Please enter a link first ✨";
        return;
    }

    resultDiv.innerHTML = "Creating your edit...";

    try {
        const res = await fetch(`/shorten?url=${encodeURIComponent(url)}`);
        const data = await res.json();

        if (data.short_url) {
            resultDiv.innerHTML = `Short Link: <a href="${data.short_url}" target="_blank">${data.short_url}</a>`;
        } else {
            resultDiv.innerHTML = "Something went wrong!";
        }
    } catch (error) {
        resultDiv.innerHTML = "Connection error!";
    }
}