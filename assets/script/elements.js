// Hangman by Malav Mehta and Justin Lu (Tuesday, April 23, 2019, Mr. Hudson, ICS20-01).
// this file is creates all the elements for the game

var body = document.createElement("center");
document.body.appendChild(body);

// importing audio for the game

// the background audio
bgAudio = document.createElement("audio");
bgAudioFile = document.createElement("source");
bgAudioFile.src = "assets/audio/background.mp3";
bgAudioFile.type = "audio/mpeg";
bgAudio.appendChild(bgAudioFile);
bgAudio.volume = 0.25; // lowering the volume so that the music is less intrusive


// audio played at wrong guesses
wrongAudio = document.createElement("audio");
wrongAudioFile = document.createElement("source");
wrongAudioFile.src = "assets/audio/wrong.mp3";
wrongAudioFile.type = "audio/mpeg";
wrongAudio.appendChild(wrongAudioFile);

// audio played on successful guesses
rightAudio = document.createElement("audio");
rightAudioFile = document.createElement("source");
rightAudioFile.src = "assets/audio/right.mp3";
rightAudioFile.type = "audio/mpeg";
rightAudio.appendChild(rightAudioFile);

// audio played on win
winAudio = document.createElement("audio");
winAudioFile = document.createElement("source");
winAudioFile.src = "assets/audio/win.mp3";
winAudioFile.type = "audio/mpeg";
winAudio.appendChild(winAudioFile);


// audio played on loss
loseAudio = document.createElement("audio");
loseAudioFile = document.createElement("source");
loseAudioFile.src = "assets/audio/lose.mp3";
loseAudioFile.type = "audio/mpeg";
loseAudio.appendChild(loseAudioFile);

window.addEventListener("click", initialAudioPlayback); // chrome doesn't allow for audio to be autoplayed, so the audio begins playing when the user focuses on the window (by clicking on it)

function initialAudioPlayback() {
    bgAudio.play();
    window.removeEventListener("click", initialAudioPlayback); // once the audio starts, the bind is removed
}

// top navigation bar
navBar = document.createElement("ul");
navBar.className = "header"

navListItem = document.createElement("li");
navListItem.className = "navLogo";

navItem = document.createElement("img"); // header image fixed on the left side of the page
navItem.setAttribute("src", "assets/images/branding/logo.png");
navItem.setAttribute("height", "35px");
navItem.setAttribute("style", "float: left; cursor: pointer;");
navItem.addEventListener("click", showHome)

navBar.appendChild(navListItem);
navListItem.appendChild(navItem);

for (let navCounter = 0; navCounter < 4; navCounter++) { // creating all nav bar items as list items
    navListItem = document.createElement("li");
    navItem = document.createElement("a");
    navBar.appendChild(navListItem);
    navListItem.appendChild(navItem);

    switch (navCounter) {
        case 0:
            navItem.appendChild(document.createTextNode("home"));
            navItem.addEventListener("click", showHome);
            break;
        case 1:
            navItem.appendChild(document.createTextNode("settings"));
            navItem.addEventListener("click", showSettings);
            break;
        case 2:
            navItem.appendChild(document.createTextNode("game"));
            navItem.addEventListener("click", showGame);
            break;
        default:
            navItem.appendChild(document.createTextNode("about"));
            navItem.addEventListener("click", showAbout);
            break;
    }
}

body.appendChild(navBar);

loadingDivSpace = document.createElement("div"); // the loading space displayed on page switches
loadingDivSpace.className = "hidden";
body.appendChild(loadingDivSpace);

loadingDiv = document.createElement("div");
loadingDiv.className = "hidden"
body.appendChild(loadingDiv);

// space before the home div to have whitespace above the div itself (format copied for each subsequent div/page)
homeDivSpace = document.createElement("div");
homeDivSpace.className = "spaceDiv";
body.appendChild(homeDivSpace);

// home page
homeDiv = document.createElement("div");
homeDiv.style.padding = "0";
innerHomeDiv = document.createElement("div");
innerHomeDiv.className = "homeDiv";

