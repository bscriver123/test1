document.getElementById('run-workflow').addEventListener('click', () => {
    const mainPrompt = document.getElementById('main-prompt').value;
    const routingDiagram = document.getElementById('routing-diagram').value;
    console.log('Running workflow with prompt:', mainPrompt);
    console.log('Using routing diagram:', routingDiagram);
    // Placeholder for running the workflow
    document.getElementById('output-display').innerText = 'Workflow executed. Check console for details.';
});