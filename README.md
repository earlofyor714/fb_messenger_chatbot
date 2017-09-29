Alex's Chatbot API

A simple chatbot designed to run on FB Messenger.  Hosted on Heroku.

====================

Structure:

application.py   : Web application setup, and the main file.
requirements.txt : Configurations for dependencies for Heroku
procfile         : Run configurations for Heroku
Vagrantfile      : Configurations if you want to run a VM locally.  Not set up with Heroku.

====================

Heroku Instructions:

1. Commit and push changes to git
2. From command line: 'git push heroku master'
3. 'heroku ps:scale web=1'
4. To view: 'heroku open'

To add configurations to heroku:

  'heroku config:add <config_name>=<value>'

To view logs:
  'heroku logs --tail'

====================