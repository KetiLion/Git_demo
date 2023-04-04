# 7.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
# http://suninjuly.github.io/xpath_examples

# XPATH
/html/body/div[2]/button[3]
//body/div[2]/button[3]
//div[2]/button[3]
//button[3][text() ='Gold']
//* [contains(text(),'Gold')]
//button [contains(text(),'Gold')]
//button [contains(text(),'Gol')]

# CSS
div:nth-child(2) button:nth-child(3)
div:nth-child(2) .btn:nth-child(3)