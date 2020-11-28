# TarockMasters

## THEORETICAL AGENTS
For purposes of evaluation of our trained models we devised a few theoretical agents.

- Random agent (random): Makes decisions randomly.

The following agents are a sort of cheating agents because they have more information than usually available to the player. They know every card in every hand instead of just their own. This of course is not possible in real world play, but results achieved with such agents present a great milestone for our trained models.

- Locally worst agent (LW): Plays the card that will, on average, produce the lowest possible score for that round.
- Locally best agent (LB): Plays the card that will, on average, produce the highest possible score for that round.
- Locally worst worst agent (LWW): Plays the card that will produce the lowest possible score for that round, but also takes into account that the other two players will play in the same way
- Locally best best agent (LBB): Plays the card that will produce the highest possible score for that round, but also takes into account that the other two players will play in the same way

*The last two agents are basically MINMAX trees for each specific round*

*Another possible theoretical agent we could use to evaluate our trained models is another cheating agent which also knows every card of every hand, but always plays by the principles of the Nash equilibrium.*

To test our trained models, we first constructed a set of all playing agents and calculated all possible permutations of playing agents of length 3 (for 3 players). Then we played 1000 games for each permutation where we selected the solo player and the duo players randomly. This gave is a total of 792000 played games. In the processing of results we also introduced a rule for deciding which hands are average, good or great: 

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
*This assessment of hand quality could also be done by taking the games where all three players played according to the same theoretical agent. The results of that game should tell us something about the quality of the hands. Perhaps even train a regression model?*

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



