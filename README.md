# TarockMasters

## LEARNING
We used Q-learning to train our models. Because of the complexity of the game in terms of playing order we started with Q-learning that did not add the estimate of the optimal future value (qf1). We then added this functionality but taking into consideration that we should substract (rather than add) the estimated optimal future value if the next player was our opponent (qf2). The logic here is very straightforward. If our action is good in the current scope but sets our opponent up for a really good action then our action should still be considered bad. We also combined these 2 approaches with 3 different reward functions:

1.) The reward is equal to the points in the current stack but its weighted by the number of actions the agent was able to take (rwf1)\
2.) We take the reward from point 1. and add some domain knowledge (rwf2)\
3.) We play the entire game and then whether the player won or lost the game we reward/punish every action taken by the player (rwf3)


This gives us a total of 6 different learning approaches. In combination with 4 different state, action pairs (described in detail below) this gives us a total of 24 trained models.

## THEORETICAL AGENTS
For purposes of evaluation of our trained models we devised a few theoretical agents.

- Random agent (random): Makes decisions randomly.

The following agents are a sort of cheating agents because they have more information than usually available to the player. They know every card in every hand instead of just their own. This of course is not possible in real world play, but results achieved with such agents present a great milestone for our trained models.

- Locally worst agent (LW): Plays the card that will on average produce the lowest possible score for that round.
- Locally best agent (LB): Plays the card that will on average produce the highest possible score for that round.
- Locally worst worst agent (LWW): Plays the card that will produce the lowest possible score for that round but also takes into account that the other two players will play in the same way
- Locally best best agent (LBB): Plays the card that will produce the highest possible score for that round but also takes into account that the other two players will play in the same way

## TESTING
There are 2 ways we can look at our Tarock playing program. Either as a normal player playing against other programs or as a program playing versus other players. The distinction is that in the case where we treat our program as a player, we use its logic to replace only 1 of the 3 players while in the other case we use our logic to replace 2 players. So far we've treated the program as a normal player so we ran all the test in this way. 

We tested all 24 models versus all 5 theoretical agents. Each model played 15000 games versus each agent. We chose 15000 games because that should be enough games to cover all possible qualities of cards multiple times. We also tested our model versus the program called Silicijasti tarokist but so far only chose a single model for each state, action pair and played 100 games with it. 50 games where we play in a duo and 50 games where we play alone.

We do not perform any bidding or talon exchanging as of yet. We randomly choose between "Naprej" and "Solo brez". We do however account for card quality when processing the results using the function below:

```
def good_cards(hand):
    king_count = 0

    for card in hand:
        if card in [8,18,28, 38]:
            king_count += 1

    tarock_count = 0
    for card in hand:
        if card >= 40:
            tarock_count += 1

    if king_count < 2:
        return 0

    if king_count == 2:
        if tarock_count >= 6:
            return 1
        else:
            return 0

    if king_count >= 2:
        if tarock_count >= 8:
            return 2
        else:
            if tarock_count >= 5:
                return 1
            else:
                return 0
```
*This assessment of hand quality could be improved (by much possibly?) by taking the games where all three players played according to the same theoretical agent. The results of those games should tell us something about the quality of the hands. Perhaps even train a regression model?*

