# cucumber-python
[Cucumber](https://cucumber.io/) is a software tool that supports behavior-driven development (BDD). </br>
[Python](https://www.python.org/) is an interpreted high-level general-purpose programming language.

## Core Concepts
* [Behaviour Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development) is an agile software development process that encourages collaboration among developers, quality assurance testers, and customer representatives in a software project.
  * Stakeholders might be used to the User Story template; ["As a … I want … So that …"](https://martinfowler.com/bliki/UserStory.html)
  * Developers might be used to a unit test design pattern; ["Arrange, Act, Assert"](http://wiki.c2.com/?ArrangeActAssert)
  * Cucumber expresess functionality using keywords; ["Given, When, Then"](https://en.wikipedia.org/wiki/Given-When-Then)
* [Fluent Interface](https://en.wikipedia.org/wiki/Fluent_interface) is an object-oriented API whose design relies extensively on method chaining.
  * PageObect.someFunction()
  * PageOject.someElement().click()
* [Page Object Model](https://www.selenium.dev/documentation/en/guidelines_and_recommendations/page_object_models/) is a Design Pattern which has become popular in test automation for enhancing test maintenance and reducing code duplication. </br>
  * The "login" screen will have a "Login page object" that contains the selectors for elements on the page and functions that can be performed on that page.

## Getting Started
1. Install [NodeJS](https://nodejs.org/en/) LTS
1. Install [Python3](https://www.python.org/downloads/)
1. [Android] Install [Android Studio](https://developer.android.com/studio) and [create an AVD](https://developer.android.com/studio/run/managing-avds)
1. Clone this repo
1. Open the root folder using [VS Code](https://code.visualstudio.com/)
   * If you use [GitHub Desktop](https://desktop.github.com/), select the "Open in Visual Studio" button
1. Open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal)
1. Install Appium by running `npm i appium`
1. Install dependencies noted in [requirements.txt](/requirements.txt)
   * In the integrated terminal run `python3 -m pip install -r requirements.txt`
1. In the root folder create a new file called `.env`
1. Copy+Paste the following
   ```
   TEST_BASE_URL="https://the-internet.herokuapp.com"
   TEST_USER="tomsmith"
   TEST_PASS="SuperSecretPassword!"
   ```
1. Save

## Run Tests

### AltUnity (Unity Mobile Apps)
[AltUnity](https://altom.gitlab.io/altunity/altunitytester) is a free, open source asset. Its main goal is to enable UI test automation, by instrumenting games to get access and programmatically control the Unity objects.</br>
The [apk](/trashcat.apk) is included as part of _this_ sample repo.

With the [AVD](https://developer.android.com/studio/run/emulator-commandline) running:
   * [mac] In the integrated terminal run `behave altunity_tester/features`
   * [win] In the integrated terminal run `python3 -m behave altunity_tester/features`

### Appium (Mobile Apps)
[Appium](https://appium.io) is an open source automation tool for running scripts and testing native applications, mobile-web applications and hybrid applications on Android or iOS using a webdriver. </br>
Example tests use https://developer.android.com/training/basics/firstapp </br>
The [apk](/app-debug.apk) is included as part of _this_ sample repo.

With the [AVD](https://developer.android.com/studio/run/emulator-commandline) running:
   * [mac] In the integrated terminal run `behave appium_webdriver/features`
   * [win] In the integrated terminal run `python3 -m behave appium_webdriver/features`

### Selenium (Web Apps)
[Selenium](https://selenium.dev) is an open-source automated testing framework for web applications. </br>
Example tests use https://the-internet.herokuapp.com/login

   * [mac] In the integrated terminal run `behave selenium_webdriver/features`
   * [win] In the integrated terminal run `python3 -m behave selenium_webdriver/features`

## Python Tips and Tricks

### Clear Dependencies

   * [mac] In the integrated terminal run `pip3 freeze | xargs pip uninstall -y`
   * [win] In the integrated terminal run `pip3 uninstall -y -r <(pip freeze)`

### Hide pycache from VS Code's Explorer
1. Open the [Command Pallete](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
1. Search for and then select "Preferences: Open User Settings"
1. Seach for `files.exclude`
1. Select the "Add Pattern" button
1. Enter `**/__pycache__`
   - Repeat `**/node_modules`
