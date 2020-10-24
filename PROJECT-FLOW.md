# Project flow

## How the voting occurs

1. A person will create a group and can add students to it / invite the students
2. Every participant of the group will be awarded a set number of tokens when they join the group. This token count is encrypted with the user's master key and stored in the database. (We'll get to where it is stored later)
3. To create a **poll**, the admin can create a form with a question along with different voting options( can be a MCQ or a Y/N ).

   > can be done by displaying a form where the admin can create a question and some option, along with the polling date and time.

4. During the poll, the participant can pick his desired option quadratically.
5. His/ her vote is encrypted and sent to the server along with the zn-proofs verifying his vote satisfies the requirements, which are

- The vote should be a part of one of the options given in the poll.
- The person has enough tokens to cast his/her vote (ex: the person needs to have 9 tokens to purchase 3 votes)

6. This data is then stored in the server
7. After the polling, the results are calculated by secure Multi-Party-Computation (MPC), this is done by splitting the votes between all the voters and computing the result. _( not sure how we verify if the votes are valid during the MPC )._ **Problem: All the voters need to be online to perform MPC.**
8. The result is computed and announced. This is saved in the database in encrypted form.

## Schemas

### 1. User Schema

- user_id **Primary Key**
- Username **String(50)**
- Email id _( Preferably webmail, for proving one-person one-account)_ **String(50), unique**
- Password **String(150)** _(Unsure how we are gonna hash passwords. Therefore length is changeable)_
- Groups user is a part of **( 1. a )** _( Many to many relationship )_

  #### 1. a. Association Object for keeping track of tokens(User's Groups)

  - left_id **User_id**
  - right_id **group_id**
  - Token's left **string(300)** _( Encrypted with user's master key )_

### 2. Group Schema

- Group_id **Primary Key**
- Name **String(50)**
- Admin(s) **user_id**
- Members _( Many-many relationship )_ **( 1. a )**
- Polls **DataBase relationship to Poll Schema** _(One-Many Relationship)_

### 3. Poll Schema

- poll_id **primary key**
- Question **String(1000)**
- Polling start time **DateTime**
- Polling End Time **DateTime**
- Group the poll is a part of **ForeignKey, group_id** _( many-to-one relationship)_
- Options **Database relationship to options schema** _(One to many Relationship)_
- array of votes _( many-many relationships )_
- result ( ? ) **string(300)** _(Ambiguity: If we store it in plain someone not part of the group will be able to see the result. If we encrypt it with the admin's master key, the admin might be able to manipulate the result)_

  #### 3. a. Association Object For Votes

  - left_id **user_id**
  - right_id **poll_id**
  - Encrypted Vote **String(300)**

### 4 Options Schema

- option*id **poll_id ( primary key )** *( Poll to which the option belongs to )*
- option-description **string(50)**

## Main work

_Stuff, which requires a lot more research._

1. Figure out a zero-knowledge proof for the verifying vote
2. Develop a secure MPC model.

## Ambiguities

1. All voters need to be present to perform MPC.
2. Verifying the integrity of the vote while performing MPC.
3. What's the use of storing encrypted votes in the database.
4. Storing the result of a vote.
