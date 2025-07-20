# Xpath -> Exclusive path of a locator

# Two types of Xpaths
# 1. Absolute Xpaths -> / -> /html/body/div[1]/div
# 2. Relative Xpaths -> // -> //tag[@attribute = value] -> //div[@class='large-12 columns']
# Relative xpaths are called Dynamic and absolute xpaths are static xpaths

# Parent-child relation
# Top-bottom ->//form[@id='checkboxes']/input
# //form[@id='checkboxes']/child::input (Traversing from parent to child)
# //input[@type='checkbox']/parent::form (Traversing from child to parent)
# //input[@type='checkbox']/preceding-sibling::input(Getting below sibling details)
# //input[@type='checkbox']/following-sibling::input(Getting above sibling details)


#//div[contains(@class,'large-4')] (checks for any match with value defined along with attribute)
# //div[starts-with(@class,'large-4')] (checks for starting with the value defined along with attribute)