homeTitle = document.createElement("h1");
homeTitle.appendChild(document.createTextNode("h_ngm_n"));

homeButton = document.createElement("button");
homeButton.className = "homeButton";
homeArrow = document.createElement("img");
homeArrow.src = "assets/images/other/heroarrow.png";
homeArrow.setAttribute("height", "20px");
homeButton.appendChild(homeArrow);
homeButton.addEventListener("mouseover", enlargeHomeButton); // changing the image size on mouseover/out
homeButton.addEventListener("mouseout", normalHomeButton);
homeButton.addEventListener("click", showSettings);

innerHomeDiv.appendChild(homeTitle);
innerHomeDiv.appendChild(homeButton);
innerHomeDiv.appendChild(document.createElement("br"));
innerHomeDiv.appendChild(document.createElement("br"));
homeDiv.appendChild(innerHomeDiv);
body.appendChild(homeDiv);

settingsDivSpace = document.createElement("div");
settingsDivSpace.className = "hidden";
settingsDivSpace.appendChild(document.createElement("br"));
settingsDivSpace.appendChild(document.createElement("br"));
body.appendChild(settingsDivSpace);

// settings page
settingsDiv = document.createElement("div"); // outer div has the gradient background
settingsDiv.className = "hidden" // inner div is white, creating the gradient border effect (same effect applied on all divs other than the home/splash div/page)
innerSettingsDiv = document.createElement("div");
innerSettingsDiv.className = "contentDiv";

// content on this div and subsequent divs are organized into two cells in a table: one for the header and one for the content (other than the game page, all other divs/pages follow this organisation method)
settingsTable = document.createElement("table");
settingsRow = document.createElement("tr");
settingsCell1 = document.createElement("td");
settingsCell2 = document.createElement("td");
settingsCell2.setAttribute("style", "transform: translateX(-10vw);");
settingsRow.appendChild(settingsCell1);
settingsRow.appendChild(settingsCell2);
settingsTable.appendChild(settingsRow);


settingsTitle = document.createElement("h2");
settingsTitle.appendChild(document.createTextNode("settings"));

settingsCell1.appendChild(settingsTitle);

settingsDescription = document.createElement("p");
settingsDescription.appendChild(document.createTextNode("choose the game settings below..."));

settingsCell2.appendChild(settingsDescription);

// settings form to select name, category, difficulty and timer options
var settingsForm = document.createElement("form");
var nameInput = document.createElement("input");
nameInput.id = "nameInput";
nameInput.setAttribute("placeholder", "enter gamertag here...");

var categoryInput = document.createElement("select");
categoryInput.setAttribute("id", "category");
var categoryOption;

for (let categoryCounter = 0; categoryCounter < 7; categoryCounter++) { // the loop creates all the options for the category "select" input
    categoryOption = document.createElement("option");

    switch (categoryCounter) {
        case 0:
            var defaultCategory = categoryOption;
            categoryOption.setAttribute("value", "random");
            var categoryText = document.createTextNode("hi no name! click here to choose a category");
            defaultCategory.appendChild(categoryText);
            break;

        case 1:
            categoryOption.setAttribute("value", "cities");
            categoryOption.appendChild(document.createTextNode("cities"));
            break;

        case 2:
            categoryOption.setAttribute("value", "countries");
            categoryOption.appendChild(document.createTextNode("countries"));
            break;

        case 3:
            categoryOption.setAttribute("value", "food");
            categoryOption.appendChild(document.createTextNode("food"));
            break;

        case 4:
            categoryOption.setAttribute("value", "animals");
            categoryOption.appendChild(document.createTextNode("animals"));
            break;

        case 5:
            categoryOption.setAttribute("value", "random");
            categoryOption.appendChild(document.createTextNode("random"));
            break;

        default:
            categoryOption.setAttribute("value", "multiplayer");
            categoryOption.appendChild(document.createTextNode("multiplayer"));
            break;
    }

    categoryInput.appendChild(categoryOption);
}

