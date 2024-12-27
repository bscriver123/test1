// Placeholder for content script logic
console.log('Content script loaded.');
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'interactWithAI') {
    console.log('Interacting with AI service:', request.service);
    // Placeholder for AI interaction logic
    sendResponse({status: 'Interaction complete'});
  }
});