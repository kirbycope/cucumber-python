Feature: Start Game

    Scenario Outline: Test Start Game
        Given I open the scene <name>
        When I foo
        Then I bar
        
        Examples:
            | name                    |
            | Scene 2 Draggable Panel |
