![Screenshot of deployed pp3](/images/screenshot%20of%20deployed%20project.png)

# **Jog On Text-Based Adventure Game**
<br>

[Click Here to Go To Live Site](https://jogging-adventure-rpg.herokuapp.com/)
<br>

This short RPG was inspired by my love of listening to true crime shows and knack for catastrophising every-day life. The dangers of jogging are brought to life in this fun little game where the choices the player makes during the game decide how the game ends.
The purpose of this game is just to entertain the user. It is aimed at teens to adults who are not particularily fond of jogging and running.
<br>

## UX 
<br>

### User Stories
<br>

+ A user of this site would want:
1. to be able to initiate the game easily.
2. to be able to read the storyline easily.
3. to enjoy playing a simple, humorous game.
4. to see how different answers impact the outcome of the game.
5. to be able to interact with the game easily.

+ As the creator of this game, I want to:
1. provide a simple game for the user.
2. have the user enjoy it.
3. give the user a simple to read rpg.
<br>

### Strategy
The purpose of this project is to create a game using Python to be deployed using Heroku.
I created a flowchart to visualise the different tracks the different choices would go through as it becomes more complicated to follow as each decision builds on the one before it. 
<br>

![Flowchart of Jog On Game](images/Jogging%20Game%20Flowchart.png)

<br>

## Design

As the focus of this project was the use of Python rather than on the aesthetics using CSS or HTML I kept the design aspects to the experience of reading the code and of the storyline on the app. To do this I used newlines to space out the lines on the terminal and the sleep module of the time function to add small delays in between the printed strings.
This slowed down the app to make it easier for the user to follow and broke up the blocks of text, making it more comfortable to read. 
<br>

### Future design ideas

- I would have liked to add some color and ascii art to the project and may do so in the future.
- If I had more time to develop the app, I would like to add more decisions to the storyline.
- I would like to add some random functioning to the storyline for a more interesting game.
<br>

## Features

![Intro](images/Player%20Name%20Input.png)
<br>

- The first feature that meets the player is the introduction. The player is asked to input their name which is capitalized by the app.
<br>

![Player Greeting](images/Player%20Greeting%20.png)
<br>

- The player greeting includes the player's previously inputted name and asks them if they want to go on. If they choose not to, the game over message is shown.
If they choose to continue, the storyline brings them onto the next decision they need to make.
<br>

![choice 1 and 2](images/Choice%201%20and%202.png)
<br>

- Choice 1 asks if they are ready to go and Choice 2 asks which direction they want to go. Each answer brings up a storyline and another choice to make.
<br>

![Choice 3](images/choice%203.png)
<br>

- Choice 3 will depend on the previous answers the player gave.
<br>

![game over](images/game%20over%20and%20replay%20option.png)
<br>

- Depending on the choices the player made, they may get the game over message if the made the wrong decisions. They will then be asked if they wish to play again or to end the game.
<br>

![you survived!](images/You%20survived.png)
<br>

- If the player makes it home safe they will see the 'you survived!' message. They will also be asked if they want to play again.
<br>

## Technologies used in this project:
<br>

- Python
- GitHub
- Heroku
- Python Tutor
- app.diagrams.net to make flowcharts
- GitPod
<br>

## Testing
<br>
I tested the app on Chrome, Microsoft Edge, FireFox browsers and it worked well on all these. I couldn't test on iPhone or Safari but was advised it wouldn't work on those. It did work ok on my Samsung Galaxy Note 8.
<br>

## Manual Testing
<br>


|**Feature**  |  **Test**              | **Check For**  | **Outcome** |
| ----------- | ---------------------  | -------------- |        ---: |
|Name Input   | input name, not blank  |    input       |  Pass       |
|Ready to Go  | Input yes or no only   |    valid input |  Pass       |
|Choice1      | choose left/right      |    valid input |  Pass       |
|Choice2      | input from list        |    valid input |  Pass       |
|Choice3      | input from list        |    valid input |  Pass       |
|Play Again   | input play,restart     |    restart     |  Pass       |
|Play Again   | input quit, sys.exit() |    goodbye     |  Pass       |
||||

<br>

## Validation
<br>
As advised by tutors due to pep8 no longer working, I validated using a linter in gitPod workspace called pycodestyle. It showed no warnings or problems at all as in screenshot below.
<br>

![no issues showing](images/no%20issues%20showing%20validation.png)
<br>

## Deployment 
<br>

This project was created on GitPod, then pushed to GitHub where it was connected to Heroku.
Everytime the project was pushed to GitHub, Heroku automatically deployed the updated version as the automatic box was ticked as opposed to the box for manual update.
<br>

### To Deploy
<br>

- Once logged into your GitHub account, choose the repository you wish to deploy.
  The repo for this project can be accessed [here](https://github.com/ShellyBrady/PP3Text_Based_RPG).
- Log in to Heroku and choose to create a new app.
- Name app, choose region and click the 'create app' button.
- Add Python Buildpack, then Node.js Buildpack.
- Connect to GitHub in the Deployment Method section. Search the repo name to be deployed   and click on 'connect' when it shows as chosen on the screen.
-  Select to update deployment automatically if you with Heroku to update each time you push to GitHub.
- Choose the main branch, or master if main isn't there and deploy.
<br>

### To Fork and Clone the repository
<br>

If you need instructions to fork or clone the repo please see the following links:
- [fork repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

- [clone repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository)
<br>


## Credits and Acknowledgements
<br>
Sites I used for general Python knowledge while working on this project:

- https://realpython.com/
- https://learn.codeinstitute.net/
- https://www.w3schools.com/python
- https://app.slack.com/
- https://docs.python.org/
- https://stackoverflow.com/
- https://www.geeksforgeeks.org/
- https://www.markdownguide.org/
- https://docs.github.com/en/repositories
<br>