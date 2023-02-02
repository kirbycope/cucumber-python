Feature: Main scene

    Scenario Outline: Pause a run
        Given I open the <name> scene
        When I start running and pause
        Then I should see the Pause Menu

        Examples:
            | name |
            | Main |
