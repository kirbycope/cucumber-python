Feature: MainActivity.kt

    Scenario Outline: Send Message
        Given I am on the main activity
        When I send a message saying <message>
        Then I should see a message saying <message>

        Examples:
            | message       |
            | Hello, World! |
