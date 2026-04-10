library(stringr)
library(testthat)

test_that ("number of char", {
  expect_equal(str_length("a"), 1)
  expect_equal(str_length("as"), 2)
  expect_equal(str_length("the"), 3)
  expect_equal(str_length("qwer"), 4)
})

test_that ("nothing as input", {
  expect_equal(str_length(NA), NA_integer)
  expect_equal(str_length(c(NA, ab)), c(NA, ab))
  expect_equal(str_length("NA"), 2)
  expect_equal(str_length(NaN), NaN_integer)
})

test_that ("number as input", {
  expect_equal(str_length(factor(a)), 1)
  expect_equal(str_length(factor(ab)), 2)
  expect_equal(str_length(factor(abc)), 3)
  expect_equal(str_length(factor(df)), 2)
})

test_that ("number as input", {
  expect_equal(str_length(1), 1)
  expect_equal(str_length(-1), 1)
  expect_equal(str_length(124), 3)
  expect_equal(str_length(-24), 2)
})