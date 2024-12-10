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
