# PLOT

---



x <- seq(1, 10, by = 0.5)
m <- 1
c <- 3
y <- m * x + c
df <- data.frame(x, y)
print(df)
plot(df$x , df$y)


# ABLINE

---

x <- seq(1, 10, by = 0.5)
m <- 1
c <- 3
y <- m * x + c
df <- data.frame(x, y)
print(df)
plot(df$x , df$y) + abline(a=c,b=x, color = "red",lwd = 2)


# SET

---

set.seed(50)
x <- seq(1, 10, by = 0.5)
m <- 1
c <- 3
y <- m * x + c
df <- data.frame(x, y)
print(df)
plot(df$x , df$y) + abline(a=c,b=x, color = "red",lwd = 2)


# RNORM

---

x <- seq(1, 10, by = 0.5)
m <- 1
c <- 3
y <- m * x + c + rnorm (100 , 0 , 1)
df <- data.frame(x, y)
print(df)
plot(df$x , df$y) + abline(a=c,b=x, color = "red",lwd = 2)

# RUNIF

---

x <- runif(100,1,10)
m <- 1
c <- 3
y <- m * x + c + rnorm (100 , 0 , 1)
df <- data.frame(x, y)
print(df)
plot(df$x , df$y) + abline(a=c,b=x, color = "red",lwd = 2)

# RGL ->PLOT3D

---

x_val <- seq(0,10,length.out = 100)
y_val <- sin(x_val)
z_val <- cos(x_val)
plot3d(x_val,y_val,z_val,type = "l", col= "blue" , lwd = 2)

# REP

---

x <- rep(1,100)
y <- rnorm(100,0,1)
plot(df$x, df$y)
