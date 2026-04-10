library(testthat)
source("believe.R")

test_that("computes factorial correctly", {
  expect_equal(factorial_recursive(0), 1)
  expect_equal(factorial_recursive(1), 1)
  expect_equal(factorial_recursive(5), 120)
  expect_equal(factorial_recursive(7), 5040)
})

test_that("handling errors", {
  expect_error(factorial_recursive(-1), "Input must be a non-negative integer")
  expect_error(factorial_recursive(3.5), "Input must be a non-negative integer")
  expect_error(factorial_recursive("cs50"), "Input must be a non-negative integer")
})

test_that("0!", {
  expect_equal(factorial_recursive(0), 1)
})


test_that("tad bit more to fit the checker system", {
  expect_equal(factorial_recursive(3), 6)
})