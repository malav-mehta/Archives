// Hangman by Malav Mehta and Justin Lu (Tuesday, April 23, 2019, Mr. Hudson, ICS20-01).
// this file is used to generate the game and make the game work

gameTable = document.createElement("table"); // empty game table created at the beginning that will be removed and replaced each time a new game is generated
innerGameDiv.appendChild(gameTable);
multiplayerSubmit.addEventListener("click", getSecretWord); // event listener to get the multiplayer input

function generateGame() {
    innerGameDiv.removeChild(gameTable); // clearing the table for the game
    gameTable = document.createElement("table");
    letterCount = 0;
    category = categoryNode.nodeValue;
    secretWord = "h_ngm_n";
    allowedGuesses = difficultyInput.value;
    wrongGuesses = 0; // resetting all the values to generate and restart the game
    remainingGuesses = allowedGuesses - wrongGuesses;
    innerGameDiv.setAttribute("style", `background-image: url(assets/images/hangman/${wrongGuesses + 8 - allowedGuesses}.png);`); // hangman image generated in the background of the game, based on the amount of guesses used/left

    if (timerInput.value != 0) { // only starts the timer if the user wanted it
        timeLeft = timerInput.value; // time left is the same as the timer input value in seconds, and is converted to the mm:ss format for the user interface
        timer = setInterval(startTimer, 1000); // starts the timer, decrementally reducing the timeLeft value until the time runs out and the lose parameters are triggered
    }

    switch (category) { // the secret word is generated based on the selected category
        case "cities":
            secretWord = generateSecretWord(cities);
            break;
        case "countries":
            secretWord = generateSecretWord(countries);
            break;
        case "food":
            secretWord = generateSecretWord(food);
            break;
        case "animals":
            secretWord = generateSecretWord(animals);
            break;
        case "multiplayer":
            showModal(); // multiplayer input div is shown in the multiplayer game mode
            break;
        default:
            secretWord = generateSecretWord(random);
            break;
    }

    for (let letterRowCount = 0; letterRowCount < 2; letterRowCount++) { // generating all the letter buttons, first for loop goes through the rows
        var letterRow = document.createElement("tr");
        for (let letterCellCount = 0; letterCellCount < 13; letterCellCount++) { // second for loops creating all the letter buttons in groups of 13
            var letterCell = document.createElement("td");
            var letterNode = String.fromCharCode(letterCount + 97);

            var letterButton = document.createElement("button");
            letterButton.setAttribute("style", "width: 3.2em; margin-right: 0.2em; padding: 0.3em; border-radius: 0.5em;");
            letterButton.appendChild(document.createTextNode(letterNode));
            letterButton.id = letterNode; // used for the check input function, which uses the "this.id" method to identify the inputted button
            letterButton.addEventListener("click", checkInput); // assigning function to click

            letterCell.appendChild(letterButton);
            letterRow.appendChild(letterCell); // appending everything
            letterCount++;
        }
        gameTable.appendChild(letterRow);
    }

    thirdRow = document.createElement("tr"); // third row contains everything else
    generalCell = document.createElement("td");
    generalCell.colSpan = "5";
    generalCell.style.textAlign = "center"; // general cell contains miscellaneous items/features of the game

    inputForm = document.createElement("form");
    fullGuess = document.createElement("input"); // takes in full guess from the user if necessary
    fullGuess.id = "input";
    fullGuess.className = "gameInput";
    fullGuess.placeholder = "guess in full here...";

    window.onkeypress = function(event) { // keybinding the enter key to the submitting the gull guess above
        if (event.key == "Enter") {
            event.preventDefault();
            checkInput();
        }
    }

    submitGuess = document.createElement("button"); // submit guess button for the full guess input
    submitGuess.id = "input";
    submitGuess.className = "formButton";
    submitGuess.appendChild(document.createTextNode("submit"));
    submitGuess.type = "button";
    submitGuess.addEventListener("click", checkInput);

    inputForm.appendChild(fullGuess);
    inputForm.appendChild(submitGuess);
    generalCell.appendChild(inputForm); // appending input related elements to the cell

    timerContainer = document.createElement("h4"); // element where the timer is displayed (if enabled), otherwise the message of line 89 is automatically displayed
    timerNode = document.createTextNode("timer disabled");
    timerContainer.appendChild(timerNode);
    generalCell.appendChild(timerContainer);

    remainingGuessesContainer = document.createElement("p"); // shows how many wrong guesses the use can still guess without losing (how many lives are left)
    remainingGuesses = document.createTextNode(`you have ${remainingGuesses} wrong guesses left`);
    remainingGuessesContainer.appendChild(remainingGuesses);
    generalCell.appendChild(remainingGuessesContainer);

    guessedContainer = document.createElement("p"); // shows all the guesses made using the input element rather than the buttons (as the buttons themselves show that they are guessed, but the input element does not)
    guessedContainer.className = "guessedContainer";
    guessedNode = document.createTextNode("you have guessed: ");
    guessedContainer.appendChild(guessedNode);
    generalCell.appendChild(guessedContainer);

    hintButton = document.createElement("button"); // generates one hint per game for the user
    hintButtonNode = document.createTextNode("get hint");
    hintButton.appendChild(hintButtonNode);
    hintButton.addEventListener("click", generateHint);
    generalCell.appendChild(hintButton);

    thirdRow.appendChild(generalCell);

    secretWordCell = document.createElement("td"); // shows the blank secret word for the user
    secretWordCell.colSpan = "8";
    secretWordContainer = document.createElement("h3");
    secretWordNode = document.createTextNode("h_ngm_n");
    secretWordContainer.appendChild(secretWordNode);
    secretWordCell.appendChild(secretWordContainer);
    thirdRow.appendChild(secretWordCell);
    gameTable.appendChild(thirdRow);

    blankWordList = createBlankWord("_", secretWord.length).split(""); // the blank word (blank as in dashed word) show in the form of a list

    for (let progress = 0; progress < secretWord.length; progress++) { // checks for and removes spaces in the blank/dashed word
        if (secretWord.charAt(progress) == String.fromCharCode(32)) {
            blankWordList[progress] = String.fromCharCode(32);
        }
    }

    secretWordNode.nodeValue = blankWordList.join(""); // the blank word list joined is displayed to the user

    innerGameDiv.appendChild(gameTable); // the game table is re-appended to the game div/page
}