// select a difficulty
var difficultyInput = document.createElement("select");
var difficultyOption;

for (let difficultyCounter = 0; difficultyCounter < 5; difficultyCounter++) {
    difficultyOption = document.createElement("option");

    switch (difficultyCounter) {
        case 0:
            var defaultDifficulty = difficultyOption;
            var difficultyText = document.createTextNode("click here to choose a difficulty");
            defaultDifficulty.appendChild(difficultyText);
            difficultyOption.setAttribute("value", 8);
            break;

        case 1:
            difficultyOption.appendChild(document.createTextNode("easy (8 guesses)"));
            difficultyOption.setAttribute("value", 8);
            break;

        case 2:
            difficultyOption.appendChild(document.createTextNode("regular (6 guesses)"));
            difficultyOption.setAttribute("value", 6);
            break;

        case 3:
            difficultyOption.appendChild(document.createTextNode("hard (4 guesses)"));
            difficultyOption.setAttribute("value", 4);
            break;

        default:
            difficultyOption.appendChild(document.createTextNode("crazy (2 guesses)"));
            difficultyOption.setAttribute("value", 2);
            break;
    }

    difficultyInput.appendChild(difficultyOption);
}

// updates game screen title on category input, which also determines the word cateogry that wil be selected for the game
categoryInput.oninput = function() {
    categoryNode.nodeValue = categoryInput.value;
}

// choosing a name that will be used in the end game screen as well as the default category option input
nameInput.oninput = function() {
    categoryText.nodeValue = `hi ${nameInput.value}! click here to choose a category`;
    thanksNode.nodeValue = `thank you for playing our game ${nameInput.value}. we hope you enjoyed it.`;
}


// timer function
var timerInput = document.createElement("select");
var timerOption;

for (let timerOptionCounter = 0; timerOptionCounter < 5; timerOptionCounter++) { // creates all timer options
    timerOption = document.createElement("option");
    timerOption.setAttribute("value", timerOptionCounter * 30);

    switch (timerOptionCounter) {
        case 0:
            timerOption.appendChild(document.createTextNode("disable timer"));
            break;
        case 1:
            timerOption.appendChild(document.createTextNode("00:30"));
            break;
        case 2:
            timerOption.appendChild(document.createTextNode("01:00"));
            break;
        case 3:
            timerOption.appendChild(document.createTextNode("01:30"));
            break;
        default:
            timerOption.appendChild(document.createTextNode("02:00"));
            break;
    }

    timerInput.appendChild(timerOption);
}

// append everything
settingsForm.appendChild(nameInput);
settingsForm.appendChild(document.createElement("br"));
settingsForm.appendChild(categoryInput);
settingsForm.appendChild(document.createElement("br"));
settingsForm.appendChild(difficultyInput);
settingsForm.appendChild(document.createElement("br"));
settingsForm.appendChild(timerInput);


// button to start game
settingsButton = document.createElement("button");
settingsButton.appendChild(document.createTextNode("play now \u2192"));
settingsButton.addEventListener("click", showGame);

settingsCell2.appendChild(settingsForm);

innerSettingsDiv.appendChild(settingsTable);
innerSettingsDiv.appendChild(settingsButton);
settingsDiv.appendChild(innerSettingsDiv);
body.appendChild(settingsDiv);

gameDivSpace = document.createElement("div");
gameDivSpace.className = "hidden";
body.appendChild(gameDivSpace);

// game page
var gameDiv, innerGameDiv, gameTitle, categoryNode, gameCenter;

gameDiv = document.createElement("div"); // divs structured the same way as before
gameDiv.className = "hidden";
gameDiv.setAttribute("style", "padding: 0; width: 100%;");
outerGameDiv = document.createElement("div");
innerGameDiv = document.createElement("div");
innerGameDiv.className = "hangmanDiv";

