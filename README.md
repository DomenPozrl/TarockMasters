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