function createBlankWord(string, wordLength) { // creates the blank/dashed word
    var repeatedString = "";
    while (wordLength > 0) { // the string is copied wordLength times
        repeatedString += string;
        wordLength--;
    }
    return repeatedString;
}

function getSecretWord() { // getting the secret word in the multiplayer mode
    multiplayerDiv.style.display = "none";
    secretWord = multiplayerInput.value.toLowerCase();
    multiplayerInput.value = "";
    blankWordList = createBlankWord("_", secretWord.length).split("");
    for (let progress = 0; progress < secretWord.length; progress++) {
        if (secretWord.charAt(progress) == String.fromCharCode(32)) {
            blankWordList[progress] = String.fromCharCode(32);
        }
    }
    secretWordNode.nodeValue = blankWordList.join("");
    winWordNode.nodeValue = secretWord;
    loseWordNode.nodeValue = secretWord;
}

function generateSecretWord(possibleWords) { // secretWord generated based on the given list
    secretWord = possibleWords[Math.floor(Math.random() * possibleWords.length)].toLowerCase()
    winWordNode.nodeValue = secretWord; // win and lose divs updated to show the secret word when the user finished the game
    loseWordNode.nodeValue = secretWord;
    return secretWord;
}

function generateHint() { // a hint is generated for the user
    hintOver = 1;
    while (hintOver == 1) {
        randomLetter = secretWord.charAt(Math.floor(Math.random() * secretWord.length)); // a letter in the secret word is generated until this newly generated letter hasn't been guessed already
        if (!(blankWordList.join("").includes(randomLetter))) { // checking if the generated letter was already guessed
            hintOver = 0;
            hintButtonNode.nodeValue = `try "${randomLetter}"`; // displays hint on the button
            hintButton.disabled = true; // only one hint available: the button is disabled afterwards
            break;
        }
    }
}

function checkInput() { // game engine of sorts, checks the input and sets the win/lose conditions
    var input = this.id; // works for the buttons

    if (input == "input" || input == undefined) { // validates/cancels input if it is not valid
        input = fullGuess.value.toLowerCase();
        if (input == "") { // if the input element was blank, then the submit is disregarded
            return null; // ends the function (to disregard the input element submission)
        }
        fullGuess.value = ""; // input value is reset
        guessedNode.nodeValue += `${input}; `; // the guessed value is added to the the guessed node
    } else if (input != "input") { // if it was not the input element that triggered the checkValue function to be called
        var pressedButton = document.getElementById(input); // getting the pressedButton
        pressedButton.disabled = true; // disabking it so that it can't be pressed more than once, and the color is set to red in the below line
        pressedButton.setAttribute("style", "background-image: linear-gradient(270deg, #faaca860, #ff512f60, #dd247660, #ed213a60, #93291e60); background-size: 1000% 1000%; -webkit-animation: gradientAnimation 6s ease infinite; animation: gradientAnimation 6s ease infinite; border: none; width: 3.2em; margin-right: 0.2em; padding: 0.3em; border-radius: 0.5em;");
    }

    if (secretWord.includes(input)) { // if the guess was successful
        rightAudio.play() // right guess audio plats
        for (let progress = 0; progress < secretWord.length; progress++) { // updating the displayed blank/dashed word
            if (secretWord.charAt(progress) == input) {
                blankWordList[progress] = input;
            }
        }

        try { // setting the color to green because the guess was correct
            pressedButton.setAttribute("style", "background-image: linear-gradient(270deg, #6dd5ed60, #56ab3f60, #a8e06360, #00cdac60); background-size: 800% 800%; -webkit-animation: gradientAnimation 6s ease infinite; animation: gradientAnimation 6s ease infinite; border: none; width: 3.2em; margin-right: 0.2em; padding: 0.3em; border-radius: 0.5em;");
        } catch (err) { // ignoring the error when the input element was used and the pressedButton variable was undefined
            throw (err);
        } finally {
            secretWordNode.nodeValue = blankWordList.join("");
            if ((blankWordList.includes("_") == false) || secretWord == input) { // checking winning conditions
                secretWordNode.nodeValue = secretWord;
                userWonGame(); // game won
            }
        }
    } else {
        wrongGuesses++; // wrong guess
        wrongAudio.play(); // wrong guess audio is played
        if (wrongGuesses == allowedGuesses) { // checking losing conditions
            userLostGame(); // game lost
        }
    }
    innerGameDiv.setAttribute("style", `background-image: url(assets/images/hangman/${wrongGuesses + 8 - allowedGuesses}.png);`); // updating hangman based on the amount of guesses there are left
    remainingGuesses.nodeValue = `you have ${allowedGuesses - wrongGuesses} wrong guesses left` // updating amount of remaining guesses
}