gameTitle = document.createElement("h2");
gameTitle.setAttribute("style", "transform: none; padding: 0; margin: 0; line-spacing: 0;");
categoryNode = document.createTextNode("random");
gameTitle.appendChild(categoryNode);
innerGameDiv.appendChild(gameTitle);

gameCenter = document.createElement("center");
outerGameDiv.appendChild(innerGameDiv);
gameCenter.appendChild(outerGameDiv);
gameDiv.appendChild(gameCenter);
body.appendChild(gameDiv);

aboutDivSpace = document.createElement("div");
aboutDivSpace.className = "hidden";
body.appendChild(aboutDivSpace);

// about page
aboutDiv = document.createElement("div");
aboutDiv.className = "hidden";
innerAboutDiv = document.createElement("div");
innerAboutDiv.className = "contentDiv";

aboutTable = document.createElement("table");
aboutRow = document.createElement("tr");
aboutCell1 = document.createElement("td");
aboutCell2 = document.createElement("td");
aboutCell2.setAttribute("style", "transform: translateX(-5vw);");
aboutRow.appendChild(aboutCell1);
aboutRow.appendChild(aboutCell2);
aboutTable.appendChild(aboutRow);

aboutTitle = document.createElement("h2");
aboutTitle.appendChild(document.createTextNode("about"));
aboutCell1.appendChild(aboutTitle);

// first section of the about page, containing contact information
aboutTitle2 = document.createElement("h3");
aboutTitle2.appendChild(document.createTextNode("contact"));
aboutCell2.appendChild(aboutTitle2);

aboutParagraph = document.createElement("p");
aboutParagraph.appendChild(document.createTextNode("This website was created as part of the ICS 2O course offered at Colonel By Secondary School (Ottawa, ON). Contact Malav Mehta and Justin Lu for more information about this project or to provide feedback, contact us via email at mmeht1@ocdsb.ca and jlu1@ocdsb.ca."));
aboutCell2.appendChild(aboutParagraph);

// second section of the about page, containing the game rules
aboutSubtitle = document.createElement("h3");
aboutSubtitle.appendChild(document.createTextNode("rules"));

aboutSubparagraph = document.createElement("p");
aboutSubparagraph.appendChild(document.createTextNode("A random word will be chosen as the secret word, based on the category you choose. Attempt to guess the word by guessing individual letters. If the letter isn't in the word then another body part of the hangman will appear on the gallows. Guess to world completely in the permitted guesses to win."));

aboutCell2.appendChild(aboutSubtitle);
aboutCell2.appendChild(aboutSubparagraph);

innerAboutDiv.appendChild(aboutTable);
aboutDiv.appendChild(innerAboutDiv);
body.appendChild(aboutDiv);

winDivSpace = document.createElement("div");
winDivSpace.className = "hidden";
body.appendChild(winDivSpace);

// victory screen (defeat screen follows same structure, although the background gradient colors and text differ)
winDiv = document.createElement("div");
winDiv.className = "hidden";
innerWinDiv = document.createElement("div");
innerWinDiv.className = "contentDiv";

winTable = document.createElement("table");
winRow = document.createElement("tr");
winCell1 = document.createElement("td");
winCell2 = document.createElement("td");
winCell2.setAttribute("style", "text-align: center");

winTitle = document.createElement("h2");
winTitle.appendChild(document.createTextNode("win"));
winCell1.appendChild(winTitle);

winParagraph = document.createElement("p");
winParagraph.appendChild(document.createTextNode("congratulations, you win (+1 points)! the secret word was:"));
winCell2.appendChild(winParagraph);

winSecretWordTitle = document.createElement("h3");
winWordNode = document.createTextNode("secret word");
winSecretWordTitle.appendChild(winWordNode);
winCell2.appendChild(winSecretWordTitle);

// replay button and end game button (as replicated on the lose page)
winButtonAgain = document.createElement("button");
winButtonAgain.appendChild(document.createTextNode("play again \u2192"));
winButtonAgain.addEventListener("click", playAgain);

