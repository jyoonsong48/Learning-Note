flavour <- readline("Which flavour do you prefer? (Answer should be Light/Bold) : ")
caffeine <- readline("Do you want caffeine in your tea? (Answer should be Yes/No) : ")

teahouse <-function(flavour, caffeine) {
  if (flavour == "Light" & caffeine == "Yes") {
    print("I recommend green tea for you!")
  }
  else if (flavour == "Light" & caffeine == "No") {
    print("I recommend chamomile tea for you!")
  }
  else if (flavour == "Bold" & caffeine == "Yes") {
    print("I recommend black tea for you!")
  }
  else if (flavour == "Bold" & caffeine == "No") {
    print("I recommend rooibos tea for you!")
  }
  else if (flavour == "Bold" | flavour == "Light" & caffeine != "Yes" & caffeine != "No") {
    print("Please answer Yes or No to your caffeine option")
  }
  else if (flavour != "Bold" & flavour != "Light" & caffeine == "Yes" | caffeine == "No") {
    print("Please answer Light or BoldLi to your flavour option")
  }
}

teahouse(flavour, caffeine)