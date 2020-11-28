# TarockMasters

## THEORETICAL AGENTS
For purposes of evaluation of our trained models we devised a few theoretical agents.

- Random agent (random): Makes decisions randomly.

The following agents are a sort of cheating agents because they have more information than usually available to the player. They know every card in every hand instead of just their own. This of course is not possible in real world play, but results achieved with such agents present a great milestone for our trained models.

- Locally worst agent (LW): Plays the card that will, on average, produce the lowest possible score for that round.
- Locally best agent (LB): Plays the card that will, on average, produce the highest possible score for that round.
- Locally worst worst agent (LWW): Plays the card that will produce the lowest possible score for that round, but also takes into account that the other two players will play in the same way
- Locally best best agent (LBB): Plays the card that will produce the highest possible score for that round, but also takes into account that the other two players will play in the same way

*The last two agents (LWW and LBB) are basically MINMAX trees for each specific round*

*Another possible theoretical agent we could use to evaluate our trained models is another cheating agent which also knows every card of every hand, but always plays by the principles of the Nash equilibrium.*

To test our trained models, we first constructed a set of all playing agents and calculated all possible permutations of playing agents of length 3 (for 3 players). Then we played 1000 games for each permutation where we selected the solo player and the duo players randomly. This gave us a total of 792000 played games. For starters testing was only done either over all played games or a single Q agent playing with two of the same theoretical agents. There is a lot more test we could run. This just scratches the surface.

*Of course we should also do testing versus other Tarock playing applications and real life play.*

In the processing of results we also introduced a rule for deciding which hands are average, good or great: 

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

## LEARNING
We used the QLearning method to train our models with a slight but significant change. Due to the complexity of the game we do not add the score of the new state to the reward for the action in the previous state. 
We devised two sets of rewarding functions: 
One deals out rewards according to the points of won/lost stack and weighted by the number of actions we had available to play.
The other takes the above mentioned score, and further increases/decreases it based on some domain knowledge.

*There are a few possible improvements here. We could expand the second reward function with even more domain knowledge, but a far more interesting improvement would be to follow the classic QLearning method and add the score of the new state to the action in the previous state. We would have to make sure to take from the correct Q table and change the reward from positive to negative (or vice-versa) when the situation called for it. Hopefully this would help the model to learn some long term strategies*


## Q AGENTS
So far we've tried to train 5 different Q Learning models. Each with a unique set of state representations and actions. From here on we will refer to them as X_Y Q Agents where X stands for the type of state representation and Y for the type of actions.

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

### 1_1 Q AGENT
The below image shows the average number of points the 1_1 Q agent scored playing solo versus two of the same theoretical agents.

![1_1 average results](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/1_1%20Q%20agent%20playing%20vs%202%20theoretical%20agents.png)

The below image shows the average number of points the 1_1 Q agent scored playing solo versus two of the same theoretical agents with respect to the quality of the cards.

![1_1 average results quality](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/1_1%20Q%20agent%20vs%202%20theoretical%20agents%20with%20respect%20to%20quality%20of%20cards.png)

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


### 2_2 Q AGENT
The below image shows the average number of points the 2_2 Q agent scored playing solo versus two of the same theoretical agents.

![2_2 average results](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/2_2%20Q%20agent%20playing%20vs%202%20theoretical%20agents.png)

The below image shows the average number of points the 2_2 Q agent scored playing solo versus two of the same theoretical agents with respect to the quality of the cards.

![2_2 average results quality](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/2_2%20Q%20agent%20vs%202%20theoretical%20agents%20with%20respect%20to%20quality%20of%20cards.png)

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


### 3_3 Q AGENT
The below image shows the average number of points the 3_3 Q agent scored playing solo versus two of the same theoretical agents.

![3_3 average results](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/3_3%20Q%20agent%20playing%20vs%202%20theoretical%20agents.png)

The below image shows the average number of points the 3_3 Q agent scored playing solo versus two of the same theoretical agents with respect to the quality of the cards.

![3_3 average results quality](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/3_3%20Q%20agent%20vs%202%20theoretical%20agents%20with%20respect%20to%20quality%20of%20cards.png)


### STATE 4
Q table would be one where each variable of the state is each card in the deck described as, discarded, not in our hand or in our hand. We assumed that this state representation would create a Q table that is too big to fit in memory. We tested this and could not fit it into 16GB of RAM.


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


### 5_5 Q AGENT

The below image shows the average number of points the 5_5 Q agent scored playing solo versus two of the same theoretical agents.

![5_5 average results](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/5_5%20Q%20agent%20playing%20vs%202%20theoretical%20agents.png)

The below image shows the average number of points the 5_5 Q agent scored playing solo versus two of the same theoretical agents with respect to the quality of the cards.

![5_5 average results quality](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/5_5%20Q%20agent%20vs%202%20theoretical%20agents%20with%20respect%20to%20quality%20of%20cards.png)

## FINAL RESULTS
Finally, we present the average points across all games played by every mentioned model as a solo player and as a duo player

![solo_players](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/Average%20number%20of%20points%20for%20solo%20play.png)
![duo_players](https://github.com/DomenPozrl/TarockMasters/blob/main/Plots/Average%20number%20of%20points%20for%20duo%20play.png)