winButtonEnd = document.createElement("button");
winButtonEnd.appendChild(document.createTextNode("end game \u2192"));
winButtonEnd.addEventListener("click", endGame);

winRow.appendChild(winCell1);
winRow.appendChild(winCell2);
winTable.appendChild(winRow);

innerWinDiv.appendChild(winTable);
winCell2.appendChild(winButtonAgain);
winCell2.appendChild(winButtonEnd);

winDiv.appendChild(innerWinDiv);
body.appendChild(winDiv);

loseDivSpace = document.createElement("div");
loseDivSpace.className = "hidden";
body.appendChild(loseDivSpace);

// defeat screen
loseDiv = document.createElement("div");
loseDiv.className = "hidden";
innerLoseDiv = document.createElement("div");
innerLoseDiv.className = "contentDiv";

loseTable = document.createElement("table");
loseRow = document.createElement("tr");
loseCell1 = document.createElement("td");
loseCell2 = document.createElement("td");
loseCell2.setAttribute("style", "text-align: center");

loseTitle = document.createElement("h2");
loseTitle.appendChild(document.createTextNode("loss"));
loseCell1.appendChild(loseTitle);

loseParagraph = document.createElement("p");
loseParagraph.appendChild(document.createTextNode("sorry, you lose (-1 points)! the secret word was:"));
loseCell2.appendChild(loseParagraph);

loseSecretWordTitle = document.createElement("h3");
loseWordNode = document.createTextNode("secret word");
loseSecretWordTitle.appendChild(loseWordNode);
loseCell2.appendChild(loseSecretWordTitle);

loseButtonAgain = document.createElement("button");
loseButtonAgain.appendChild(document.createTextNode("play again \u2192"));
loseButtonAgain.addEventListener("click", playAgain);

loseButtonEnd = document.createElement("button");
loseButtonEnd.appendChild(document.createTextNode("end game \u2192"));
loseButtonEnd.addEventListener("click", endGame);

loseRow.appendChild(loseCell1);
loseRow.appendChild(loseCell2);
loseTable.appendChild(loseRow);

innerLoseDiv.appendChild(loseTable);
loseCell2.appendChild(loseButtonAgain);
loseCell2.appendChild(loseButtonEnd);

loseDiv.appendChild(innerLoseDiv);
body.appendChild(loseDiv);

endDivSpace = document.createElement("div");
endDivSpace.className = "hidden";
body.appendChild(endDivSpace);

// game over div
endDiv = document.createElement("div");
endDiv.className = "hidden";
innerEndDiv = document.createElement("div");
innerEndDiv.className = "contentDiv";

endTable = document.createElement("table");
endRow = document.createElement("tr");
endCell1 = document.createElement("td");
endCell2 = document.createElement("td");
endCell2.setAttribute("style", "transform: translateX(-5vw);");

endTitle = document.createElement("h2");
endTitle.appendChild(document.createTextNode("thanks"));
endCell1.appendChild(endTitle);

// end game message
endParagraph = document.createElement("p");
thanksNode = document.createTextNode("thank you for playing our game. we hope you enjoyed it.")
endParagraph.appendChild(thanksNode);
endCell2.appendChild(endParagraph);

// statistics button
endStatsButton = document.createElement("button");
endStatsButton.appendChild(document.createTextNode("view stats"));
endStatsButton.addEventListener("click", showStats);
endCell2.appendChild(endStatsButton);

// about page button
endAboutButton = document.createElement("button");
endAboutButton.appendChild(document.createTextNode("about \u2192"));
endAboutButton.addEventListener("click", showAbout)
endCell2.appendChild(endAboutButton);

endRow.appendChild(endCell1);
endRow.appendChild(endCell2);
endTable.appendChild(endRow);

innerEndDiv.appendChild(endTable);
endDiv.appendChild(innerEndDiv);
body.appendChild(endDiv);

statsDivSpace = document.createElement("div");
statsDivSpace.className = "hidden";
body.appendChild(statsDivSpace);

