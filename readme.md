To receive a Discord notification when a user makes a merge in GitHub, you can use GitHub webhooks to send the necessary information to your Discord server. Here are the general steps you'll need to follow:

    Create a new webhook on your Discord server. Go to Server Settings > Integrations > Webhooks and click "Create Webhook". Give the webhook a name, choose a channel to post the notifications to, and copy the webhook URL.

    In your GitHub repository, go to Settings > Webhooks and click "Add webhook". Paste the Discord webhook URL into the "Payload URL" field and choose "application/json" as the content type. Then, select the events you want to trigger the webhook (in this case, "Pull request reviews" and "Pull requests"). Click "Add webhook" to save your changes.

    Now, you'll need to set up a script that receives the webhook payload from GitHub and formats it into a message that can be posted to Discord. You can use a programming language like Python to do this. Here's some sample code that shows how to parse the GitHub webhook payload and send a message to a Discord webhook using the Requests library:

    ---- CODE -----

    Once you've created your script, you'll need to host it somewhere so that it can receive the webhook requests from GitHub. You can use a cloud platform like Heroku or Google Cloud Platform to do this.

    In this version of the script, we're extracting the issue number, author, and URL from the pull_request object in the GitHub webhook payload, and using them to construct a message that includes the issue number in the notification. You can customize the message formatting to suit your needs.

    In this version of the script, we're passing the Discord username of the user who triggered the webhook as a separate argument to the send_discord_notification function, and including it in the notification message using string interpolation. We're also setting the username field in the Discord webhook payload to "GitHub", which will be displayed as the username of the bot that sends the notification. You can customize the username field to suit your needs.