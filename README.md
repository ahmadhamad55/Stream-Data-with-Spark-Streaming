# Stream-Data-with-Spark-Streaming
<img src="https://github.com/ahmadhamad55/Stream-Data-with-Spark-Streaming/blob/main/spark.png" alt="" width="500">

### English version 
In this challenge, I successfully implemented a streaming pipeline using Spark Streaming. The challenge was divided into two parts. 

For the first part, I read and streamed data from CSV files, specifically the provided employee data and its schema. I prepared a read stream DataFrame to read from a specific location where the CSV files were stored. I then computed the average salary for male and female employees, along with the count for each group. Finally, I sorted the results by average salary in descending order. I wrote the streaming output to the Spark console in an "appending" mode and started consuming the data. By sequentially copying the five data files to the specified HDFS location, I was able to observe the streaming results.

In the second part of the challenge, I modified the stream to read data from a socket on localhost:9999. I opened another terminal and began sending messages to the socket. I implemented a DataFrame to split each line into words and performed an aggregation to calculate the total count of each distinct word. The remaining steps were similar to the first part, including writing the stream to the Spark console and consuming the data.

Through this project, I demonstrated my proficiency in building streaming pipelines using Spark Streaming. I showcased my ability to process data from different sources, perform computations in real-time, and handle streaming data efficiently. This project highlights my skills in data streaming and analysis, as well as my familiarity with the Spark framework.

### French version
Dans ce défi, j'ai réussi à mettre en place un pipeline de streaming en utilisant Spark Streaming. Le défi était divisé en deux parties.

Pour la première partie, j'ai lu et diffusé des données à partir de fichiers CSV, plus précisément des données sur les employés fournies et leur schéma. J'ai préparé un DataFrame de lecture en continu pour lire à partir d'un emplacement spécifique où les fichiers CSV étaient stockés. J'ai ensuite calculé le salaire moyen des employés masculins et féminins, ainsi que le décompte pour chaque groupe. Enfin, j'ai trié les résultats par salaire moyen par ordre décroissant. J'ai écrit la sortie du streaming dans la console Spark en mode "appending" et j'ai commencé à consommer les données. En copiant séquentiellement les cinq fichiers de données dans l'emplacement HDFS spécifié, j'ai pu observer les résultats du streaming.

Dans la deuxième partie du défi, j'ai modifié le flux pour lire les données à partir d'une "socket" sur localhost:9999. J'ai ouvert un autre terminal et commencé à envoyer des messages à la socket. J'ai mis en place un DataFrame pour diviser chaque ligne en mots et j'ai effectué une agrégation pour calculer le décompte total de chaque mot distinct. Les étapes restantes étaient similaires à la première partie, y compris l'écriture du flux dans la console Spark et la consommation des données.

Grâce à ce projet, j'ai démontré ma maîtrise de la mise en place de pipelines de streaming en utilisant Spark Streaming. J'ai mis en valeur ma capacité à traiter des données provenant de différentes sources, à effectuer des calculs en temps réel et à gérer efficacement les données en continu. Ce projet met en évidence mes compétences en streaming de données et en analyse, ainsi que ma familiarité avec le framework Spark.
