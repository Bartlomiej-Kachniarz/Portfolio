# Portfolio
## This is my Machine Learning projects portfolio

Here you can find my projects ranging from pure python coding to advanced Machine Learning projects.

The repository shall be extended to contain Data Engineering as well as DevOps projects.

In case of any questions please contact me:

- [LinkedIn](https://www.linkedin.com/in/bart%C5%82omiej-kachniarz-5208b8153/)
- [e-mail](bart.kach@gmail.com)

### The repository structure is displayed below:

```bash
.
├── data_engineering
│   ├── airflow
│   │   ├── dags
│   │   │   ├── basic_etl_dag.py
│   │   │   ├── etl_1_extract_dag.py
│   │   │   ├── etl_2_transform_dag.py
│   │   │   ├── etl_3_load_dag.py
│   │   │   ├── one_task_dag.py
│   │   │   └── two_task_dag.py
│   │   ├── lab
│   │   │   └── db
│   │   │       ├── initialize_top_level_domains_db.py
│   │   │       └── sqlite_initialize_example_db.py
│   │   ├── airflow.cfg
│   │   ├── airflow.sh
│   │   ├── docker-compose.yaml
│   │   ├── install_airflow.sh
│   │   └── webserver_config.py
│   └── pyspark
│       ├── simple_app
│       │   └── simple_app.py
│       ├── etl.py
│       ├── pyspark_1.py
│       ├── pyspark_by_examples.ipynb
│       ├── pyspark_template.ipynb
│       └── quickstart.ipynb
├── java
│   └── training
│       └── Hello.java
├── machine_learning
│   ├── NLP
│   │   ├── sentiment_analysis
│   │   │   ├── hugging_face.ipynb
│   │   │   └── nltk.ipynb
│   │   ├── word2vec
│   │   │   └── nlp.ipynb
│   │   └── youtube_llm
│   │       └── youtube_llm.ipynb
│   ├── apartment_for_rent
│   │   └── apartments.ipynb
│   ├── clusters
│   │   └── comparison_of_algorithms.ipynb
│   ├── decision_trees
│   │   └── iris_dtree.png
│   ├── meteorite_landings
│   │   └── meteorite_landings_analysis.ipynb
│   ├── mnist
│   │   └── mnist_digits.ipynb
│   ├── msl-images
│   │   └── README.md
│   └── mushrooms_dataset
│       ├── README.md
│       └── mushrooms.ipynb
├── python
│   ├── api
│   │   ├── using_apis.ipynb
│   │   └── using_apis.py
│   ├── data_structures
│   │   ├── deque.py
│   │   ├── queue_ll.py
│   │   └── stack_class.py
│   ├── decorators
│   │   ├── decorators.py
│   │   ├── decorators_calls.py
│   │   └── plugins_calls.py
│   ├── design_patterns
│   │   ├── abstract_factory
│   │   │   └── car_app.py
│   │   └── factory_method
│   │       ├── logistics_app.py
│   │       └── shipments.py
│   ├── dto
│   │   └── game_character.ipynb
│   ├── games_in_python
│   │   ├── connectfour.py
│   │   ├── snake.py
│   │   └── tetris.py
│   ├── neural_networks_from_scratch
│   │   └── mlp.py
│   ├── training
│   │   ├── asyncio
│   │   │   └── train_asyncio.py
│   │   ├── numpy
│   │   │   └── numpy.ipynb
│   │   ├── tests
│   │   │   └── test_counting_partitions.py
│   │   ├── counting_partitions.py
│   │   ├── exercise_matrix_rhomb.py
│   │   ├── exercise_operator.py
│   │   ├── exercise_trip.py
│   │   ├── general_python.ipynb
│   │   └── pandas.ipynb
│   └── web_scraping_projects
│       ├── books_to_scrape
│       │   └── books_to_scrape
│       │       └── spiders
│       │           └── books2scrape.py
│       ├── ebay
│       │   └── ebay
│       │       ├── spiders
│       │       │   └── ebay_books.py
│       │       └── books.json
│       ├── glasses
│       │   ├── glasses
│       │   │   └── spiders
│       │   │       └── glasses_shop.py
│       │   └── glasses.json
│       ├── imdb
│       │   └── imdb
│       │       └── spiders
│       │           ├── rating_10k.py
│       │           └── top_imdb_movies.py
│       ├── livecoin
│       │   └── livecoin
│       │       └── spiders
│       │           └── coin.py
│       ├── national_debt
│       │   └── national_debt
│       │       └── spiders
│       │           └── gdp_debt.py
│       ├── quotes
│       │   └── quotes
│       │       └── spiders
│       │           └── quotess.py
│       └── worldometers
│           └── worldometers
│               ├── spiders
│               │   └── countries.py
│               ├── runner.py
│               └── runner_2.py
├── scala
│   ├── firstApp
│   │   ├── project
│   │   │   └── build.properties
│   │   ├── src
│   │   │   └── main
│   │   │       └── scala
│   │   │           └── SimpleApp.scala
│   │   └── build.sbt
│   └── training
│       ├── Hello.scala
│       ├── WindowFunctions.scala
│       └── pi.scala
├── sql
│   └── postgre_sql
│       └── Advanced SQL AppDev
│           ├── Database Errors.ipynb
│           ├── Parameterized Query Challenge Solution.ipynb
│           └── SQL Alchemy quering.ipynb
├── LICENSE.txt
├── README.md
├── requirements.txt
├── setup.cfg
└── setup.py
``````

<!-- create the new tree by running: -->
<!-- tree . -I '__pycache__|mlruns|__init__.py|.DS_Store|venv/|.git/|.metals/|.vscode/|.ipynb_checkpoints|*.csv|*.shp|*.shx|*.dbf|*.prj|*.bin|.scala-build|*.npy|*.npz|*ubyte|*ed.txt|*.Z|cardiffnlp|data.txt|index.txt|tetrisscores.txt|agaricus-lepiota.txt|items.py|middlewares.py|pipelines.py|settings.py|scrapy.cfg|example*|*.out|*.sql' --dirsfirst -a --gitignore --prune -->

<!-- pipreqs --scan-notebooks --force --ignore machine_learning/NLP/word2vec/ -->