random_character <- function() {
  sample(letters, 1)
}

print_sequence <- function(length) {
  length <- 20
  for(i in 1:length) {
    cat(paste0(random_character()))
    Sys.sleep(0.25)
   }
 }

print_sequence(length)