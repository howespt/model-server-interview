# Simple model server

## Resources

- The internet
- Me
- Whatever else you need I'm not your dad

## Goal

Write a basic model server that does the following

- Loads a model from disk
- Serves that model at a route `/predict`

## Extension

- Add the ability to hot swap a model: given a URL, download the model and swap it out for the old one.
- Add the ability to run validations on input data and handle erroneous inputs
- Create an A/B testing framework where the predict endpoint serves one of N models with some probability specified by some config.
