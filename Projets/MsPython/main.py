
import data
import Sentences
import Affichage

your_name,surname,age,city,job= data.donnee()
res= Sentences.yourName(your_name)
res= res + Sentences.surnam(surname)
res= res + Sentences.Age(age)
res= res + Sentences.City(city)
res= res + Sentences.Job(job)
Affichage.afficher(res)






