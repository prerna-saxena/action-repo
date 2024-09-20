To implement this project, here's a structured approach:

1. GitHub Webhooks Integration
Setup Webhook: In your GitHub repository, go to Settings → Webhooks → Add Webhook.
Specify the payload URL (your Flask app's endpoint URL), and choose the events (push, pull_request, and merge) to trigger the webhook.
2. Flask App Setup
Flask Endpoint: Create an endpoint in Flask to handle incoming webhook events.
Handle Data: Parse and process the GitHub webhook payload to extract necessary data.
Store in MongoDB: Save the processed data to MongoDB using a defined schema.

Frontend Polling (UI)
Poll MongoDB every 15 seconds using a Flask API or a similar endpoint.
Display Events: Depending on the event type (push, pull request, merge), format and display them.


5. UI Design
Keep it minimal with a clean layout, displaying the latest events in a list.
Use simple CSS or a framework like Tailwind CSS to style the page.
6. Testing and Deployment
Test using GitHub by triggering Push, Pull Request, and Merge actions.
Share the link to the repository and the live Flask application as required.
This approach should cover the core functionality, webhook integration, MongoDB storage, and the UI polling mechanism.
