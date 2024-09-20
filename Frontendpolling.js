async function fetchData() {
    const response = await fetch('/api/get-latest-events');
    const data = await response.json();
    const eventList = document.getElementById('event-list');
    eventList.innerHTML = '';  // Clear previous list
    
    data.forEach(event => {
        let message = '';
        if (event.type === 'push') {
            message = `${event.author} pushed to ${event.branch} on ${new Date(event.timestamp).toLocaleString()}`;
        } else if (event.type === 'pull_request') {
            message = `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${new Date(event.timestamp).toLocaleString()}`;
        } else if (event.type === 'merge') {
            message = `${event.author} merged branch ${event.from_branch} to ${event.to_branch} on ${new Date(event.timestamp).toLocaleString()}`;
        }
        const listItem = document.createElement('li');
        listItem.textContent = message;
        eventList.appendChild(listItem);
    });
}

setInterval(fetchData, 15000);  // Poll every 15 seconds
