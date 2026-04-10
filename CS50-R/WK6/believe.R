factorial_recursive <- function(n) {
  if (!is.numeric(n) || n < 0 || n != floor(n)) {
    stop("Input must be a non-negative integer")
  }
  if (n == 0) return(1)
  n * factorial_recursive(n - 1)
}