## RESULTS
### PLAYING WITH THEORETICAL AGENTS
![alt text](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/All%20variations%20of%20model%201_1%20playing%20vs%20milestone%20agents.png

## 1_1 Q AGENT
### STATE 1
Two separate Q tables were created, one for playing the first card of the round and another for playing the second and third card of the round. The tables below show each variable used in state representations as well as all the possible values of that variable. We will not explain every single variable in detail since most are pretty self explanatory. The main idea was to discretize the game state to a certain extent.

**Q table for playing the first card of the round**
|Variable name|Possible variable values|
|-------------|------------------------|
|"imas kralja"|[0, 1]|
|"imas damo"|[0,1]|
|"imas pob/caval"|[0,1]|
|"imas platlca"|[0,1]|
|"imam se tarokov"| [0,1]|
|"player2 nima vec tarokov"|[0,1]|
|"player3 nima vec tarokov"|[0,1]|


**Q table for playing the second and third card of the round**
|Variable name|Possible variable values|
|-------------|------------------------|
|"vrednost igranih kart"| [1, 2, 3]|
|"skrt igrane karte"|[0,1]|
|"lahko poberes igrane karte"| [0,1]|
|"player2 skrt igrane karte"| [0,1]|
|"player3 skrt igrane karte"| [0,1]|
|"imam se tarokov"| [0,1]|
|"player2 nima vec tarokov"| [0,1]|
|"player3 nima vec tarokov"| [0,1]|

### ACTIONS 1
Actions used for playing the first card of the round: "play king", "play queen", "play knight/jack", "play platlc", "play tarok".  
Actions used for playing the second and third card of the round: "win current stack", "pass current stack".


## 2_2 Q AGENT

### STATE 2
Only one Q table was created for use in every situation of the game. The table below shows which variables were used to describe the state of the game.

***Q table for every play***
|Variable name|Possible variable values|
|-------------|------------------------|
|"herc kralj"| [0,1,2]|
|"herc dama"| [0,1,2]|
|"kara kralj"| [0,1,2]|
|"kara dama"| [0,1,2]|
|"pik kralj"| [0,1,2]|
|"pik dama"| [0,1,2]|
|"kriz kralj"| [0,1,2]|
|"kriz dama"| [0,1,2]|
|"mond"| [0,1,2]|
|"skis"| [0,1,2]|
|"pagat"| [0,1,2]|
|"vrednost stacka"| [0,1,2]|
|"player2 brez tarokov"| [0, 1]|
|"player3 brez tarokov"| [0, 1]|

### ACTIONS 2
Playing each specific card in the deck presented a single action which in total gave us 52 possible actions. Of course not each action is possible in every state.



## 3_3 Q AGENT
### STATE 3
We devised a total of 6 Q tables, one for each turn in a round (first, second, third) and all three with respect to whether the player is playing solo or in a duo.

***Q table for playing solo, first card***
|Variable name|Possible variable values|
|-------------|------------------------|
|"herc kralj"| [0,1,2]|
|"herc dama"| [0, 1]|
|"karo kralj"| [0,1,2]|
|"karo dama"| [0, 1]|
|"pik kralj"| [0,1,2]|
|"pik dama"| [0, 1]|
|"kriz kralj"| [0,1,2]|
|"kriz dama"| [0, 1]|
|"nizki taroki"| [0,1]|
|"srednji taroki"| [0,1]|
|"visoki taroki"| [0,1]|
|"player2 skrt herc"| [0,1]|
|"player2 skrt karo"| [0,1]|
|"player2 skrt pik"| [0,1]|
|"player2 skrt kriz"| [0,1]|
|"player2 skrt taroki"| [0,1]|
|"player3 skrt herc"| [0,1]|
|"player3 skrt karo"| [0,1]|
|"player3 skrt pik"| [0,1]|
|"player3 skrt kriz"| [0,1]|
|"player3 skrt taroki"| [0,1]|]


***Q table for solo second card***
|Variable name|Possible variable values|
|-------------|------------------------|
|"vrednost prve karte"| [0,2,3,4,5]|
|"a je prva karta tarok"| [0,1]|
|"a sm skrt te barve"| [0,1]|
|"a lahko poberem z barvo"| [0,1]|
|"a lahko poberem s tarokom"| [0,1]|
|"nizki taroki"| [0,1]|
|"srednji taroki"| [0,1]|
|"visoki taroki"| [0,1]|
|"mam kralja te barve"| [0,1]|
|"mam damo te barve"| [0,1]|
|"mam cavala te barve"| [0,1]|
|"mam poba te barve"| [0,1]|
|"mam platlca te barve"| [0,1]|
|"zadnji player skrt barve"| [0,1]|
|"zadnji player skrt tarokov"| [0,1]|


***Q table for solo third card***
|Variable name|Possible variable values|
|-------------|------------------------|
|"vrednost prve karte"| [0,2,3,4,5]|
|"vrednost druge karte"| [0,2,3,4,5]|
|"a je prva karta tarok"| [0,1]|
|"a sm skrt te barve"| [0,1]|
|"a lahko poberem z barvo"| [0,1]|
|"a lahko poberem s tarokom"| [0,1]|
|"nizki taroki"| [0,1]|
|"srednji taroki"| [0,1]|
|"visoki taroki"| [0,1]|
|"mam kralja te barve"| [0,1]|
|"mam damo te barve"| [0,1]|
|"mam cavala te barve"| [0,1]|
|"mam poba te barve"| [0,1]|
|"mam platlca te barve"| [0,1]|


***Q tables for duo play***   
Q tables for duo play are the same as for the solo play for each turn respectively. But they have two additional variables "partner za mano" and "partner pobere".


### ACTIONS 3
Actions for playing the first card of the round: "herc kral", "herc dama", "herc kaval", "herc pob", "herc platlc", "karo kral", "karo dama", "karo kavla", "karo pob", "karo platlc", "pik kral", "pik dama", "pik kaval", "pik pob", "pik platlc", "kriz kral", "kriz dama", "kriz kaval", "kriz pob", "kriz platlc", "nizek tarok", "srednji tarok", "visok tarok".    
Actions for playing the other two cards of the round: "pass", "poberi", "stegni se".    

## 5_5 Q AGENT

### STATE 5
We took the idea in STATE 3 and expanded on it by making more descriptive states. 