// stats div
statsDiv = document.createElement("div");
statsDiv.className = "hidden";
innerStatsDiv = document.createElement("div");
innerStatsDiv.className = "contentDiv";

statsTable = document.createElement("table");
statsRow = document.createElement("tr");
statsCell1 = document.createElement("td");
statsCell2 = document.createElement("td");
statsCell2.setAttribute("style", "text-align: center");
statsCell3 = document.createElement("td");

statsTitle = document.createElement("h2");
statsTitle.appendChild(document.createTextNode("stats"));
statsCell1.appendChild(statsTitle);

statsRatioPara = document.createElement("p");
statsRatioPara.appendChild(document.createTextNode("your success rate is"))
statsCell2.appendChild(statsRatioPara);
statsCell2.appendChild(document.createElement("br")); // maintaining space between paragraphs to replicate the header side
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));

statsRatioTitle = document.createElement("h3"); // headers used for the actual stats to emphasize them
statsRatio = document.createTextNode("0%");
statsRatioTitle.appendChild(statsRatio);
statsCell3.appendChild(statsRatioTitle);

statsWinPara = document.createElement("p");
statsWinPara.appendChild(document.createTextNode("you have won")); // this and the below two stats categories are duplicates of the above, although the numbers are changed
statsCell2.appendChild(statsWinPara);
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));
statsCell2.appendChild(document.createElement("br"));

statsWinTitle = document.createElement("h3");
statsWin = document.createTextNode("0 time(s)");
statsWinTitle.appendChild(statsWin);
statsCell3.appendChild(statsWinTitle);

statsLosePara = document.createElement("p");
statsLosePara.appendChild(document.createTextNode("your have lost"));
statsCell2.appendChild(statsLosePara);

statsLoseTitle = document.createElement("h3");
statsLose = document.createTextNode("0 time(s)");
statsLoseTitle.appendChild(statsLose);
statsCell3.appendChild(statsLoseTitle);

statsRow.appendChild(statsCell1);
statsRow.appendChild(statsCell2);
statsRow.appendChild(statsCell3);
statsTable.appendChild(statsRow); // appending everything

innerStatsDiv.appendChild(statsTable);
statsDiv.appendChild(innerStatsDiv);
body.appendChild(statsDiv);
body.appendChild(document.createElement("br"));
body.appendChild(document.createElement("br"));
body.appendChild(document.createElement("br"));

multiplayerDiv = document.createElement("center"); // modal used to create a box that gets the secret word in the multiplayer mode of hangman
multiplayerDiv.className = "modal";
multiCenter = document.createElement("center");
insideDiv = document.createElement("div");
insideDiv.className = "modal-content";

multiDescription = document.createElement("p");
multiDescription.appendChild(document.createTextNode("in multiplayer mode, one player must first create a secret word (letters only)"))

multiplayerForm = document.createElement("form");
multiplayerInput = document.createElement("input");
multiplayerInput.setAttribute("pattern", "[A-Za-z ]+"); // regular expression is used to regulate user input
multiplayerInput.placeholder = "enter custom secret word here...";

multiplayerSubmit = document.createElement("button");
multiplayerSubmit.appendChild(document.createTextNode("submit"));
multiplayerSubmit.type = "button";
multiplayerSubmit.className = "formButton";

multiplayerForm.appendChild(multiplayerInput);
multiplayerForm.appendChild(multiplayerSubmit);
insideDiv.appendChild(multiDescription);
insideDiv.appendChild(multiplayerForm);
multiCenter.appendChild(insideDiv);

multiplayerDiv.appendChild(multiCenter);
body.appendChild(multiplayerDiv);

window.onkeypress = function(event) { // keybinding buttons on different divs to facilitate navigating between the pages of the game
    if (event.key == "Enter") {
        event.preventDefault();
        showSettings();
    }
}

function enlargeHomeButton() { // functions which control the arrow size on the home page
    homeArrow.setAttribute("height", "40px");
}

function normalHomeButton() {
    homeArrow.setAttribute("height", "20px");
}