function userWonGame() {
    bgAudio.pause();
    winAudio.play(); // win audio played by briefly pausing the score
    setTimeout(function() {
        bgAudio.play();
    }, 6000);
    loadingDiv.setAttribute("style", "transform: scale(1, 1); height: 85vh;"); // regular transition occurs
    loadingDiv.className = "loadingDiv";
    loadingDivSpace.className = "spaceDiv"
    loadingDivSpace.scrollIntoView();
    setTimeout(function() {
        homeDivSpace.className = "hidden";
        homeDiv.className = "hidden";
        settingsDivSpace.className = "hidden";
        settingsDiv.className = "hidden";
        gameDivSpace.className = "hidden";
        gameDiv.className = "hidden";
        aboutDivSpace.className = "hidden";
        aboutDiv.className = "hidden";
        winDivSpace.className = "hidden";
        winDiv.className = "winDiv";
        loseDivSpace.className = "hidden";
        loseDiv.className = "hidden";
        endDivSpace.className = "hidden";
        endDiv.className = "hidden";
        statsDivSpace.className = "hidden";
        statsDiv.className = "hidden";
        statsDivSpace.scrollIntoView();
    }, 1000);
    setTimeout(function() {
        loadingDiv.setAttribute("style", "transform: scale(0, 0); height: 0;");
    }, 2000);

    wins++;
    total = wins + losses;
    statsRatio.nodeValue = `${Math.round(wins / total * 100)}%`;
    statsLose.nodeValue = `${losses} time(s)`;
    statsWin.nodeValue = `${wins} time(s)`;
    clearInterval(timer);
    window.onkeypress = function(event) {
        if (event.key == "Enter") {
            event.preventDefault();
            endGame();
        }
    }
}

function userLostGame() {
    bgAudio.pause();
    loseAudio.play(); // lose audio played after briefly pausing the score
    setTimeout(function() {
        bgAudio.play();
    }, 3100);
    loadingDiv.setAttribute("style", "transform: scale(1, 1); height: 85vh;"); // regular transitional function followed
    loadingDiv.className = "loadingDiv";
    loadingDivSpace.className = "spaceDiv"
    loadingDivSpace.scrollIntoView();
    setTimeout(function() {
        homeDivSpace.className = "hidden";
        homeDiv.className = "hidden";
        settingsDivSpace.className = "hidden";
        settingsDiv.className = "hidden";
        gameDivSpace.className = "hidden";
        gameDiv.className = "hidden";
        aboutDivSpace.className = "hidden";
        aboutDiv.className = "hidden";
        winDivSpace.className = "hidden";
        winDiv.className = "hidden";
        loseDivSpace.className = "hidden";
        loseDiv.className = "loseDiv";
        endDivSpace.className = "hidden";
        endDiv.className = "hidden";
        statsDivSpace.className = "hidden";
        statsDiv.className = "hidden";
        statsDivSpace.scrollIntoView();
    }, 1000);
    setTimeout(function() {
        loadingDiv.setAttribute("style", "transform: scale(0, 0); height: 0;");
    }, 2000);

    losses++;
    total = wins + losses;
    statsRatio.nodeValue = `${Math.round(wins / total * 100)}%`;
    statsLose.nodeValue = `${losses} time(s)`;
    statsWin.nodeValue = `${wins} time(s)`;
    clearInterval(timer);
    window.onkeypress = function(event) {
        if (event.key == "Enter") {
            event.preventDefault();
            endGame();
        }
    }
}

function startTimer() { // timer function
    if ((timeLeft % 60).toString().length < 2) { // checks if the seconds value is less than 10 (to add a zero before the value for the mm:ss format to display properly)
        timerNode.nodeValue = `0${(timeLeft - timeLeft % 60) / 60}:0${timeLeft % 60}`; // displaying the time left variables (originally in seconds) to the mm:ss format of displaying time
    } else {
        timerNode.nodeValue = `0${(timeLeft - timeLeft % 60) / 60}:${timeLeft % 60}`;
    }

    if (timeLeft == 0) { // if no more time is left, the user loses the game (losing condition)
        userLostGame(); // game is lost 
    }
    timeLeft--; // time decreases each time the funciton is run at the set interval defined above
}