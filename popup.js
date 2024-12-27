document.getElementById('run-workflow').addEventListener('click', () => {
    const mainPrompt = document.getElementById('main-prompt').value;
    const routingDiagram = document.getElementById('routing-diagram').value;
    chrome.runtime.sendMessage({
        action: 'executeWorkflow',
        data: {
            mainPrompt: mainPrompt,
            routingDiagram: routingDiagram
        }
    }, response => {
        document.getElementById('output-display').innerText = response.status;
    });
});