# NOTES:

When developing: follow 80/20. If it takes 80% of your time to develop and automate something that provides only 20% values, drop it and implement `terminal`.

# Main Flow

## Farm hashtags

1. Start the application
-- app starts and opens up the browsers
-- app prompts you several accounts with usernames and passwords to use to login
2. Login to Instagram
3. Confirm on app. Begin 5 second countdown before hashtag farming begins
-- app begins farming hashtags around a certain niche
-- interactions with the terminal can occur to change the queue? << FUTURE UPGRADE >>

## Farm users & niches

TBD

## Farm popular posts from users in my niche / market

1. 

# Commands

```pytest```  
```python main.py```  


# Dev Notes

## File Structure

```
|_ x
  |_ .venv
  |_ .vscode
  |_ src
    |_ agents
      |_ instagram.py
      |_ browser.py
      |_ agent.py
      |_ dtos.py
    |_ builders
      |_ content_builder
        |_ node_modules
        |_ public
      |
      |_ bot_builder.py
      |_ username_builder.py
    |_ console
    |_ controls
    |_ data
    |_ http_listener
    |_ interaction_logger
    |_ utils
    |_ virtualization
    |
    |_ app.py
    |_ programs.py
    |_ state.py
```