chrome.runtime.onInstalled.addListener(() => {
  console.log('AI Routing Assistant installed.');
});
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'executeWorkflow') {
    const { mainPrompt, routingDiagram } = request.data;
    console.log('Executing workflow with main prompt:', mainPrompt);
    console.log('Routing diagram:', routingDiagram);
    // TODO: Implement workflow execution logic
    sendResponse({status: 'Workflow execution started'});
  }
});