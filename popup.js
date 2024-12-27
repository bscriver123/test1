document.getElementById('run-workflow').addEventListener('click', () => {
    const mainPrompt = document.getElementById('main-prompt').value;
    console.log('Running workflow with prompt:', mainPrompt);
    // Placeholder for running the workflow
    document.getElementById('output-display').innerText = 'Workflow executed. Check console for details.';
});