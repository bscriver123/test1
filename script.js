document.getElementById('run-workflow').addEventListener('click', function() {
    const prompt = document.getElementById('prompt-input').value;
    document.getElementById('output-display').innerText = `Running workflow with prompt: ${prompt}`;
});

document.getElementById('clear').addEventListener('click', function() {
    document.getElementById('prompt-input').value = '';
    document.getElementById('output-display').innerText = '';
});