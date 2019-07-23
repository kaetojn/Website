###Initial Plan:

We have a number of things planned to be completed by the demo.  This includes reviewing the difficulty of questions and adjusting how much time to it takes to answer them.  We will have the game played level by level, with a short lesson before the start of each one; this means we will have to implement a functional transition from one level to the next; this involves wiping the enemy array, the player, and displaying the next level’s lesson onto the game area.  This also means we will have to have some lessons completed; to this end, we plan to have at least a single level along with its lesson completed by the demo.

We also plan to have the scoreboard finished and fully functional, tallying up the total score and displayed properly.

We have decided that we will let the player answer any question that’s been posed but not yet answered; to do this, they will denote which question they are answering via an index.  This means we will have the questions placed in an array.

We plan to have the player sprite finished as well as implementing a shooting animation whenever the player answers a question correctly.


###Replanning:

Changing JTextArea for the console area to a JTextPane was a goal devised from the previous phase. This task was more difficult than previously expected. Using JTextArea originally proved to be a major oversight. More time can be put into solving this task but the gain (for now) is not worth the effort required. This task is shelved for now.

Initially, questions could be answered on a stack and plans were to allow the player to answer the latest question, (top of the stack). Through this phase, we changed the implementation of this feature to allow the player to answer any of the currently active questions. Regex and other functions were changed to allow for this. As such more tasks were presented (how to demonstrate that a question has been answered, correctly, incorrectly), and encoding more visual feedback.

Some of the implementations in the code for the game had to be redone. All Hashsets that acted as question containers, were reimplemented to be ArrayLists. Subsequently sections had to be refactored.

The initial vision to have a “wall” separating the player from the enemies was shelved. The feature was deemed not high enough on the list of priorities to be pursued for this phase. We decided to focus this phase on getting the major mechanics working.

Other feature thought up in the project’s initial stages were also shelved (at least for now). For example, upgrades etc. These features add to the experience but are not important for the main experience we are trying to build for the minimum viable product.

We have redesigned our levels so that they load a lesson for the player to study before actually playing the game. This is a replanning of our original idea of having wave based levels. For this we had to replan to actually design and incorporate the lessons. And encode transitions between them.



###Retrospective and Review:

Our plan was spread by giving each person a set of (high level) tasks (shown in sprint backlog of process report). These tasks/goals were then broken down with issues that we came across and sub tasks. For example, when working on the level transition we had to learn how to display/render the lessons for that level on the frame.


####What worked:

The score implementation had many different ideas. The one we used was with a new JLabel that was embedded in the corner of the screen. This worked just as intended and increments on every correct answer.

Putting the questions into an ArrayList/Stack worked well. Items could be removed and added efficiently. 

Changing the regex so that the player can specify which item or question on the stack to answer was completed. Also parsing errors and incorrect syntax is now presented to the player by printing out any exceptions that are thrown when parsing. This gives the player more information and feedback.


####What didn't work:

Initial game mechanics that seemed (at least for the minimum viable product) unnecessary.

The console: switching from the text area to a pane required a lot of refactoring. Ultimately (for now) the benefits did not outweigh the work necessary.

The wall Idea (as discussed previously) was shelved.

The previous idea for levels and level transition did not mesh well with our new idea of  lessons before each level. This required some replanning.

 
####Interesting Insights and Possible Improvements:

Deciding on the appropriate level of question difficulty for grades 5-6 students was tough.  We didn’t want our game to be too difficult, but we also wanted our game to introduce enough concepts to be worthwhile.  We are still debating on the appropriate difficulty level for some questions.

We will be thinking about the UX design for the game during this last phase. Making the game’s appearance appealing to kids will be an interesting endeavor. Many modern computer games have quite complex graphics, we’re hoping to appeal to kids with a simple interface and lessons with fonts similar to handwriting. 
