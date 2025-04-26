async function checkNews() {
    const newsText = document.getElementById('newsInput').value;
    const newsURL = document.getElementById('urlInput').value;
    const resultDiv = document.getElementById('result');
    const previewDiv = document.getElementById('preview');
    const spinner = document.getElementById('spinner');

    if (!newsText && !newsURL) {
        resultDiv.innerHTML = '<span class="text-danger">Please enter text or a URL.</span>';
        previewDiv.innerHTML = '';
        return;
    }

    resultDiv.innerHTML = '';
    previewDiv.innerHTML = '';
    spinner.style.display = 'block';

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: newsText, url: newsURL }),
        });

        const data = await response.json();
        spinner.style.display = 'none';

        if (response.ok) {
            const colorClass = data.prediction === 'Fake' ? 'text-danger' : 'text-success';
            resultDiv.innerHTML = `<span class="${colorClass}">Prediction: ${data.prediction}<br>Confidence: ${data.confidence}%</span>`;

            if (data.preview) {
                previewDiv.innerHTML = `<strong>Preview of Analyzed Text:</strong><br>${data.preview}`;
            }
        } else {
            resultDiv.innerHTML = `<span class="text-danger">Error: ${data.error}</span>`;
        }
    } catch (error) {
        spinner.style.display = 'none';
        resultDiv.innerHTML = `<span class="text-danger">Error: Unable to connect to the server.</span>`;
    }
    fetchHistory();  // After result is shown


}

async function fetchHistory() {
    const historyList = document.getElementById('historyList');
    historyList.innerHTML = '';

    const response = await fetch('http://127.0.0.1:5000/history');
    const history = await response.json();

    history.forEach(item => {
        const li = document.createElement('li');
        li.className = 'list-group-item';
        li.innerHTML = `<strong>${item.result}</strong> (${item.confidence}% confidence) <br> <small>${item.date}</small>`;
        historyList.appendChild(li);
    });
}

// Call this after each prediction



function clearForm() {
    document.getElementById('newsInput').value = '';
    document.getElementById('result').innerHTML = '';
    document.getElementById('spinner').style.display = 'none';
    document.getElementById('newsInput').focus();
    }
    

