# Instructions for Sprint C

## Objectives
- Understand how to do integration testing  in the context of Flask applications.

## Introduction
In sprint B we created two views: one to serve epithets and one to serve the 
vocabulary used to generate epithets. Application logic to generate these 
views was abstracted out into three helper classes that were then unit tested 
to ensure each helper class behaves as expected. However, at this point we 
have not ensured our application is actually functional. Assuming all unit tests 
pass, we know components work in isolation but we do not know if each 
component is working together. This difference, between testing if components 
work in isolation vs in cooperation with each other, is the difference between 
unit and integration testing.

In order to serve epithets, the FileManager class must read the 
contents of a file at a given path. Next, the Vocabulary class must transform 
output of FileManager into a dictionary of lists keyed per column of the 
vocabulary. Then, the EpithetGenerator must select a random word from each column 
of the vocabulary and return a templated epithet. Finally, Flask must serve 
generated epithets for each incoming request. Where unit tests verify each step 
in this series is functional, we need to know if all steps of the series work 
together to serve epithets.

In this assignment we will continue where sprint B concluded by:
1. adding a route to serve a random number of epithets.
2. creating integration tests to verify each route serves its expected payload.




## Instructions
1. Watch [Web API Development with Flask: Using the Flask Test Client](https://www.youtube.com/watch?v=APbPtQg3_04)
2. Read [Flask-Testing's documentation](https://pythonhosted.org/Flask-Testing/).
3. Add one route that serves a random number of epithets.
4. Create integration tests using the Flask-Testing extension to verify each 
route serves its expected payload.

