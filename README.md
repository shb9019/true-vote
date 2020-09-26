# True Vote
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![Generic badge](https://img.shields.io/badge/Stage-Ideation-<COLOR>.svg)](https://shields.io/)

A collective decision making platform which uses a Quadratic Voting approach instead of the traditional one-person-one-vote method.

## Motivation

Being a college graduate, I've been a part of plenty of collective decisions being made. Decisions that are of different value to different participants. Some of them could be,

1. There is a sports tournament coming up which is clashing with a test. The class has to choose whether to prepone the test and let everyone attend it, or force the few people attending the tournament to cancel their trip.
2. It's raining heavily. There is an important class scheduled in an hour. Most students have umbrellas and transport, hence can make it to the class safely. Others don't have these luxuries. The class has to decide whether to postpone the class.
3. Club members have to decide whether to remove a person from the club. Not every member knows the candidate and only few have interacted with the candidate.

We go with a vote in these scenarios. But, there is a clear difference of majority and minority. Using a traditional One-Person One-Vote method, we assume that the outcome of the result affects all voters equally by giving all voters an equal voice. This creates the "Tyranny of the Majority". Voters who don't really care about the outcome are influencing the decision equally. 

## Quadratic Voting

An alternative to traditional voting can be a system where voters buy votes with tokens/money which is called One-Dollar One-Vote. This creates another problem. The decision can be heavily influenced by a minority.

Quadratic voting provides a neat intermediate solution. In simple terms, instead of valuing each vote equally, the cost to buy next vote increases linearly. Assuming every first vote by a voter costs 1$, the cost increases as follows,

Number of votes | Cost
--------------- | ----
1               | 1
2               | 4
3               | 9
4               | 16
5               | 25

Mathematically, `Cost to voter = (Number of votes)^2`. The squared is what gives the name Quadratic voting.

Voters can now show how much they value the result by buying multiple votes, but cannot influence heavily since the cost increases quadratically.

![Comparison](https://vitalik.ca/files/posts_files/qv-files/Market7.png?2e)


Read the paper by Glen Weyl and Steven Lalley [here](https://economics.rice.edu/sites/g/files/bxs876/f/Weyl%20(paper)%20-%20Feb%202017.pdf) to know more.

## What does TrueVote do?

TrueVote is a platform that can be set up by anyone to make collective decisions in an organization of their choice. Admins can create voting groups and add voters to these groups. All voters in a group receive a set initial number of voting tokens.

The admins (minimum of 5) of the voting group can organize a poll on a specific decision. Voters in the group can vote using the tokens they are allocated. Once a voter depetes all tokens, he/she cannot vote in the upcoming polls. Hence, the voters are incentivized to save their tokens for future polls. Optionally, a set number of tokens can be added to the wallets of users after every month/year. Voters cannot be added to the voting group after the first poll.

A voter can be a part of multiple voting groups and the voter has a balance of tokens in each voting group which cannot be transferred. After voting, the tokens used are burnt i.e., discarded.

## Tech Stack

The project will consist of a backend and a frontend. The backend can be on Ethereum, but this brings in unnecessary latency and can be highly inconvenient to use. We will be proceeding with a centralized but encrypted solution i.e., all of users data is completely inaccessible by the project/server maintainers and should only be decrypted by the voter's master key.

To be decided.

## Developers

[Sai Hemanth B](https://www.saihemanth.com/)
