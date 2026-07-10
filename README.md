In this project I was inspired by the concept of "center of mass" from my Calculus 2 class this summer
where we calculate, through the use of integrals, the center of an object given that the density is constant. 

I thought that maybe I could compare two financial metrics to each other to see if I could more deeply understand 
those metrics and the market as a whole. I decided to compare SP 500 returns and VIX changes because this could tell 
me, possibly, something about the relation between the overall market and perceived risk in that market. 

So I have sp 500 returns plotted on the x axis while having the vix changes on the y axis. Then, since the density of
my object is not constant I had to use gaussian kernal estimation (kde) to calculate the density of the plotted historical data, which 
I pulled from the yfinance python library. 

Using this kde approach I was able to have a total density that I could then calculate the center of mass for. Also, on the graph the 
changes in density within the plotted data are denoted by a change of color which I have provided a scale for.

![Here our time window is 21 trading days](/Users/anthonyvarriale/Desktop/Market Gravity Figure.png)

Then I marked the center of mass with a red X. This can show the changing relationship between these two metrics and allow me to 
more deeply understand how they behave in relation with each other, and over time. 

I am open to any type of feedback or instruction in how I might improve! This was my first coding project and I'm still learning 
so any type of help would be greatly appreciated! Thanks and have a great day! 
