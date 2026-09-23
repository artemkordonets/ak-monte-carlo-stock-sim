# ak-monte-carlo-stock-sim

Monte Carlo Stock Price Simulator

A Python-based Monte Carlo simulator for modelling possible stock-price paths using Geometric Brownian Motion (GBM).
The project shows how assumptions about expected annual return and volatility affect the distribution of possible future prices.

_**This project is actively being developed, with additional features planned**_
## Features:
  - Monte Carlo simulation of stock-price paths
  - Geometric Brownian Motion model is used in the simulator
  - (Formula used can be found on https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
  - Customisable initial price, expected return and volatility
  - 10,000 simulated paths
  - Two-year simulation period
  - Calculation of mean, median and standard deviation of terminal prices
  - Identification of extreme simulated outcomes
  - Visualisation of price paths and terminal-price distributions


## Technologies:
  - Python
  - NumPy - numerical computation and simulation
  - Matplotlib - data visualisation


## Example Parameters:
  - Initial price:       £100
  - Expected return:     8%
  - Annual volatility:   20%
  - Time horizon:        2 years
  - Simulations:         10,000


## Future Improvements:

  - Adding historical market data for parameter estimation
  - Comparing simulated distributions with historical returns
  - Calculating confidence intervals and percentiles
  - Implementing additional stochastic models
  - Adding backtesting functionality
  - Comparing simulated and observed price distributions