function showHome() { // same structure as this function used to change between all the pages (all functions are seperately defined below)
    window.onkeypress = function(event) { // keybinding changes for each page
        if (event.key == "Enter") {
            event.preventDefault();
            showSettings();
        }
    }
    loadingDiv.setAttribute("style", "transform: scale(1, 1); height: 85vh;"); // loading div image grows, hiding the content
    loadingDiv.className = "loadingDiv";
    loadingDivSpace.className = "spaceDiv" // loading div image takes up the entire window, completeley hiding the content
    loadingDivSpace.scrollIntoView();
    setTimeout(function() {
        homeDivSpace.className = "hidden";
        homeDiv.className = "visible";
        settingsDivSpace.className = "hidden";
        settingsDiv.className = "hidden";
        gameDivSpace.className = "hidden";
        gameDiv.className = "hidden";
        aboutDivSpace.className = "hidden";
        aboutDiv.className = "hidden";
        winDivSpace.className = "hidden";
        winDiv.className = "hidden";
        loseDivSpace.className = "hidden";
        loseDiv.className = "hidden";
        endDivSpace.className = "hidden";
        endDiv.className = "hidden";
        statsDivSpace.className = "hidden";
        statsDiv.className = "hidden";
        homeDivSpace.scrollIntoView();
    }, 2000);
    setTimeout(function() {
        loadingDiv.setAttribute("style", "transform: scale(0, 0); height: 0;"); // loading div shrinks down, transitioning into the wanted page
    }, 2000);
    clearInterval(timer);
}

function showSettings() {
    window.onkeypress = function(event) {
        if (event.key == "Enter") {
            event.preventDefault();
            showGame();
        }
    }
    loadingDiv.setAttribute("style", "transform: scale(1, 1); height: 85vh;");
    loadingDiv.className = "loadingDiv";
    loadingDivSpace.className = "spaceDiv"
    loadingDivSpace.scrollIntoView();
    setTimeout(function() {
        homeDivSpace.className = "hidden";
        homeDiv.className = "hidden";
        settingsDivSpace.className = "hidden";
        settingsDiv.className = "visible";
        gameDivSpace.className = "hidden";
        gameDiv.className = "hidden";
        aboutDivSpace.className = "hidden";
        aboutDiv.className = "hidden";
        winDivSpace.className = "hidden";
        winDiv.className = "hidden";
        loseDivSpace.className = "hidden";
        loseDiv.className = "hidden";
        endDivSpace.className = "hidden";
        endDiv.className = "hidden";
        statsDivSpace.className = "hidden";
        statsDiv.className = "hidden";
        settingsDivSpace.scrollIntoView();
    }, 1000);
    setTimeout(function() {
        loadingDiv.setAttribute("style", "transform: scale(0, 0); height: 0;");
    }, 2000);
    try {
        clearInterval(timer);
    } catch (err) {
        throw (err);
    }
}

function showGame() {
    loadingDiv.setAttribute("style", "transform: scale(1, 1); height: 85vh;");
    loadingDiv.className = "loadingDiv";
    loadingDivSpace.className = "spaceDiv"
    loadingDivSpace.scrollIntoView();
    setTimeout(function() {
        homeDivSpace.className = "hidden";
        homeDiv.className = "hidden";
        settingsDivSpace.className = "hidden";
        settingsDiv.className = "hidden";
        gameDivSpace.className = "hidden";
        gameDiv.className = "contentDiv";
        aboutDivSpace.className = "hidden";
        aboutDiv.className = "hidden";
        winDivSpace.className = "hidden";
        winDiv.className = "hidden";
        loseDivSpace.className = "hidden";
        loseDiv.className = "hidden";
        endDivSpace.className = "hidden";
        endDiv.className = "hidden";
        statsDivSpace.className = "hidden";
        statsDiv.className = "hidden";
        gameDivSpace.scrollIntoView();
    }, 1000);
    setTimeout(function() {
        loadingDiv.setAttribute("style", "transform: scale(0, 0); height: 0;");
    }, 2000);
    try {
        clearInterval(timer);
    } catch (err) {
        throw (err);
    }
    generateGame();
}

