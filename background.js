chrome.runtime.onInstalled.addListener(() => {
  console.log('AI Routing Assistant installed.');
});
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'executeWorkflow') {
    console.log('Executing workflow with data:', request.data);
    // Placeholder for workflow execution logic
    sendResponse({status: 'Workflow executed'});
  }
});