***Q table for playing solo, first card***
|Variable name|Possible variable values|
|-------------|------------------------|
|"Kral herc"| [0, 1, 2]|
|"Dama herc"| [0, 1, 2]|
|"Kaval herc"| [0, 1, 2]|
|"Pob herc"| [0, 1, 2]|
|"Platlci herc"| [0, 1]|
|"Stevilo hercev v igri"| [0, 1, 2, 3, 4, 5, 6, 7, 8]|
|"2. player skrt"| [0, 1]|
|"3. player skrt"| [0, 1]|
|"Kral karo"| [0, 1, 2]|
|"Dama karo"| [0, 1, 2]|
|"Kaval karo"| [0, 1, 2]|
|"Pob karo"| [0, 1, 2]|
|"Platlci karo"| [0, 1]|
|"Stevilo kar v igri"| [0, 1, 2, 3, 4, 5, 6, 7, 8]|
|"2. player skrt"| [0, 1]|
|"3. player skrt"| [0, 1]|
|"Kral pik"| [0, 1, 2]|
|"Dama pik"| [0, 1, 2]|
|"Kaval pik"| [0, 1, 2]|
|"Pob pik"| [0, 1, 2]|
|"Platlci pik"| [0, 1]|
|"Stevilo pikov v igri"| [0, 1, 2, 3, 4, 5, 6, 7, 8]|
|"2. player skrt"| [0, 1]|
|"3. player skrt"| [0, 1]|
|"Kral kriz"| [0, 1, 2]|
|"Dama kriz"| [0, 1, 2]|
|"Kaval kriz"| [0, 1, 2]|
|"Pob kriz"| [0, 1, 2]|
|"Platlci kriz"| [0, 1]|
|"Stevilo krizev v igri"| [0, 1, 2, 3, 4, 5, 6, 7, 8]|
|"2. player skrt"| [0, 1]|
|"3. player skrt"| [0, 1]|
|"škis"| [0, 1, 2]|
|"mond"| [0, 1, 2]|
|"pagat"| [0, 1, 2]|
|"II - VII"| [0, 1, 2]|
|"VIII - XV"| [0, 1, 2]|
|"XVI - XX"| [0, 1, 2]|


***Q table for playing solo, second card***
|Variable name|Possible variable values|
|-------------|------------------------|
|"Jz skrt barve"| [0, 1]|
|"Lahko poberem"| [0, 1]|
|"Kralj barve stacka"| [0, 1, 2]|
|"Dama barve stacka"| [0, 1, 2]|
|"Kaval barve stacka"| [0, 1, 2]|
|"Pob barve stacka"| [0, 1, 2]|
|"Max platlc barve stacka"| [0, 1, 2]|
|"top mid platlc barve stacka"| [0, 1, 2]|
|"bot mid barve stacka"| [0, 1, 2]|
|"Min platlc barve stacka"| [0, 1, 2]|
|"koliko tarokov se v igri"| list(range(23))|
|"zadnji player skrt barve"| [0, 1]|
|"vrednost prve karte"| [0, 2, 3, 4, 5]|


***Q tables for playing solo, third card***
|Variable name|Possible variable values|
|-------------|------------------------|
|"vrednost prve karte"| [0, 2, 3, 4, 5]|
|"vrednost druge karte"| [0, 2, 3, 4, 5]|
|"Jz skrt barve"| [0, 1]|
|"Lahko poberem"| [0, 1]|
|"Kralj barve stacka"| [0, 1, 2]|
|"Dama barve stacka"| [0, 1, 2]|
|"Kaval barve stacka"| [0, 1, 2]|
|"Pob barve stacka"| [0, 1, 2]|
|"Max platlc barve stacka"| [0, 1, 2]|
|"top mid platlc barve stacka"| [0, 1, 2]|
|"bot mid barve stacka"| [0, 1, 2]|
|"Min platlc barve stacka"| [0, 1, 2]|
|"koliko tarokov se v igri"| list(range(23))|


***Q tables for playing duo***  
We constructed the Q tables for playing duo the same way we did in STATE 3.


### ACTIONS 5
Actions for playing the first card of the round: "herc kral", "herc dama", "herc kaval", "herc pob", "herc platlc", "karo kral", "karo dama",
                    "karo kavla", "karo pob", "karo platlc", "pik kral", "pik dama", "pik kaval", "pik pob",
                    "pik platlc", "kriz kral", "kriz dama", "kriz kaval", "kriz pob", "kriz platlc",
                    "skis", "pagat", "mont", "nizki taroki", "srednji taroki", "visoki taroki"
                    
Actions for playing the second card of the round: "pass", "nalozi", "stegni", "all-in"   
Actions for playing the third card of the round: "spusti", "poberi", "nalozi"



## FUTURE PLANS
We already mentioned many possible improvements for every part (written in italics). The main focus should for now be to test and train all of the models with new and proposed reward functions. There is not much more experimentation, we can do when it comes to state representation, but perhaps minor changes can lead to drastic performance increases. There is still room for improvement when it comes to discretization of actions. Perhaps try the state 3 or 5 in combinations with actions 2. A great test would also be to deal exactly the same cards to each agent and see how differently they play and what are their strengths and weaknesses.

Then we would like to move on to different reinforcement learning approaches, starting with Deep Q learning.



