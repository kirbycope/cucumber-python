# cucumber-python
[Cucumber](https://cucumber.io/) is a software tool that supports behavior-driven development (BDD). </br>
[Python](https://www.python.org/) is an interpreted high-level general-purpose programming language. </br>
[Selenium](https://selenium.dev) is an open-source automated testing framework for web applications.

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

# Getting Started
1. Install [Python3](https://www.python.org/downloads/)
1. Clone this repo
1. Open the root folder using [VS Code](https://code.visualstudio.com/)
   * If you use [GitHub Desktop](https://desktop.github.com/), select the "Open in Visual Studio" button
1. Select "Terminal" > "New Terminal"
1.  Install dependencies noted in [requirements.txt](/requirements.txt)
   * [mac] Run `python3 -m pip install -r requirements.txt`
   * [win] Run `py -3 -m pip install -r requirements.txt`
1. In the root folder create a new file called `.env`
1. Copy+Paste the following
   ```
   TEST_BASE_URL="https://the-internet.herokuapp.com"
   TEST_USER="tomsmith"
   TEST_PASS="SuperSecretPassword!"
   ```
1. Save
1. Run tests
   * [mac] In terminal run `behave`
   * [win] In terminal run `py -3 -m behave`