function showAbout() {
    loadingDiv.setAttribute("style", "transform: scale(1, 1); height: 85vh;");
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
        aboutDiv.className = "visible";
        winDivSpace.className = "hidden";
        winDiv.className = "hidden";
        loseDivSpace.className = "hidden";
        loseDiv.className = "hidden";
        endDivSpace.className = "hidden";
        endDiv.className = "hidden";
        statsDivSpace.className = "hidden";
        statsDiv.className = "hidden";
        aboutDivSpace.scrollIntoView();
    }, 1750);
    setTimeout(function() {
        loadingDiv.setAttribute("style", "transform: scale(0, 0); height: 0;");
    }, 2000);
    clearInterval(timer);
}

function playAgain() {
    window.onkeypress = function(event) {
        if (event.key == "Enter") {
            event.preventDefault();
            showSettings();
        }
    }
    loadingDiv.setAttribute("style", "transform: scale(1, 1); height: 85vh;");
    loadingDiv.className = "loadingDiv";
    loadingDivSpace.className = "spaceDiv"
    loadingDivSpace.scrollIntoView();
    setTimeout(function() {
        homeDivSpace.className = "hidden";
        homeDiv.className = "hidden";
        settingsDivSpace.className = "hidden";
        settingsDiv.className = "visble";
        gameDivSpace.className = "hidden";
        gameDiv.className = "hidden";
        aboutDivSpace.className = "hidden";
        aboutDiv.className = "hidden";
        winDivSpace.className = "hidden";
        winDiv.className = "hidden";
        loseDivSpace.className = "hidden";
        loseDiv.className = "hidden";
        endDivSpace.className = "hidden";
        endDiv.className = "hidden";
        statsDivSpace.className = "hidden";
        statsDiv.className = "hidden";
        settingsDivSpace.scrollIntoView();
    }, 1000);
    setTimeout(function() {
        loadingDiv.setAttribute("style", "transform: scale(0, 0); height: 0;");
    }, 2000);
    try {
        clearInterval(timer);
    } catch (err) {
        throw (err);
    }
}

function endGame() {
    window.onkeypress = function(event) {
        if (event.key == "Enter") {
            event.preventDefault();
            showStats();
        }
    }
    loadingDiv.setAttribute("style", "transform: scale(1, 1); height: 85vh;");
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
        loseDiv.className = "hidden";
        endDivSpace.className = "hidden";
        endDiv.className = "visible";
        statsDivSpace.className = "hidden";
        statsDiv.className = "hidden";
        endDivSpace.scrollIntoView();
    }, 1000);
    setTimeout(function() {
        loadingDiv.setAttribute("style", "transform: scale(0, 0); height: 0;");
    }, 2000);
    try {
        clearInterval(timer);
    } catch (err) {
        throw (err);
    }
}

function showStats() {
    window.onkeypress = function(event) {
        if (event.key == "Enter") {
            event.preventDefault();
            showHome();
        }
    }
    loadingDiv.setAttribute("style", "transform: scale(1, 1); height: 85vh;");
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
        loseDiv.className = "hidden";
        endDivSpace.className = "hidden";
        endDiv.className = "hidden";
        statsDivSpace.className = "hidden";
        statsDiv.className = "visible";
        statsDivSpace.scrollIntoView();
    }, 1000);
    setTimeout(function() {
        loadingDiv.setAttribute("style", "transform: scale(0, 0); height: 0;");
    }, 2000);
    try {
        clearInterval(timer);
    } catch (err) {
        throw (err);
    }
}

function showModal() {
    multiplayerDiv.style.display = "block"; // showing the multiplayer modal
    multiplayerDiv.onkeypress = function(event) { //  changing binding for the modal
        if (event.key == "Enter") {
            event.preventDefault();
            getSecretWord();
        }
    }
}